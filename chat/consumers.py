import json
from datetime import datetime
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
import base64
from .models import Message, Room, File
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

        if text_data_json['action'] == 'send':
            message = text_data_json['message']
            author = text_data_json['username']
            date_time = text_data_json['datetime']
            userid = text_data_json['user_id']
            profile_picture = text_data_json['profile_picture']
            file = text_data_json['file']
            file_url = None
            file_name = None
            file_type = None
            if file:
                file_name, file, file_type = file['name'], file['bytes'].split(',')[1], file['type'].split('/')[0]
                file_name = file_name.split('/')[-1]
                file_name = file_name.split(';')[0]
                file = base64.b64decode(file)
                file = ContentFile(file, name=file_name)
                message_id = Message.objects.create(
                    text=message,
                    author=self.scope['user'],
                    date=date_time,
                    room=Room.objects.get(pk=int(self.room_id)),
                    file=File.objects.create(
                        file=file,
                        file_name=file_name,
                        file_type=file_type,
                    ),
                ).id
                file_url = Message.objects.get(pk=message_id).file.file.url
            else:
                message_id = Message.objects.create(
                    text=message,
                    author=self.scope['user'],
                    date=date_time,
                    room=Room.objects.get(pk=int(self.room_id)),
                ).id

            async_to_sync(self.channel_layer.group_send)(
                self.room_id,
                {
                    'type': 'send_message',
                    'message': message,
                    'author': author,
                    'profile_picture': profile_picture,
                    'userid': userid,
                    'message_id': message_id,
                    'file': file_url,
                    'file_name': file_name,
                    'file_type': file_type,
                }
            )
        if text_data_json['action'] == 'delete':
            message_id = text_data_json['message']
            message = Message.objects.get(id=message_id)
            if message.author == self.scope['user']:
                message.delete()
                async_to_sync(self.channel_layer.group_send)(
                    self.room_id,
                    {
                        'type': 'delete_message',
                        'message': message_id,
                    }
                )


    def send_message(self, event):
        self.send(text_data=json.dumps({
            'type': 'send',
            'message': event['message'],
            'author': event['author'],
            'profile_picture': event['profile_picture'],
            'userid': event['userid'],
            'message_id': event['message_id'],
            'file': event['file'],
            'file_name': event['file_name'],
            'file_type': event['file_type'],
        }))


    def delete_message(self, event):
        self.send(text_data=json.dumps({
            'type': 'delete',
            'message': event['message'],
        }))