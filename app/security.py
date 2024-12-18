from jose import jwt ,JWTError
from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated = "auto")

SECRET_KEY = "key"
ALGORITHM = "HS256"

def verifyPassword(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)


def createAccessToken(id:int):
    toEncode = {"sub":str(id)}
    encodeJWT = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodeJWT

def decodeAccessToken(token : str):
    return jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
     

