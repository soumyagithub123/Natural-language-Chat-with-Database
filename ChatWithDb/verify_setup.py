#!/usr/bin/env python3
"""
Quick verification script to check if all dependencies are installed correctly.
"""

import sys

def check_dependency(module_name, package_name=None):
    """Check if a Python module is installed."""
    if package_name is None:
        package_name = module_name
    
    try:
        __import__(module_name)
        print(f"✓ {package_name} is installed")
        return True
    except ImportError:
        print(f"✗ {package_name} is NOT installed")
        return False

def main():
    print("=" * 60)
    print("ChatWithDB - Dependency Verification")
    print("=" * 60)
    print()
    
    # Check required dependencies
    print("Required Dependencies:")
    print("-" * 60)
    mysql_ok = check_dependency("mysql.connector", "mysql-connector-python")
    print()
    
    # Check optional dependencies
    print("Optional Dependencies (for Natural Language feature):")
    print("-" * 60)
    groq_ok = check_dependency("groq", "groq")
    dotenv_ok = check_dependency("dotenv", "python-dotenv")
    print()
    
    # Summary
    print("=" * 60)
    print("Summary:")
    print("=" * 60)
    
    if mysql_ok:
        print("✓ SQL Mode: Ready to use")
    else:
        print("✗ SQL Mode: NOT ready - Install: pip install mysql-connector-python")
    
    if groq_ok and dotenv_ok:
        print("✓ Natural Language Mode: Ready to use (if API key is set)")
    else:
        print("✗ Natural Language Mode: NOT ready")
        if not groq_ok:
            print("  - Install: pip install groq")
        if not dotenv_ok:
            print("  - Install: pip install python-dotenv")
    
    print()
    print("=" * 60)
    
    # Check .env file
    from pathlib import Path
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        print("✓ .env file exists")
        try:
            with open(env_path, 'r') as f:
                content = f.read()
                if 'GROQ_API_KEY' in content:
                    print("✓ GROQ_API_KEY found in .env file")
                else:
                    print("⚠ .env file exists but GROQ_API_KEY not found")
        except Exception as e:
            print(f"⚠ Error reading .env file: {e}")
    else:
        print("⚠ .env file not found (optional for Natural Language mode)")
    
    print("=" * 60)
    print()
    
    if mysql_ok:
        print("✅ Your setup is ready for SQL Mode!")
        if groq_ok and dotenv_ok:
            print("✅ Your setup is ready for Natural Language Mode!")
            print("   (Make sure to set GROQ_API_KEY in .env file)")
        else:
            print("⚠️  To enable Natural Language Mode:")
            print("   1. Install: pip install groq python-dotenv")
            print("   2. Create .env file with: GROQ_API_KEY=your-api-key")
    else:
        print("❌ Please install required dependencies:")
        print("   pip install -r requirements.txt")
        sys.exit(1)

if __name__ == "__main__":
    main()


