from customers.models import User
from customers.serializers import UserSerializer
from rest_framework import viewsets


# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer