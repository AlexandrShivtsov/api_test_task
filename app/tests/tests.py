from rest_framework.test import APIClient
import pytest


client = APIClient()

URL_TEAM =  '/api/teams/'
URL_TEAMMATE =  '/api/teammates/'
    
#testing /api/teams/
@pytest.mark.django_db
def test_get_teams(client):
    responce = client.get(URL_TEAM)
    assert responce.status_code == 200


@pytest.mark.django_db
def test_post_teams(client):
    data = {
    "team_name": "test_team" 
    }
    responce = client.post(URL_TEAM, data=data)
    assert responce.status_code == 201
  
  
#testing /api/teammates/
@pytest.mark.django_db
def test_get_teammates(client):
    responce = client.get(URL_TEAMMATE)
    assert responce.status_code == 200
    
    
@pytest.mark.django_db
def test_post_teammates(client):
    data = {
    "teammate_name": "test_name1",
    "teammate_surname": "test_surname1",
    "teammate_email": "test@test1.com",
    "team": "team4"
    }
    responce = client.post(URL_TEAMMATE, data=data)
    assert responce.status_code == 201
