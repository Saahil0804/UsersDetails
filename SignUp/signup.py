from ormodel import UserDetails
from SignUp.signuphelper import *
from datetime import datetime
from database import SessionLocal

# Function to sign up a new user
def signUpUser(Username, Pword,f_name,l_name, email_id, phone_no):
    try: 
        FullName = validationForFName(f_name, l_name)
        if not FullName:
            return "Entered full name is not valid. Please try again."
            
        Validphone = validationForPhone(phone_no)
        if not Validphone:
            return "Entered phone number is not valid. Please try again."

        result = insert_user_data(Username, Pword, FullName, email_id, phone_no)
        return result
    except ValueError:
        return "Invalid input. Please enter the correct data types."
    except Exception as e:
        return f"An error occurred: {e}"

# Function to check if the email already exists
def check_existing_email(email_id):
    try:
        db= SessionLocal()
        if db is not None:
            existing_user = (
            db.query(UserDetails)
            .filter(
                UserDetails.email_id == email_id,
                UserDetails.is_active == True
            )
            .first()
        )
            if existing_user:
                return "User is already registered with this email."    
            else:
                print("Email is available for registration.")        
            return True
    except Exception as e:
            return f"Error checking existing email: {e}"
    finally:
            db.close()
                
# Function to insert user data into the database
def insert_user_data(Username, Pword, FullName, email_id, phone_no):
    try:
        db= SessionLocal()
        if db is None:
            raise "Error in database connection."
        isUserExist = check_existing_email(email_id)
        if not isUserExist:
                return "User already exists with this email."
        new_user = UserDetails(
                username=Username,
                pword=Pword, 
                fullname=FullName,
                email_id=email_id,
                phone_no=phone_no,
                created_by=FullName,
                updated_by=FullName
            )            
        db.add(new_user)           
        db.commit()
        return "User signed up successfully"

    except Exception as e:
            db.rollback()
            raise e

    finally:
            db.close()
