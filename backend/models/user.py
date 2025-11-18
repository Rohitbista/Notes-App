from pydantic import BaseModel, EmailStr

class User(BaseModel):
    """Model for user registration and login"""
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    """Model for user data in database"""
    id: int
    email: str
    hashed_password: str

class Token(BaseModel):
    """Model for JWT token response"""
    access_token: str
    token_type: str

class TokenData(BaseModel):
    """Model for token payload data"""
    email: str | None = None
