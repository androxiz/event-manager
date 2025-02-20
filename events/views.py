from django.shortcuts import render

from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event

from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import action
from rest_framework.response import Response


from django.core.mail import send_mail
from django.conf import settings


class EventApi(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]


    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        user = request.user
        event = self.get_object()
        if event.participants.filter(id=user.id).exists():
            return Response({'result': "Already registred"}, status=409)
        
        event.participants.add(user)

        
        subject = f'Registration to {event.title}'
        message = f'Hi, {user.username}!\n\nYou have successfully registered to "{event.title}", which will be on {event.date.strftime("%d.%m.%Y")}.\n\nThanks!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, message, email_from, recipient_list)

        return Response({'result': f'Successfully registred at {event.title}'})
    
