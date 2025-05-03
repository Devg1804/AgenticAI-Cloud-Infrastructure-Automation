import sqlite3
from datetime import datetime

def log_request(user_input, intent_data, result):
    """
    Log the user request, parsed intent, and execution result to the database.
    """
    conn = sqlite3.connect('cloud_operations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                 (timestamp TEXT, user_input TEXT, intent TEXT, result TEXT)''')

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    intent = str(intent_data)
    c.execute("INSERT INTO logs (timestamp, user_input, intent, result) VALUES (?, ?, ?, ?)", 
              (timestamp, user_input, intent, str(result)))
    conn.commit()
    conn.close()
