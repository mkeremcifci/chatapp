from jose import jwt
from passlib.context import CryptContext

pwdContext = CryptContext(schemes=["bcrypt"], deprecated = "auto")

SECRET_KEY = "key"
ALGORITHM = "HS256"

def verifyPassword(plainPassword, hashedPassword):
    return pwdContext.verify(plainPassword, hashedPassword)


def createAccessToken(username:str):
    toEncode = {"sub":username}
    encodeJWT = jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)
    return encodeJWT
