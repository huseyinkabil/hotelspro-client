# -*- coding: utf-8 -*-

from unittest import TestCase, main
from hotelspro_client.client import Coral


class TestClient(TestCase):
    _hotel_code = "HOTEL_CODE"
    _prod_code = "PRODUCTION_CODE"
    _book_code = "BOOK_CODE"

    def __init__(self, *args, **kwargs):
        self._coral = Coral("API_USERNAME", "API_PASSWORD")
        self._search_resp = self._coral.search({"pax": "1",
                                                "checkin": "2016-09-30",
                                                "checkout": "2016-10-03",
                                                "currency": "USD",
                                                "hotel_code": self._hotel_code,
                                                "client_nationality": "tr"})

        super(TestClient, self).__init__(*args, **kwargs)

    def test_search(self):
        # self.assertEqual(200, self._search_resp.status_code)
        # resp = self._search_resp.json()
        self.assertGreaterEqual(self._search_resp['count'], 1)
        self.assertIn('code', self._search_resp['results'][0]['products'][0])

    def test_search_failed(self):
        pass
        # resp = self._coral.search({"pax": "1",
        #                            "checkin": "2016-09-30",
        #                            "currency": "USD",
        #                            "hotel_code": self._hotel_code,
        #                            "client_nationality": "tr"})
        # self.assertEqual(400, resp.status_code)

    def test_availability(self):
        resp = self._coral.availability(self._prod_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, dict)
        self.assertIn('meal_type', resp)
        self.assertIn('price', resp)
        self.assertIn('cost', resp)
        self.assertIsInstance(resp['rooms'], list)

    def test_provision(self):
        resp = self._coral.provision(self._prod_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIn('code', resp)

    def test_book_and_cancel(self):
        prov_code = self._coral.provision(self._prod_code)['code']
        resp = self._coral.book(prov_code, {'name': '1,abc,abc,adult'})
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIn('code', resp)
        self.assertEqual('succeeded', resp['status'])

        resp = self._coral.cancel(resp['code'])
        self.assertIsInstance(resp, dict)
        self.assertIn('code', resp)

    def test_bookings(self):
        resp = self._coral.bookings()
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, list)

        resp = self._coral.bookings(self._book_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(resp, dict)

if __name__ == '__main__':
    main()
