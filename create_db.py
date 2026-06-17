from database.db import engine
from database.auth import Base

Base.metadata.create_all(
    bind=engine
)

print("Database Created")