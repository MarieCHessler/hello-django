from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):
    """ Test all functions in form """

    def test_item_name_is_required(self):
        """ Test that name field is required """
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], "This field is required.")

    def test_done_field_is_not_required(self):
        """ Test that done field is not required """
        form = ItemForm({'name': 'Test to-do item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        """
        Test that only fields stated in inner metaclass
        on the item form are shown
        """
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
