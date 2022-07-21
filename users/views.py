from django.shortcuts import render

# Create your views here.
import json

import bcrypt
import jwt
from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError 

from core.utils     import login_decorator
from core.validator import validate_email,validate_password,validate_nickname
from delicious_in_seoul.settings import SECRET_KEY,ALGORITHM
from users.models   import User

class SignupView(View): 
    def post(self,request):
        try:
            data         = json.loads(request.body)   
            email        = data['email'] 
            nickname    = data['nickname'] 
            password     = data['password']
            category_id  = data['category_id']
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({"message":"DUPLICATE_EMAIL"}, status = 400)
            
            validate_email(email)
            validate_nickname(nickname)
            validate_password(password)

            
            User.objects.create(
                nickname    = nickname,
                email        = email,
                category_id  = category_id,
                password     = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
            )
            return JsonResponse({"message":"SUCCESS"}, status = 201)
        
        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status = 400)
        except ValidationError as e :
            return JsonResponse({'message' : e.message }, status = 400)

class SigninView(View):
    def post(self,request):
        try: 
            data     = json.loads(request.body)
            email    = data['email']
            password = data['password']
            
            if not User.objects.filter(email = email).exists():
                return JsonResponse({"message":"INVALID_USER"}, status = 401)
            
            user = User.objects.get(email = email)
            
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({"message": "INVALID_USER"}, status = 401)
            
            token  = jwt.encode({'user_id' : user.id}, SECRET_KEY, ALGORITHM)
            
            return JsonResponse({ "nickname" : user.nickname,
                                  "access_token":token},status=200)
        
        except KeyError: 
            return JsonResponse({"message":"KEY_ERROR"},status=400)
        