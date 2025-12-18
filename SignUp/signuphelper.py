import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

# Validating username
def validationForUsername(Username):
    try : 
        Username = str(Username).strip()
        if len(Username) < 6 or len(Username) > 20 or not Username.isalnum():
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating password
def validationForPassword(Pword):
    try :   
        Pword = str(Pword).strip()
        if len(Pword) < 8:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating email
def validationForEmail(email_id):
    try : 
        email_id = str(email_id).strip()
        if "@" not in email_id or ".com" not in email_id:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating phone number
def validationForPhone(phone_no):
    try :
        phone_no = str(phone_no).strip()
        if len(str(phone_no)) != 10:
            return False
        else:
            return True
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
        return False

# Validating full name
def validationForFName (fname, lname):
    try :
        FullName = fname + " " + lname   
        FullName = str(FullName).strip()
        if len(FullName) < 3:
            return False
        else:
            return FullName
    except Exception as e:
        print(f"An error occurred during username validation: {e}")
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