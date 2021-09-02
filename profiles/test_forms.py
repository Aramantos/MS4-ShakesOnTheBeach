from django.test import TestCase
from .forms import UserProfileForm

# Create your tests here.


class TestUserProfiles(TestCase):

    def test_create_user_profile_with_required_fields_filled(self):
        form = UserProfileForm({
            'full_name': 'Bill Shister',
            'default_phone_number': '0858585851',
            'default_postcode': '858585',
            'default_town_or_city': 'Imaginopolis',
            'default_street_address1': '123 Fake Street',
            'default_street_address2': 'Con Artist Street',
            'default_county': 'Narnia',
            })
        self.assertTrue(form.is_valid())
