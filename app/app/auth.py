import jwt
import os
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = os.environ['ALGORITHM']

# def create_access_token(*, data : dict, expires_delta: timedelta = None):
