import json
from datetime import datetime

from django.contrib.auth.decorators import login_required

from .models import Message, Room
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
# from models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):

        self.room_id = self.scope['path'].split('/')[-2]
        async_to_sync(self.channel_layer.group_add)(
            self.room_id,
            self.channel_name
        )

        self.accept()

    def receive(self, text_data, *args):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        author = text_data_json['username']
        datetime = text_data_json['datetime']
        userid = text_data_json['userid']
        profile_picture = text_data_json['profile_picture']

        message_object = Message.objects.create(
            text=message,
            author=self.scope['user'],
            date=datetime,
            room=Room.objects.get(pk=int(self.room_id)),

        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_id,
            {
                'type': 'chat_message',
                'message': message,
                'author': author,
                'profile_picture': profile_picture,
                'userid': userid,
            }
        )

    def chat_message(self, event):
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': event['message'],
            'author': event['author'],
            'profile_picture': event['profile_picture'],
            'userid': event['userid'],
        }))