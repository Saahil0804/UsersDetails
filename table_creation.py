from database import engine, Base
from ormodel import UserDetails  

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully")
