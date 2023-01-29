from django.http import HttpRequest, Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User
from groves.models import Grove
from users.models import User
from .models import Notification
from .serializers import NotificationSerializer
from django.db.models import Q


@api_view(["GET"])
def get_notifications(request):
    username = request.user
    user = User.objects.filter(username=username).first()
    print(user) 
    notif = Notification.objects.filter(user_to=user)
    print(notif)

    return Response(NotificationSerializer(notif, many=True).data)

