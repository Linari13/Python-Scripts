from models.item import ItemModel
from tests.base_test import BaseTest
from app import app

class ItemTest(BaseTest):
    def test_crud(self):
        with app.app_context():
            item = ItemModel('piano', 139.713)

            self.assertIsNone(ItemModel.find_by_name('piano'), f'Found an item {item.name}, but expected not to.')

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('piano'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('piano'))

