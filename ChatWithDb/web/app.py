import streamlit as st
from db_mysql import connect_server, connect_db, get_databases, get_schema_info, execute_query
from ai_query import nl_to_sql
import pandas as pd

st.set_page_config(page_title="ChatWithDB", layout="wide")

st.title("💬 ChatWithDB — AI + SQL (MySQL Edition)")

# -------------------- STEP 1: CONNECTION DETAILS --------------------
with st.sidebar:
    st.header("🔌 Connect to MySQL Server")
    host = st.text_input("Host", value="localhost")
    user = st.text_input("Username", value="root")
    password = st.text_input("Password", type="password")

    if st.button("Connect"):
        try:
            conn = connect_server(host, user, password)
            st.session_state["conn_server"] = conn
            st.success("✅ Connected to MySQL Server!")
        except Exception as e:
            st.error(f"❌ Connection failed: {e}")

# -------------------- STEP 2: DATABASE SELECTION --------------------
if "conn_server" in st.session_state:
    conn_server = st.session_state["conn_server"]
    databases = get_databases(conn_server)

    selected_db = st.sidebar.selectbox("Select Database", databases)
    if st.sidebar.button("Use this Database"):
        try:
            db_conn = connect_db(host, user, password, selected_db)
            st.session_state["db_conn"] = db_conn
            st.success(f"✅ Connected to database: {selected_db}")
        except Exception as e:
            st.error(f"❌ Failed to select DB: {e}")

# -------------------- STEP 3: CHAT/QUERY SECTION --------------------
if "db_conn" in st.session_state:
    db_conn = st.session_state["db_conn"]
    schema = get_schema_info(db_conn)

    with st.sidebar.expander("📘 Database Schema", expanded=False):
        for t, cols in schema.items():
            st.write(f"**{t}**: {', '.join(cols)}")

    mode = st.radio("Choose Mode", ["🧠 Natural Language", "🧾 SQL Query"])

    if mode == "🧠 Natural Language":
        nl_query = st.text_input("Ask in natural language:")
        if st.button("Run"):
            if nl_query:
                sql = nl_to_sql(nl_query, schema, db_type="mysql")
                st.code(sql, language="sql")
                result = execute_query(db_conn, sql)
                if isinstance(result, pd.DataFrame):
                    st.dataframe(result)
                else:
                    st.write(result)

    elif mode == "🧾 SQL Query":
        sql_query = st.text_area("Write your SQL query here:")
        if st.button("Execute SQL"):
            result = execute_query(db_conn, sql_query)
            if isinstance(result, pd.DataFrame):
                st.dataframe(result)
            else:
                st.write(result)
else:
    st.info("👈 Please connect to your MySQL server and select a database first.")
