from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class UserDetails(Base):
    __tablename__ = "userdetails"   
    sno = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    pword = Column(String(100))

    fullname = Column(String(50))
    email_id = Column(String(50))
    phone_no = Column(String(20))

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    created_by = Column(String(50), default="ADMIN")
    updated_by = Column(String(50), default="ADMIN")
