# -*- coding: utf-8 -*-

from unittest import TestCase, main
from hotelspro_client.client import Coral


class TestClient(TestCase):
    search_payload = {"pax": "1", "checkin": "2016-10-10",
                      "checkout": "2016-10-20", "currency": "USD",
                      "destination_code": "18faa", "client_nationality": "tr"}

    def __init__(self, *args, **kwargs):
        self.coral = Coral("API_URL", "API_USERNAME", "API_PASSWORD")
        self.resp_search = self.coral.search(self.search_payload)
        self.product_code = self.resp_search['results'][0]['products']\
                                            [0]['code']
        super(TestClient, self).__init__(*args, **kwargs)

    def test_search(self):
        self.assertGreaterEqual(self.resp_search['count'], 1)
        self.assertIn('code', self.resp_search['results'][0]['products'][0])

        with self.assertRaisesRegexp(AssertionError, 'error_code'):
            self.coral.search({"pax": "1",
                               "checkin": "2016-10-10",
                               "currency": "USD",
                               "destination_code": "18faa",
                               "client_nationality": "tr"})
        with self.assertRaises(TypeError):
            self.coral.search()
            self.coral.search(["pax", "1"])

    def test_availability(self):
        resp = self.coral.availability(self.product_code)
        self.assertIsInstance(resp, dict)
        self.assertIn('meal_type', resp)
        self.assertIn('price', resp)
        self.assertIn('cost', resp)
        self.assertIsInstance(resp['rooms'], list)

        with self.assertRaisesRegexp(TypeError, 'arguments'):
            self.coral.availability()

        with self.assertRaisesRegexp(AssertionError, 'required'):
            self.coral.availability("")

    def test_provision(self):
        resp = self.coral.provision(self.product_code)
        self.assertIn('code', resp)

        with self.assertRaises(TypeError):
            self.coral.provision()

        with self.assertRaisesRegexp(AssertionError, 'required'):
            self.coral.provision("")

        with self.assertRaisesRegexp(AssertionError, 'error_code'):
            self.coral.provision("asdasdas")

    def test_book(self):
        provision_code = self.coral.provision(self.product_code)['code']
        resp = self.coral.book(provision_code, {'name': '1,abc,abc,adult'})
        self.assertIn('code', resp)
        self.assertEqual('succeeded', resp['status'])

        with self.assertRaises(TypeError):
            self.coral.book()
            self.coral.book(provision_code)
            self.coral.book(pax={'name': '1,abc,abc,adult'})
            self.coral.book(provision_code, ['name', '1,abc,abc,adult'])

        with self.assertRaises(AssertionError):
            self.coral.book("", None)
            self.coral.book("", {'name': '1,abc,abc,adult'})
            self.coral.book(provision_code, {})

        with self.assertRaisesRegexp(AssertionError, 'error_code'):
            self.coral.book("sadasdas", {'name': 'asdasdas'})

    def test_cancel(self):
        provision_code = self.coral.provision(self.product_code)['code']
        book_code = self.coral.book(provision_code,
                                    {'name': '1,abc,abc,adult'})['code']
        resp = self.coral.cancel(book_code)
        self.assertIsInstance(resp, dict)
        self.assertIn('code', resp)

        with self.assertRaises(TypeError):
            self.coral.cancel()

        with self.assertRaisesRegexp(AssertionError, 'required'):
            self.coral.cancel("")

        with self.assertRaisesRegexp(AssertionError, 'error_code'):
            self.coral.cancel("asdasdasd")

    def test_bookings(self):
        resp = self.coral.bookings()
        self.assertIsInstance(resp, list)

        provision_code = self.coral.provision(self.product_code)['code']
        book_code = self.coral.book(provision_code,
                                    {'name': '1,abc,abc,adult'})['code']
        resp = self.coral.bookings(book_code)
        self.assertIsInstance(resp, dict)

        with self.assertRaisesRegexp(AssertionError, 'error_code'):
            self.coral.bookings("asdasdasd")

if __name__ == '__main__':
    main()
