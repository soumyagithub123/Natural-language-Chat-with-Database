# ChatWithDB - Setup and Execution Guide

## Overview
ChatWithDB is a powerful CLI application that supports **TWO FEATURES**:
1. **Direct SQL Queries** - Execute SQL queries directly
2. **Natural Language Queries** - Convert natural language to SQL using AI (Groq API)

## Prerequisites

### Required (for both features):
- Python 3.7 or higher
- MySQL Server 5.7+ or 8.0+
- MySQL database credentials (host, user, password, database name)

### Optional (for Natural Language feature):
- Groq API key (get one from https://console.groq.com/)
- Internet connection (for API calls)

## Installation Steps

### Step 1: Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `mysql-connector-python` - For MySQL database connections
- `groq` - For natural language to SQL conversion (optional)
- `python-dotenv` - For loading API keys from .env file (optional but recommended)

### Step 2: Set Up Natural Language Feature (Optional)

If you want to use the Natural Language query feature:

1. **Get a Groq API Key:**
   - Visit https://console.groq.com/
   - Sign up or log in
   - Create an API key

2. **Create a .env file:**
   ```bash
   # Create .env file in the project directory
   echo GROQ_API_KEY=your-api-key-here > .env
   ```
   
   Or manually create a `.env` file with:
   ```
   GROQ_API_KEY=your-api-key-here
   ```

   **Important:** Replace `your-api-key-here` with your actual Groq API key.

3. **Alternative (Development only):**
   ```bash
   # Windows PowerShell
   $env:GROQ_API_KEY="your-api-key-here"
   
   # Windows CMD
   set GROQ_API_KEY=your-api-key-here
   
   # Linux/Mac
   export GROQ_API_KEY='your-api-key-here'
   ```

## Running the Application

### Basic Usage

```bash
python main.py
```

### Command-Line Options

```bash
# Interactive mode (prompts for all credentials)
python main.py

# With command-line arguments
python main.py --host localhost --user root --database mydb

# Full example
python main.py --host localhost --user root --database mydb --ssl-disabled
```

### Available Options:
- `--host` or `-H`: MySQL server host (default: localhost)
- `--user` or `-u`: MySQL username (default: root)
- `--database` or `-d`: Database name (required)
- `--password` or `-p`: Prompt for password (always prompted for security)
- `--ssl-disabled`: Disable SSL connection (default: True)

## Using the Application

### Step 1: Enter Database Credentials

When you run the application, you'll be prompted for:
- **Host**: Your MySQL server host (default: localhost)
- **User**: Your MySQL username (default: root)
- **Password**: Your MySQL password (hidden input)
- **Database**: Your database name (required)

### Step 2: System Diagnostics

The application will show system diagnostics:
- Groq library installation status
- python-dotenv availability
- .env file status
- GROQ_API_KEY availability

### Step 3: Select Query Mode

You'll be prompted to choose between:

#### Option 1: Direct SQL Queries
- Enter SQL queries directly
- Immediate execution
- No API key required
- Works offline

#### Option 2: Natural Language Queries
- Enter questions in natural language
- Automatically converted to SQL
- Requires Groq API key
- Requires internet connection

**Note:** If Natural Language mode is not available, you'll see helpful error messages explaining how to set it up.

### Step 4: Execute Queries

#### In SQL Mode:
```
SQL> SELECT * FROM startups LIMIT 5;
```

#### In Natural Language Mode:
```
Query> Show me all startups
Query> Count the number of startups in each industry
Query> Find startups with funding greater than 1000000
```

### Available Commands

Both modes support:
- `help` - Show help message
- `quit` or `exit` or `q` - Exit the application
- `switch` - Switch between SQL and Natural Language modes
- `clear` or `cls` - Clear screen

## Feature 1: Direct SQL Queries

### How It Works:
1. Select option 1 when prompted
2. Enter SQL queries directly
3. Results are displayed in formatted tables
4. Supports all MySQL queries (SELECT, INSERT, UPDATE, DELETE, etc.)

### Example:
```
SQL> SELECT name, industry, funding FROM startups WHERE funding > 1000000 ORDER BY funding DESC;

name          | industry       | funding
--------------|----------------|----------
TechCorp      | Technology     | 5000000
DataInc       | Data Analytics | 2000000

(2 row(s) returned)
```

### Features:
- ✅ Real-time query execution
- ✅ Formatted result display
- ✅ Error handling with clear messages
- ✅ Transaction support (automatic commit/rollback)
- ✅ Works offline

## Feature 2: Natural Language Queries

### How It Works:
1. Select option 2 when prompted (requires Groq API key)
2. Enter questions in natural language
3. AI converts your question to SQL
4. SQL is executed automatically
5. Results are displayed

### Example:
```
Query> Show me all startups in the technology industry

🔄 Converting to SQL...
📝 Generated SQL: SELECT * FROM startups WHERE industry = 'Technology'

⚡ Executing query...

name          | industry   | funding
--------------|------------|----------
TechCorp      | Technology | 5000000
DevStudio     | Technology | 1000000

(2 row(s) returned)
```

### Features:
- ✅ Natural language to SQL conversion
- ✅ Automatic schema detection
- ✅ Smart query generation
- ✅ Error handling and retry suggestions
- ✅ Works with complex queries

### Natural Language Query Examples:
- "Show me all startups"
- "Count the number of startups in each industry"
- "Find startups with funding greater than 1000000"
- "List the top 5 startups by funding"
- "Show me startups founded after 2020"
- "What is the average funding per industry?"

## Troubleshooting

### Issue: "Error connecting to MySQL database"
**Solution:**
- Verify MySQL server is running
- Check host, username, and password
- Ensure database name is correct
- Check firewall settings

### Issue: "Natural Language mode is not available"
**Solutions:**
1. **Groq library not installed:**
   ```bash
   pip install groq
   ```

2. **API key not set:**
   - Create `.env` file with `GROQ_API_KEY=your-key`
   - Or set environment variable

3. **API key invalid:**
   - Verify your API key at https://console.groq.com/
   - Check for typos in the .env file
   - Ensure no extra spaces around the `=` sign

### Issue: "Table doesn't exist" or "Column not found"
**Solution:**
- Verify table and column names
- Check database schema
- Use `SHOW TABLES;` to list tables
- Use `DESCRIBE table_name;` to see table structure

### Issue: "Rate limit exceeded"
**Solution:**
- Wait a moment and try again
- Check your Groq API usage limits
- Consider upgrading your API plan

### Issue: "Network error"
**Solution:**
- Check your internet connection
- Verify firewall settings
- Check if Groq API is accessible

## Switching Between Modes

You can switch between SQL and Natural Language modes at any time:

1. Type `switch` in the current mode
2. You'll be switched to the other mode
3. Continue querying in the new mode

**Note:** Switching to Natural Language mode requires:
- Groq library installed
- Valid GROQ_API_KEY set

## Best Practices

1. **Security:**
   - Never commit `.env` file to version control
   - Use strong database passwords
   - Keep API keys secure

2. **Performance:**
   - Use specific queries (avoid SELECT *)
   - Add appropriate WHERE clauses
   - Use indexes for large tables

3. **Natural Language Queries:**
   - Be specific in your questions
   - Mention table and column names when possible
   - Review generated SQL before execution (displayed automatically)

4. **Error Handling:**
   - Read error messages carefully
   - Check SQL syntax if query fails
   - Verify table/column names

## Advanced Usage

### Using with Different Databases

```bash
# Connect to remote database
python main.py --host remote-server.com --user admin --database production_db

# Connect with SSL enabled (remove --ssl-disabled)
python main.py --host secure-server.com --user admin --database secure_db
```

### Environment Variables

You can set database credentials as environment variables (not recommended for production):

```bash
# Windows PowerShell
$env:DB_HOST="localhost"
$env:DB_USER="root"
$env:DB_NAME="mydb"

# Then run
python main.py
```

## Support

For issues or questions:
1. Check error messages for guidance
2. Review this setup guide
3. Verify all dependencies are installed
4. Check database and API connectivity
5. Review the main README.md file

## Summary

✅ **Feature 1 (SQL Mode)**: Always available, works offline
✅ **Feature 2 (Natural Language Mode)**: Requires Groq API key, needs internet

Both features are fully functional and ready to use!


