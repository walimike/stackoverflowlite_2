import unittest

from flask import json

from app.views import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client(self)
        self.test_data_question = {
            "qn_id": 1,
            "question": "Whats's up?"
        }
        self.test_data_answer = {
            "ans_id": 1,
            "answer" : "The sky is up"
        }

    # test for endpoints. Run using $pytest
    def test_get_all_questions(self):
        response = self.client.get('/stackoverlow/api/v1/questions', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_question(self):
        res = self.client.post('/stackoverlow/api/v1/questions', data=json.dumps(self.test_data_question), content_type='application/json')
        self.assertEqual(res.status_code, 201)

    def test_get_one_question(self):
        response = self.client.get('/stackoverlow/api/v1/questions/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_post_answer(self):
        res = self.client.post('/stackoverlow/api/v1/questions/1/answers', data=json.dumps(self.test_data_answer), content_type='application/json')
        self.assertEqual(res.status_code, 201)