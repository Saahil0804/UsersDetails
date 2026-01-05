from ormodel import UserDetails
from database import SessionLocal
from auth import create_access_token
from security import verify_password

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
                UserDetails.is_active == True
            )
            .first()
        )
        if not user or not verify_password(Pword, user.pword):
            return {"error": "Invalid email or password"}

        # 🔐 Create JWT Token
        access_token = create_access_token(
            data={
                "sub": user.email_id,
                "user_id": user.sno
            }
        )
        return {
                    "access_token": access_token,
            "token_type": "bearer",
            "user": {
                 "user_id":user.sno,
                 "username":user.username,
                 "fname":user.fullname,
                 "mail":user.email_id,
                 "phone":user.phone_no,
            }
            }
      
    except Exception as e:
            print("Error in the signInUser:SignIn.signIn",str(e))
            raise e
    finally:
            db.close()