from Update.updatehelper import  validationForNewFname
from ormodel import UserDetails
from datetime import datetime
from database import SessionLocal

def update_user_data(email_id, fname, lname, phone_update, choice):
    db = SessionLocal()
    try:
        user = (
            db.query(UserDetails)
            .filter(
                UserDetails.email_id == email_id,
                UserDetails.is_active == True
            )
            .first()
        )

        if not user:
            return "User does not exist"

        if choice not in (1, 2, 3):
            return "Invalid choice"
        
        if choice == 1 and phone_update:
            return "Invalid operation: choice 1 allows only name update"

        if choice == 2 and (fname or lname):
            return "Invalid operation: choice 2 allows only phone update"

        if choice == 3 and not (fname or lname or phone_update):
            return "Invalid operation: nothing to update"
        
        if choice ==1:
            full_name = validationForNewFname(fname, lname)
            if not full_name:
                return "Invalid name"
            user.fullname = full_name

        if choice ==2:
            user.phone_no = phone_update


        if choice == 3:
            full_name = validationForNewFname(fname, lname)
            if not full_name:
                return "Invalid name"

            if not phone_update:
                return "Invalid phone number"

            user.fullname = full_name
            user.phone_no = phone_update

        user.updated_at = datetime.now()
        user.updated_by = user.fullname or "Admin"

        db.commit()
        return "User details updated successfully"

    except Exception as e:
        db.rollback()
        raise e


    finally:
        db.close()
