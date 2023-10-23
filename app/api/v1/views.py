from django.shortcuts import render

from rest_framework import viewsets

from . serializers import TeamsSerializer, TeammatesSerializer
from . models import Teams, Teammates
from . paginators import TeammatesPaginations, TeamsPaginations


class TeamsApiView(viewsets.ModelViewSet):
    """Handling teams API point"""
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer
    pagination_class = TeamsPaginations


class TeammatesApiView(viewsets.ModelViewSet):
    """Handling teammates API point"""
    queryset = Teammates.objects.all()
    serializer_class = TeammatesSerializer
    pagination_class = TeammatesPaginations
