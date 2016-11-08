# -*- coding: utf-8 -*-

import requests
import json


class Coral(object):
    """ A python client library for HotelsPro. """

    def __init__(self, api_url="http://localhost:8000/api/v2/", username=None,
                 password=None):
        """ Initialization method. """

        self.API_BASE_URL = api_url
        self.api_user = username
        self.api_pass = password
        self.req_session = self._authenticate()

    def _authenticate(self):
        """ This private method authenticate requests library.

            :returns session object -- Authenticated requests session object.
        """
        ses = requests.session()
        ses.auth = (self.api_user, self.api_pass)
        return ses

    def search(self, payload):
        """ This method is used for getting hotel information and properties on
            a specific date range (check-out - check-in), with a designated
            amount of people (pax) from /search endpoint.

            :param payload (*)(dict): parameters such as pax,checkin,checkout,
                              hotel code or destination code,currency,client
                              nationality.
            :returns json -- Detailed search result.
        """
        assert payload or isinstance(payload, dict), "Payload is required and \
must be a dict"
        resp = self.req_session.get(self.API_BASE_URL + "search",
                                    params=payload)
        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()

    def availability(self, product_code):
        """ This method is used for getting information of a hotel(s) room
            availability via GET from /availability endpoint.

            :param product_code (*)(str): A code coming from searching step.
            :returns json -- Result of availability step.
        """
        assert product_code, "Product code is required!"
        resp = self.req_session.get(self.API_BASE_URL + "availability/" +
                                    product_code)
        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()

    def provision(self, product_code):
        """ This method is used to get the last second information of the
            product that either it is available or not by POST method.

            :param product_code (str): A code coming from searching step.
            :returns json -- If the product is available, this method returns
                             with provision code.
        """
        assert product_code, "Product code is required!"
        resp = self.req_session.post(self.API_BASE_URL + "provision/" +
                                     product_code)
        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()

    def book(self, provision_code, pax):
        """ This method is the fourth and last step of hotel booking.
            The method is used to book a product that have made sure
            available with 'Provision' request. Carry the unique code which
            has got from Provision response.

            :param provision_code (*)(str): A code coming from provision step.
            :param pax (*)(json): Customer information.
            :returns json -- Booking informations.
        """
        assert provision_code and pax, "provision code and pax is required!"
        assert isinstance(pax, dict), "pax must be a dictionary!"
        resp = self.req_session.post(self.API_BASE_URL + "book/" +
                                     provision_code, data=pax)
        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()

    def cancel(self, book_code):
        """ This method is used to cancel booking.

            :param book_code (*)(str): Value from the booking response.
            :returns json -- Cancellation process results.
        """
        assert book_code, "book_code is required for the cancellation!"
        resp = self.req_session.post(self.API_BASE_URL + "cancel/" + book_code)

        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()

    def bookings(self, book_code=""):
        """ This method is also known for 'booking list' and
            it is for retrieving past booking data.

            :param book_code (str): a specific booking code.
            :returns json -- All consumer's bookings or specific booking info.
        """
        url = self.API_BASE_URL + "bookings/"
        if book_code:
            url += book_code
        resp = self.req_session.get(url)
        if resp.status_code != 200:
            return json.loads(resp.text)

        return resp.json()
