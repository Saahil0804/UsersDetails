from pydantic import BaseModel, Field, EmailStr

class SignIn(BaseModel):
    Email: EmailStr
    Password: str

class SignUp(BaseModel):
    Username: str = Field(..., min_length=6 , max_length=20)
    Password: str = Field (..., min_length =8)
    Fname: str = Field (..., min_length =4)
    Lname: str = Field (..., min_length =4)
    Email: EmailStr
    Phone: str 

class Update(BaseModel):
    Choice: int
    Newfname: str =Field(..., min_length=3)
    Newlname: str =Field(...,min_length=3)
    NewPhone: str = Field(...,min_length=10)
    

class Delete(BaseModel):
    DeleteChoice: int    
    