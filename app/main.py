from flask import Flask
import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.environ.get("DB_PASSWORD")

app = Flask(__name__)

@app.route('/') 
def index(): 
    conn =  psycopg2.connect(database="postgres",
                            user="postgres",
                            password=DB_PASSWORD,
                            host="host.docker.internal",
                            port="5432")
  
    cur = conn.cursor() 
  
    cur.execute('''SELECT * FROM employee''') 
  
    data = cur.fetchall() 
    print(data)

    cur.close() 
    conn.close() 
  
    return str(data)

if __name__ == "__main__":
     app.run(host ='0.0.0.0', port = 5001, debug = True) 