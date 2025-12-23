from fastapi import FastAPI
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
        response=signInUser(item.Email,item.Password)
        return {
            "status":True,
            "statusCode":200,
            "message":"User can able to login",
            "data":response
        }
    except Exception as e :
        print("Error in the signIn:Main",str(e))
        return {
            "status":False,
            "statusCode":400,
            "message":str(e),
            "data":{}
        }

@app.post('/user/signup')
def signup(item:SignUp):
    try:
        response=signUpUser(item.Username,item.Password,item.Fname,item.Lname,item.FullName,item.Email,item.Phone)
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
def update(Data: Update):
    try:
        print(len(Data.Newfname))
        response=update_user_data(Data.Email,Data.Newfname,Data.Newlname,Data.NewPhone,Data.Choice)
        return {
            "status":True,
            "statusCode":200,
            "message":"User can update details",
            "data":response
        }
    except Exception as e :
        print("Error in the update:Main",str(e))
        return {
            "status":False,
            "statusCode":400,
            "message":str(e),
            "data":{}
        }

@app.post('/user/delete')
def delete(request:Delete):
    try:
        response= deleteUserAccount(request.Email, request.DeleteChoice)
        return {
            "status":True,
            "statusCode":200,
            "message":"User can delete",
            "data":response
        }
    except Exception as e :
        print("Error in the delete:Main",str(e))
        return {
            "status":False,
            "statusCode":400,
            "message":str(e),
            "data":{}
        }
