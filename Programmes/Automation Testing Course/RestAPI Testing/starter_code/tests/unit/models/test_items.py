from unittest import TestCase
from models.item import ItemModel

class ItemTest(TestCase):

    def test_create_item(self):
        item = ItemModel('piano', 139.713)

        self.assertEqual(item.name,'piano',
                         '*** item name doesn\'t match constructor argument after creation ***')
        self.assertEqual(item.price,139.713,
                         '*** item price doesn\'t match constructor argument after creation ***')

    def test_item_json(self):
        item = ItemModel('piano', 139.713)
        expected = {
            'name': 'piano',
            'price': 139.713
        }

        self.assertEqual(expected, item.json(),
                         '\n***'
                         '\nThe JSON export of the item is incorrect.'
                         f'\nReceived {item.json()},\nExpected {expected}'
                         '\n***'
                         )
