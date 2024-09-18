import json
from datetime import datetime
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

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        message_object = Message.objects.create(
            text=message,
            author=self.scope['user'],
            date=datetime.now(),
            room=Room.objects.get(pk=int(self.room_id)),

        )
        async_to_sync(self.channel_layer.group_send)(
            self.room_id,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))