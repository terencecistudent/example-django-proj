from django.test import TestCase
from .forms import LoginForm, RegisterForm


class TestAccountsForm(TestCase):
    def test_correct_message_for_missing_name(self):
        form = LoginForm({"username": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["username"], [u"This field is required."])


class TestAccountsView(TestCase):
    """
    Tests Book view
    """
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
