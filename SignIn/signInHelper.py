import os
import psycopg2
from dotenv import load_dotenv
load_dotenv() 

# Function to connect to the database
def dbConnection():
    try:
        connection = psycopg2.connect(
            host=os.getenv("HOSTNAME"),
            user=os.getenv("USER_NAME"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
            port=os.getenv("PORT")
        )
        print("Database connected successfully")
        return connection
    except Exception as e:
        print("Error in the dbConnection:signIn.signInHelper",str(e))
        return None  