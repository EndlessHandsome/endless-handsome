from django.contrib.auth.models import User
from account.serializer import LoginSerializer


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken

class RegisterView(APIView):
	def check_request_data_complete(self, data):
		"""判断用户入参是否完整"""
		return all([
			data.get('username', False),
			data.get('password', False)
		])

	def get(self, request, *args, **kwargs):
		return Response({'detail': '请勿用GET方法'},  status=status.HTTP_400_BAD_REQUEST)

	def post(self, request, *args, **kwargs):
		data_complete = self.check_request_data_complete(request.data)
		if not data_complete:
			return Response({'detail': '参数错误'},  status=status.HTTP_400_BAD_REQUEST)
		username = request.data.get('username').strip()
		if len(username) > 30:
			return Response({'detail': '用户名过长'},  status=status.HTTP_400_BAD_REQUEST)
		if username is None:
			return Response({'detail': '用户名格式不正确'},  status=status.HTTP_400_BAD_REQUEST)
		ret = User.objects.filter(username=username)
		if ret.exists():
			return Response({'detail': '用户名已经存在'},  status=status.HTTP_403_FORBIDDEN)
			
		user = User.objects.create(username=username,email='')
		user.set_password(request.data.get('password'))
		user.save()
		return Response({'detail': '创建用户成功'},  status=status.HTTP_201_CREATED)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token})

    def delete(self, request):
        logout(request)
        return Response({'detail': 'logout successful.'})