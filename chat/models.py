from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class ChatGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30)

    def __str__(self):
        return self.group_name


class ChatGroupMembers(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    chatGroup = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.member.name + " in " + self.chatGroup.group_name


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=500)
    send_by = models.IntegerField()

    def __str__(self):
        return self.message


# Holds messages in corresponding Group
class MessagesGroups(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.message.message + " in " + self.group.group_name
