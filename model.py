from pydantic import BaseModel

class SignIn(BaseModel):
    Email: str
    Password: str

class SignUp(BaseModel):
    Username: str
    Password: str
    Fname: str
    Lname: str
    FullName: str
    Email: str
    Phone: str

    
    