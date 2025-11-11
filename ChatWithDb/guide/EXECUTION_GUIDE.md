# ChatWithDB - Quick Execution Guide

## ✅ Your Setup is Ready!

All dependencies are installed and both features are available.

## 🚀 Quick Start

### 1. Run the Application

```bash
python main.py
```

### 2. Enter Database Credentials

You'll be prompted for:
- **Host**: [localhost] (press Enter for default)
- **User**: [root] (press Enter for default)
- **Password**: Enter your MySQL password
- **Database**: Enter your database name (required)

### 3. Select Query Mode

You'll see two options:
- **Option 1**: Direct SQL Queries
- **Option 2**: Natural Language Queries

## 📝 Using Feature 1: Direct SQL Queries

1. Select **Option 1** when prompted
2. Enter SQL queries directly:

```
SQL> SELECT * FROM startups;
SQL> SELECT name, funding FROM startups WHERE funding > 1000000;
SQL> INSERT INTO startups (name, industry, funding) VALUES ('NewCo', 'Tech', 500000);
```

3. Results will be displayed in formatted tables
4. Type `quit` or `exit` to exit

## 🤖 Using Feature 2: Natural Language Queries

1. Select **Option 2** when prompted
2. Enter questions in natural language:

```
Query> Show me all startups
Query> Count the number of startups in each industry
Query> Find startups with funding greater than 1000000
Query> What is the average funding per industry?
```

3. The AI will convert your question to SQL
4. The SQL will be executed automatically
5. Results will be displayed

## 🔄 Switching Between Modes

You can switch between modes anytime:
- Type `switch` in SQL mode to go to Natural Language mode
- Type `switch` in Natural Language mode to go to SQL mode

## 📋 Available Commands

Both modes support:
- `help` - Show help message
- `quit`/`exit`/`q` - Exit the application
- `switch` - Switch between SQL and Natural Language modes
- `clear`/`cls` - Clear screen

## 🎯 Example Session

```
D:\ChatWithDb> python main.py

Please enter your database credentials:
Host [localhost]: 
User [root]: 
Password: ********
Database: data

Connecting to MySQL database 'data' at localhost...
✓ Successfully connected to the database!

============================================================
System Diagnostics
============================================================
Groq library installed: ✓ Yes
python-dotenv available: ✓ Yes
.env file status: .env file exists and contains GROQ_API_KEY
GROQ_API_KEY found: ✓ Yes
============================================================

============================================================
ChatWithDB - Query Mode Selection
============================================================
Select query mode:
  1. Direct SQL Queries (enter SQL directly)
  2. Natural Language Queries (converted to SQL via LLM)
============================================================

Enter your choice (1 or 2): 2

============================================================
ChatWithDB - Natural Language Query Mode (Option 2)
============================================================
Enter your queries in natural language. They will be converted to SQL automatically.
Type 'quit' or 'exit' to exit.
Type 'help' for available commands.
Type 'switch' to switch to SQL mode (Option 1).

Query> Show me all startups

🔄 Converting to SQL...
📝 Generated SQL: SELECT * FROM startups

⚡ Executing query...

name          | industry       | funding
--------------|----------------|----------
TechCorp      | Technology     | 5000000
DataInc       | Data Analytics | 2000000

(2 row(s) returned)

Query> switch

============================================================
ChatWithDB - SQL Query Mode (Option 1)
============================================================
Enter your SQL queries directly.
Type 'quit' or 'exit' to exit.
Type 'help' for available commands.
Type 'switch' to switch to Natural Language mode (Option 2).

SQL> SELECT COUNT(*) as total FROM startups;

total
-----
2

(1 row(s) returned)

SQL> quit

Exiting...
✓ Database connection closed.
```

## 🛠️ Troubleshooting

### If SQL Mode Doesn't Work:
1. Verify MySQL server is running
2. Check your database credentials
3. Ensure the database exists
4. Check firewall settings

### If Natural Language Mode Doesn't Work:
1. Verify `.env` file exists with `GROQ_API_KEY=your-key`
2. Check your internet connection
3. Verify your Groq API key is valid
4. Check API usage limits

### Common Errors:

**"Error connecting to MySQL database"**
- Check MySQL server is running
- Verify credentials are correct
- Ensure database name is correct

**"Natural Language mode is not available"**
- Check `.env` file exists
- Verify `GROQ_API_KEY` is set correctly
- Install dependencies: `pip install groq python-dotenv`

**"Rate limit exceeded"**
- Wait a moment and try again
- Check your Groq API usage limits

## ✅ Verification

Before running, verify your setup:

```bash
python verify_setup.py
```

This will check:
- ✓ All dependencies are installed
- ✓ .env file exists (if using Natural Language mode)
- ✓ GROQ_API_KEY is set (if using Natural Language mode)

## 🎉 You're Ready!

Both features are fully functional and ready to use. Start with:

```bash
python main.py
```

Happy querying! 🚀


