import re

from django.core.exceptions import ValidationError

def validate_email(email):
    
    REGEX_EMAIL = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
    
    if not re.match(REGEX_EMAIL,email) :
        raise ValidationError(message='INVALID_EMAIL')
  
def validate_password(password):
    
    REGEX_PASSWORD = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    
    if not re.match(REGEX_PASSWORD,password):
        raise ValidationError(message = "INVALID_PASSWORD")

def validate_nickname(nickname):
    
    REGEX_NICKNAME = '^[a-zA-Z가-힣]+$'
    
    if not re.match(REGEX_NICKNAME,nickname):
        raise ValidationError(message = "INVALID_NICKNAM")
  