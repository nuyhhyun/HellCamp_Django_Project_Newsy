from django.test import TestCase
import requests


class TestCase1(TestCase):
    def is_the_requests_done(self):
        res = requests.get("http://rss.nocutnews.co.kr/Nocutnews.xml")
        self.assertEqual(res.status_code, 200)


class TestCase2(TestCase):
    res = requests.get("http://rss.nocutnews.co.kr/Nocutnews.xml")
    assert res
