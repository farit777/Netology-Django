from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product, Review

class ProductTests(APITestCase):
    def setUp(self):
        self.product1 = Product.objects.create(title="Samsung Galaxy S23", description="Latest Samsung phone", price=70000)
        self.product2 = Product.objects.create(title="Apple IPhone 15", description="Latest Apple phone", price=100000)
        Review.objects.create(product=self.product1, text="Great phone!", mark=5)
        Review.objects.create(product=self.product1, text="Too expensive.", mark=3)
        Review.objects.create(product=self.product2, text="Best iPhone ever!", mark=5)

    def test_products_list(self):
        response = self.client.get(reverse('products-list'))  # убедитесь, что вы добавили имя для этого URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Samsung Galaxy S23")
        self.assertEqual(response.data[1]['title'], "Apple IPhone 15")

    def test_product_details(self):
        response = self.client.get(reverse('product-detail', args=[self.product1.id]))  # убедитесь, что вы добавили имя для этого URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Samsung Galaxy S23")
        self.assertEqual(len(response.data['reviews']), 2)
