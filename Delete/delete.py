from auth import verify_access_token
from database import SessionLocal
from ormodel import UserDetails
from datetime import datetime
# Function to allow user to soft delete or hard delete their account
def deleteUserAccount(token, delete_choice):
    db = SessionLocal()
    try:
        # 🔐 Get email from JWT
        email_id = verify_access_token(token)

        user = (
            db.query(UserDetails)
            .filter(UserDetails.email_id == email_id)
            .first()
        )

        if not user:
            return "User not found"

        if delete_choice == 1:
            user.is_active = False
            user.updated_at = datetime.now()
            user.updated_by = email_id
            db.commit()
            return "Your account has been soft deleted."

        elif delete_choice == 2:
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