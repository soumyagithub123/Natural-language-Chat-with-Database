import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def nl_to_sql(nl_query, schema, db_type="mysql"):
    """
    Convert natural language query to SQL using Groq AI
    """
    schema_text = "\n".join([f"Table {t}: {', '.join(cols)}" for t, cols in schema.items()])
    prompt = f"""
    You are an expert SQL assistant.
    The connected database type is {db_type.upper()}.
    Convert the user's natural language request into a valid {db_type.upper()} SQL query.
    Ensure syntax is strictly compatible with {db_type.upper()}.
    
    Database Schema:
    {schema_text}

    User Request:
    {nl_query}

    Return only the SQL query without any explanation or markdown formatting.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        sql = response.choices[0].message.content.strip()
        # Remove markdown if any
        sql = sql.replace("```sql", "").replace("```", "").strip()
        return sql

    except Exception as e:
        return f"-- Error generating SQL: {e}"
