from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()


class SignupView(APIView):
    # Allow for user registration
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # post signup data
        data = self.request.data

        name = data['name']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email is already registered by another user'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password is too short.'})
                else:
                    user = User.objects.create_user(
                        name=name, email=email, password=password)

                    user.save()
                    return Response({'success': 'User created successfully'})

        else:
            return Response({'error': 'Passwords do not match'})
