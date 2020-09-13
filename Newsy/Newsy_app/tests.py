from django.test import TestCase, Client
import requests


class NewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_is_the_requests_done(self):
        res = requests.get("http://rss.nocutnews.co.kr/Nocutnews.xml")
        self.assertEqual(res.status_code, 200)

    def test_view_category_news(self):
        resp = self.client.get("/news/Latest")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_politics(self):
        resp = self.client.get("/Politics/Politics")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_social(self):
        resp = self.client.get("/Social/Social")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_economy(self):
        resp = self.client.get("/Economy/Economy")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_sports(self):
        resp = self.client.get("/Sports/Sports")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_local(self):
        resp = self.client.get("/Local/Local")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_global(self):
        resp = self.client.get("/Global/Global")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_sports(self):
        resp = self.client.get("/Sports/Sports")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_it(self):
        resp = self.client.get("/IT/IT")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_enter(self):
        resp = self.client.get("/Enter/Entertain")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_culture(self):
        resp = self.client.get("/Culture/Culture")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_column(self):
        resp = self.client.get("/Column/Column")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_photo(self):
        resp = self.client.get("/Photo/Photo")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_scoop(self):
        resp = self.client.get("/Only/Scoop")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_home(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)

