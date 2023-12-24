from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions


class SignupView(APIView):
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
        elif User.objects.filter(email=email):
            return Response({'error': 'A user with that email exists'})
        else:
            if len(password) < 7:
                return Response({'error': 'Password must at least be 6 characters long'})
            else:
                user = User.objects.create_user(email=email, name=name, password=password)

                user.save()
                
                return Response({'success': 'Account created successfully!'})
