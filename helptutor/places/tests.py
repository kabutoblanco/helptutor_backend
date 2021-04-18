from django.test import RequestFactory, TestCase
from django.urls import reverse
from model_mommy import mommy

from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from helptutor.places.models import Country
from helptutor.places.api import *

# Create your tests here.
class TestApitCountry(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/country/"
        
        Country.objects.create(name="Colombia",cod="30")
    
    def test_get_country(self):

        # process
        response = self.client.get(self.url)
        result = response.json()
        
        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],"Colombia")

    def test_post_country(self):
        
        # definition
        data = {
            "name":"Peru",
            "cod":"30"
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],"Peru")

    def test_put_country(self):
        pk = "1"
        data = {
            "name":"Ecuador"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Ecuador")

class TestApitEstate(APITestCase):

    def setUp(self):

        self.client = APIClient()

        self.url = "/api/state/"
        
        self.state = mommy.make(State)

    def test_get_state(self):

        # process
        response = self.client.get(self.url)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertIsInstance(result,list)
        self.assertEqual(result[0]["name"],self.state.name)

    def test_post_state(self):
        
        # definition
        country = mommy.make(Country)
        print()
        data = {
            "name": "Putumayo",
            "cod": "33",
            "country": country.id
        }

        # process
        response = self.client.post(self.url, data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertEqual(result["name"],"Putumayo")

    def test_put_state(self):
        pk = "1"
        data = {
            "name":"Huila"
        }

        # process
        response = self.client.patch(self.url + f"{pk}/", data=data)
        result = response.json()

        # assert
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(result["name"],"Huila")
