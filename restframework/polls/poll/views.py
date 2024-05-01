from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404

from .models import (Poll, Choice, Vote)
from .serializers import (PollsSerializer, ChoiceSerializer, VoteSerializer)


class PollList(APIView):
    MAX_OBJECTS = 20
    def get(self, request):
        polls = Poll.objects.all()[:self.MAX_OBJECTS]
        data = PollsSerializer(polls, many=True).data
        return Response(data)


class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, id=pk)
        data = PollsSerializer(poll).data
        return Response(data)


