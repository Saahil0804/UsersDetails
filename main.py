from fastapi import FastAPI, HTTPException, Header
from model import *
from SignIn.signIn import signInUser
from SignUp.signup import signUpUser
from Update.update import *
from Update.updatehelper import *
from Delete.delete import *
app= FastAPI()

@app.get('/user/signIn')
def signIn(item:SignIn):
    try :
        response = signInUser(item.Email, item.Password)

        if "error" in response:
            raise HTTPException(
                status_code=401,
                detail=response["error"]
            )

        return {
            "status": True,
            "statusCode": 200,
            "message": "Login successful",
            "data": response
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        print("Error in signIn:Main", str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@app.post('/user/signup')
def signup(item:SignUp):
    try:
        response=signUpUser(item.Username,item.Password,item.Fname,item.Lname,item.Email,item.Phone)
        return {
            "status":True,
            "statusCode":201,
            "message":"User can sign up",
            "data": response
        }
    except Exception as e:
        print("Error in signup:Main",str(e))
        return {
            "status":False,
            "statusCode":400,
            "message":str(e),
            "data":{}
        }
    
@app.post('/user/update')
def update(Data: Update, Authorization: str= Header(...)):
    try:
        # 🔐 Extract token from header
        token = Authorization.split(" ")[1]

        response = update_user_data(
            token,
            Data.Newfname,
            Data.Newlname,
            Data.NewPhone,
            Data.Choice
        )

        return {
            "status": True,
            "statusCode": 200,
            "message": "User details updated successfully",
            "data": response
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        print("Error in update:Main", str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

@app.post('/user/delete')
def delete(request:Delete, Authorization: str= Header(...)):
    try:
        token= Authorization.split(" ")[1]
        response= deleteUserAccount(token, request.DeleteChoice)
        return {
            "status":True,
            "statusCode":200,
            "message":"User can delete",
            "data":response
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        print("Error in delete:Main", str(e))
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )