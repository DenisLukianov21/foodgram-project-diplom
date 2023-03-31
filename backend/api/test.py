from rest_framework import status
from rest_framework.test import APITestCase
from recipes.models import Tag, Ingredient


class TagApiTest(APITestCase):

    def setUp(self):
        test_tag = Tag.objects.create(
            name='test_tag',
            color='#00ff7f',
            slug='test_slug_tag'
        )
        test_tag.save()

    def test_tags_response_api(self):
        response = self.client.get('http://localhost/api/tags/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{
            'color': '#00ff7f',
            'name': 'test_tag',
            'id': 1,
            'slug': 'test_slug_tag'
        }])


class IngredientApiTest(APITestCase):

    def setUp(self):
        test_ingredient = Ingredient.objects.create(
            name='яйцо',
            measurement_unit='шт',
        )
        test_ingredient.save()

    def test_ingredient_response_api(self):
        response = self.client.get('http://localhost/api/ingredients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), [{
            'measurement_unit': 'шт',
            'name': 'яйцо',
            'id': 1
        }])
