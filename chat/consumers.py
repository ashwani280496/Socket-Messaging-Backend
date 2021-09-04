import json
import uuid

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer

from chat.models import Message, ChatGroup, MessagesGroups


class TicTacToeConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = 'room_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'MOVE':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                "event": "MOVE"
            })

        if event == 'START':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                'event': "START"
            })

        if event == 'END':
            # Send message to room group
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                'event': "END"
            })
        if event == 'CHAT':
            # Send message to room group
            model = Message(message=message, send_by=response.get("send_by", None))
            model.save()
            group = ChatGroup.objects.filter(id=int(self.room_name))[0]
            MessagesGroups(message=model, group=group).save()
            mymessage = {}
            mymessage['id'] = response.get("id", None)
            mymessage['message'] = message
            mymessage['send_by'] = 1
            mymessage['event'] = "CHAT"
            mymessage['group_id'] = int(self.room_name)
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': mymessage,
                'event': "CHAT"
            })

    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))
# /Users/nestap/Downloads/Django-channels-Tic-Tac-Toe-main/chat/admin.py