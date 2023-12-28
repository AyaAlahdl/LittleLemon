from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemtr = item.get_item()

        self.assertEqual(itemtr, "IceCream : 80")


class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, menu_item_description="Cold and fresh flavors.")
        self.assertEqual(item, "IceCream : 80")