from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):
    
    def test_get_todo_list(self):
        respose  = self.client.get('/')
        self.assertEqual(respose, status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        respose  = self.client.get('/add')
        self.assertEqual(respose, status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        respose  = self.client.get(f'/edit/{item.id}')
        self.assertEqual(respose, status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

