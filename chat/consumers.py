import json
from datetime import datetime

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
# from models import Message

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['chat_id']

        print(self.room_group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # message_object = Message.objects.create(
        #     text=message,
        #     author=self.scope['user'],
        #     date=datetime.datetime.now(),
        #     room=self.room_group_name
        #
        # )
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))