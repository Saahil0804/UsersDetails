from database import SessionLocal
from ormodel import UserDetails
from datetime import datetime
# Function to allow user to soft delete or hard delete their account
def deleteUserAccount(email_id, delete_choice):
    try:
        db= SessionLocal()
        if db is None:
            return "Failed to connect to the database."
        user = user = (
            db.query(UserDetails)
            .filter(
                UserDetails.email_id == email_id
            )
            .first()
        )    
        if not user:
            return "Authentication failed. Please check your email and try again."   
        else:
            print("Authentication successful. You can now delete your account.")
            if delete_choice == 1:
                user.is_active= False
                user.updated_at= datetime.now()
                user.updated_by= user.fullname
                db.commit()
                return "Your account has been soft deleted."
            if delete_choice == 2:
                db.delete(user)
                db.commit()
                return "Your account has been hard deleted."
            else:
               return "Invalid choice. Please enter 1 or 2."
    except Exception as e:
        db.rollback()
        raise e

    finally:
        db.close()