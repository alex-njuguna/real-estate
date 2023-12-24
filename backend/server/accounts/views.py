from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

User = get_user_model()

class SignUp(APIView):
    """alllows for creation of a new user"""
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        """a function to post or send in a new user"""
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password != password2:
            return Response({'error': 'Passwords must be similar!'})
        else:
            if len(password) < 7:
                return Response({'error': 'Password must at least be characters long'})
            else:
                user = User.create_user(email=email, name=name, password=password)

                user.save()
                
                return Response({'success': 'Account created successfully!'})
