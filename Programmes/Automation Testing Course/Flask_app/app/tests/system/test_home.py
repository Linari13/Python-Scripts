from tests.system.base_test import BaseTest
import json

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c:
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(                           #Flask can't return dictionary, only strings
                json.loads(resp.get_data()),            #We use json.loads to convert a the "resp.get_data string"
                {'message': 'Hello, world!'}             #Into a valifd json representation (: dictionary)
            )
