from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):
        form = OrderForm({
            'full_name': 'Tester McTester',
            'email': 'tester1@tester1.com',
            'phone_number': '085 8585851',
            'street_address1': '123 Fake Street',
            'town_or_city': 'Imaginopolis'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['full_name'], [u'This field is required.'])
