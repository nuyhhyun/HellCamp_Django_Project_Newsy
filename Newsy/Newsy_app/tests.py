from django.test import TestCase, Client
import requests


class TestCase1(TestCase):
    def test_is_the_requests_done(self):
        res = requests.get("http://rss.nocutnews.co.kr/Nocutnews.xml")
        self.assertEqual(res.status_code, 200)

    def test_view_category_news(self):
        c = Client()
        resp = c.get("/news/Latest")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_politics(self):
        c = Client()
        resp = c.get("/Politics/Politics")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_social(self):
        c = Client()
        resp = c.get("/Social/Social")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_economy(self):
        c = Client()
        resp = c.get("/Economy/Economy")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_sports(self):
        c = Client()
        resp = c.get("/Sports/Sports")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_local(self):
        c = Client()
        resp = c.get("/Local/Local")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_global(self):
        c = Client()
        resp = c.get("/Global/Global")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_sports(self):
        c = Client()
        resp = c.get("/Sports/Sports")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_it(self):
        c = Client()
        resp = c.get("/IT/IT")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_enter(self):
        c = Client()
        resp = c.get("/Enter/Entertain")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_culture(self):
        c = Client()
        resp = c.get("/Culture/Culture")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_column(self):
        c = Client()
        resp = c.get("/Column/Column")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_photo(self):
        c = Client()
        resp = c.get("/Photo/Photo")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_scoop(self):
        c = Client()
        resp = c.get("/Only/Scoop")
        self.assertEqual(resp.status_code, 200)

    def test_view_category_home(self):
        c = Client()
        resp = c.get("/")
        self.assertEqual(resp.status_code, 200)

