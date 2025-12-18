from rest_framework.generics import CreateAPIView
from ..permissions import IsAdmin
from ..models import User
from ..serializers import RegisterSerializer

class RegisterCreateAPIView(CreateAPIView):
     queryset = User.objects.all()
     serializer_class = RegisterSerializer
     permission_classes = [IsAdmin]