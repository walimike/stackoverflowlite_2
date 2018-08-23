import unittest

from flask import json

from app.views import app


class EndpointsTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    # test for endpoints. Run using $pytest
    def test_can_get_all_questions(self):
        response = self.client.get('/stackoverlow/api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_can_post_question(self):
        test_question = {"qn_id":1, "question":"What's up?"}
        res = self.client.post('/stackoverlow/api/v1/questions', json = test_question)
        self.assertEqual(res.status_code, 201)

    def test_can_get_one_question(self):
        response = self.client.get('/stackoverlow/api/v1/questions/1')
        self.assertEqual(response.status_code, 200)

    def test_can_post_answer(self):
        test_answer = {"ans_id":1, "answer":"The sky is up"}
        res = self.client.post('/stackoverlow/api/v1/questions/1/answer', json = test_answer)
        self.assertEqual(res.status_code, 201)