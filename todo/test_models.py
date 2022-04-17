from django.test import TestCase
from .models import Item


class TestModels(TestCase):
    """
    Test that to-do items are created by default with done status of false
    """

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name='Test to-do item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Item.objects.create(name='Test to-do item')
        self.assertEqual(str(item), 'Test to-do item')
