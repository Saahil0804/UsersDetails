import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Validating new full name
def validationForNewFname (newfname, newlname):
    try :
        NewFullName = newfname + " " + newlname   
        NewFullName = str(NewFullName).strip()
        if len(NewFullName) < 3:
            print("Entered name is not valid. Please try again.")
            return False
        else:
            print("Full name validated successfully.")
            print(NewFullName,"NewFullName")
            return NewFullName
    except Exception as e:
        print(f"An error occurred during full name validation: {e}")
        return False
    
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
        print(f"Error connecting to database: {e}")
        return None