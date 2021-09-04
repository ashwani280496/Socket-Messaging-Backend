from django.contrib import admin
from chat.models import ChatGroup, Member, ChatGroupMembers


class GroupAdmin(admin.ModelAdmin):
    name = ["Group"]


admin.site.register(ChatGroup, GroupAdmin)
admin.site.register(Member)
admin.site.register(ChatGroupMembers)


