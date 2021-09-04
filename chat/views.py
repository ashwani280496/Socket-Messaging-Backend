from django.shortcuts import render, redirect
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from chat.models import *


def index(request):
    if request.method == "POST":
        room_code = request.POST.get("room_code")
        char_choice = request.POST.get("character_choice")
        return redirect(
            '/play/%s?&choice=%s'
            % (room_code, char_choice)
        )
    return render(request, "index.html", {})


def game(request, room_code):
    choice = request.GET.get("choice")
    if choice not in ['X', 'O']:
        raise Http404("Choice does not exists")
    context = {
        "char_choice": choice,
        "room_code": room_code
    }
    return render(request, "game.html", context)


class ChatGroupViewsSet(viewsets.GenericViewSet, viewsets.generics.ListAPIView, viewsets.generics.ListCreateAPIView):
    serializer_class = ChatGroup
    queryset = ChatGroup.objects.all()
    model = ChatGroup

    def list(self, request, *args, **kwargs):
        result = ChatGroupMembers.objects.all()
        data = {}
        for a in result:
            if a.chatGroup.group_name not in data:
                data[a.chatGroup.group_name] = []
            member = {
                "id": a.member.id,
                "name": a.member.name
            }
            data[a.chatGroup.group_name].append(member)
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        mId = int(data.get('member_id', None))
        gId = int(data.get('group_id', None))

        member = Member.objects.filter(id=mId)[0]
        group = ChatGroup.objects.filter(id=gId)[0]
        model = ChatGroupMembers(member=member, chatGroup=group)
        model.save()
        data = {}
        return Response(data, status=status.HTTP_200_OK)


class MembersViewSet(viewsets.GenericViewSet, viewsets.generics.ListAPIView):
    serializer_class = Member
    queryset = Member.objects.all()
    model = Member

    def list(self, request, *args, **kwargs):
        results = Member.objects.all()
        data = []
        for member in results:
            chatGroups = ChatGroupMembers.objects.filter(member=member)
            chatGroupsData = []
            for chatGroup in chatGroups:
                chatGroupsData.append({
                    "name": chatGroup.chatGroup.group_name,
                    "id": chatGroup.chatGroup.id
                })

            data.append({
                "name": member.name,
                "id": member.id,
                "associated_groups": chatGroupsData
            })

        return Response(data, status=status.HTTP_200_OK)
