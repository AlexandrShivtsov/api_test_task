from rest_framework import serializers

from . models import Teams, Teammates


class TeamsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teams
        fields = (
            'team_name',
            'created',
        )


class TeammatesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Teammates
        fields = (
            'teammate_name',
            'teammate_surname',
            'teammate_email',
            'team',
            'created',
        )