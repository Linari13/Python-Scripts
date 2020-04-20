from models.user import UserModel
from tests.base_test import BaseTest
import json


class UserTest(BaseTest):
    def test_register_user(self):                           # Tests that user can be registered
        with self.app() as client:                          # Launches the client
            with self.app_context():                        # Loads up the app context
                # Sending a post request to our actual API
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({'message': 'User created successfully'},
                                     json.loads(response.data))

    def test_register_and_login(self):                      # user can login
        with self.app() as client:                          # the client
            with self.app_context():                        # Loads up the app context
                # Sending a post request to our actual API
                client.post('/register', data={'username': 'test', 'password': '1234'})
                auth_response = client.post('/auth',
                                            data=json.dumps({'username': 'test', 'password': '1234'}),
                                            headers={'Content-type': 'application/json'})

                self.assertIn('access_token', json.loads(auth_response.data).keys()) #


    def register_duplicate_user(self):                      # Test duplicate user register error
        with self.app() as client:                          # the client
            with self.app_context():                        # Loads up the app context
                # Sending a post request to our actual API
                client.post('/register', data={'username': 'test', 'password': '1234'})
                response = client.post('/register', data={'username': 'test', 'password': '1234'})

                self.assertEqual(response.status_code, 400)
                self.assertDictEqual({'message': 'A user with that username already exists'},
                                     json.loads(response.data))
