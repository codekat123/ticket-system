from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



class LogoutAPIView(APIView):

     def post(self,request):
          refresh = request.data.get('refresh')
          
          if not refresh:
               Response(
                    {
                         'error':'Refresh Token required'
                    },
                    status=status.HTTP_200_OK
               )
          
          try:
               token = RefreshToken(refresh)
               token.blacklist()
               return Response(
                    {
                         'message':'Logged out successfully'
                    },
                    status=status.HTTP_200_OK,
               )
          except Exception as e:
               return Response({'error':e},status=status.HTTP_400_BAD_REQUEST)