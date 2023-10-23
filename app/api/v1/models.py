from django.db import models


class Teams(models.Model):
    team_name = models.CharField('Teame',max_length=100, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.team_name
        
        
class Teammates(models.Model):
    teammate_name = models.CharField('Name',max_length=50, null=False)
    teammate_surname = models.CharField('Surname',max_length=50, null=False)
    teammate_email = models.EmailField('Email',max_length=80, null=False, unique=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, db_column='team_name')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.teammate_name} {self.teammate_surname}'
