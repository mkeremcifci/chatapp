from pydantic import BaseModel

class loginRequest(BaseModel):
    username : str
    password : str
    