# ChatWithDB - Interactive MySQL Database Client

A powerful command-line MySQL database client with **TWO FEATURES**:
1. **Direct SQL Queries** - Execute SQL queries directly
2. **Natural Language Queries** - Convert natural language to SQL using AI (Groq API)

## ✨ Features

### Feature 1: Direct SQL Queries
- 🔐 **Secure Credential Input**: Enter credentials at runtime (no hardcoded passwords)
- 💬 **Interactive Query Mode**: Execute multiple SQL queries in one session
- 📊 **Formatted Results**: Beautiful table formatting for query results
- ⚠️ **Error Handling**: Comprehensive error handling with clear messages
- 🔄 **Transaction Support**: Automatic commit/rollback functionality
- 🪟 **Windows Compatible**: Fully tested on Windows 10+

### Feature 2: Natural Language Queries
- 🤖 **AI-Powered**: Convert natural language to SQL using Groq API
- 🧠 **Smart Conversion**: Automatically understands your questions
- 📋 **Schema Awareness**: Uses database schema for accurate queries
- 🔍 **Error Recovery**: Helpful error messages and suggestions
- 🌐 **Internet Required**: Needs Groq API key and internet connection

## 🚀 Quick Start

### Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Natural Language Feature (Optional)**
   ```bash
   # Create .env file with your Groq API key
   echo GROQ_API_KEY=your-api-key-here > .env
   ```
   Get your API key from: https://console.groq.com/

### Running the Application

```bash
python main.py
```

## 📖 Usage

### Step 1: Enter Database Credentials
- Host: Your MySQL server (default: localhost)
- User: Your MySQL username (default: root)
- Password: Your MySQL password (hidden)
- Database: Your database name (required)

### Step 2: Select Query Mode

#### Option 1: Direct SQL Queries
```
SQL> SELECT * FROM startups LIMIT 5;
SQL> SELECT name, funding FROM startups WHERE funding > 1000000;
```

#### Option 2: Natural Language Queries
```
Query> Show me all startups
Query> Count the number of startups in each industry
Query> Find startups with funding greater than 1000000
```

### Available Commands
- `help` - Show help message
- `quit`/`exit`/`q` - Exit the application
- `switch` - Switch between SQL and Natural Language modes
- `clear`/`cls` - Clear screen

## 📋 Requirements

### Required (for both features):
- Python 3.7+
- MySQL Server 5.7+ or 8.0+
- mysql-connector-python

### Optional (for Natural Language feature):
- groq (for AI-powered queries)
- python-dotenv (for .env file support)
- Groq API key
- Internet connection

## 🔧 Setup Details

### Basic Setup (SQL Mode Only)
```bash
pip install mysql-connector-python
python main.py
```

### Full Setup (Both Features)
```bash
pip install -r requirements.txt
# Create .env file with GROQ_API_KEY=your-key
python main.py
```

## 📚 Examples

### SQL Mode Example
```
SQL> SELECT name, industry, funding FROM startups ORDER BY funding DESC LIMIT 5;

name          | industry       | funding
--------------|----------------|----------
TechCorp      | Technology     | 5000000
DataInc       | Data Analytics | 2000000
...

(5 row(s) returned)
```

### Natural Language Mode Example
```
Query> Show me the top 5 startups by funding

🔄 Converting to SQL...
📝 Generated SQL: SELECT * FROM startups ORDER BY funding DESC LIMIT 5

⚡ Executing query...

[Formatted results displayed]
```

## 🛠️ Troubleshooting

### Connection Issues
- Verify MySQL server is running
- Check credentials (host, user, password, database)
- Ensure database exists
- Check firewall settings

### Natural Language Mode Not Available
1. **Install groq library:**
   ```bash
   pip install groq
   ```

2. **Set up API key:**
   - Create `.env` file: `GROQ_API_KEY=your-api-key`
   - Or set environment variable: `export GROQ_API_KEY='your-key'`

3. **Get API key:**
   - Visit https://console.groq.com/
   - Sign up and create an API key

### Query Errors
- Check SQL syntax
- Verify table and column names
- Review error messages for details
- Use `SHOW TABLES;` to list tables
- Use `DESCRIBE table_name;` to see table structure

## 📖 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup and usage instructions
- **[CHANGES.md](CHANGES.md)** - Detailed changelog and feature documentation

## 🔒 Security

- Credentials never stored or hardcoded
- Passwords hidden during input
- API keys stored in `.env` file (not committed to version control)
- Connections properly closed after use
- No sensitive data logged

## 🌟 Features Comparison

| Feature | SQL Mode | Natural Language Mode |
|---------|----------|----------------------|
| Availability | Always | Requires API key |
| Internet | Not required | Required |
| Setup | Simple | Requires Groq API key |
| Speed | Instant | Depends on API |
| Flexibility | Full SQL control | Natural language |

## 💡 Tips

1. **Start with SQL Mode** - Always available, fast, and flexible
2. **Use Natural Language for Exploration** - Great for discovering database structure
3. **Switch Between Modes** - Use `switch` command to change modes anytime
4. **Review Generated SQL** - Natural Language mode shows the generated SQL
5. **Use Specific Queries** - More specific questions = better SQL generation

## 🤝 Support

For issues or questions:
1. Check [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed instructions
2. Review error messages carefully
3. Verify all dependencies are installed
4. Check database and API connectivity

## 📝 License

This project is provided as-is for educational and personal use.

---

**Both features are fully functional and ready to use!** 🚀
