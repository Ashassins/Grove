from django.http import HttpResponse, HttpRequest, Http404
from django.db.models import Q
from rest_framework.decorators import api_view
from users.models import User
from groves.models import Grove
from notifications.models import Notification

@api_view(["POST"])
def shake_friend(request):
    src = User.objects.filter(username=request.user).first()
    print(request.data)
    if (dst_name := request.data["dst"]) is None:
        return Http404
    dst = User.objects.filter(username=dst_name).first()
    if (friendship := Grove.objects.filter(Q(user_a=src, user_b=dst) | Q(user_a=dst, user_b=src)).first()) is None:
        return Http404
    friendship.xp += 50
    friendship.save()
    n = Notification(user_to=dst, content="What's shaking?", src=str(src))
    n.save()
    return HttpResponse(f"Created shake to {dst}")