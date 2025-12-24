from ormodel import UserDetails
from database import SessionLocal

# Function to sign in an existing user
def signInUser(email_id, Pword):
    try:
        db = SessionLocal()
        if db is None:
            raise Exception ("Error in database connection")
        user =  (
            db.query(UserDetails)
            .filter(
                UserDetails.email_id == email_id,
                UserDetails.pword == Pword,
                UserDetails.is_active == True
            )
            .first()
        )
        if user:
            return {
                 "user_id":user.sno,
                 "username":user.username,
                 "password":user.pword,
                 "fname":user.fullname,
                 "mail":user.email_id,
                 "phone":user.phone_no,
            }
        else:
            return "Invalid email or password."
    except Exception as e:
            print("Error in the signInUser:SignIn.signIn",str(e))
            raise e
    finally:
            db.close()