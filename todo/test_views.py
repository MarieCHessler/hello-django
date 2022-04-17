from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    """
    Test the http responses of the different views,
    to see that they are working
    """

    def test_get_todo_list(self):
        """ Test that you get the to-do list view """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        """ Test that you get the add item page view """
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        """ Test that you get the edit item page view """
        item = Item.objects.create(name='Test to-do item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        """ Test that you can add an item """
        response = self.client.post('/add', {'name': 'Test added item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        """ Test that you can delete an item """
        item = Item.objects.create(name='Test to-do item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        """ Test that you can toggle an item """
        item = Item.objects.create(name='Test to-do item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

    def test_can_edit_item(self):
        """ Test that you can edit an item """
        item = Item.objects.create(name='Test to-do item')
        response = self.client.post(f'/edit/{item.id}', {'name': 'Updated name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated name')
