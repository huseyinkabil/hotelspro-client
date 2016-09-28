# -*- coding: utf-8 -*-

import requests


class Coral(object):
    """ A python client library for HotelsPro. """

    API_BASE_URL = "http://localhost:8000/api/v2/"

    def __init__(self, username=None, password=None):
        """ Initialization method. """
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

    def _generate_url(self, endpoint, params):
        """ This private method generates a GET url with payload.

            :param endpoint (*)(str): API endpoint.
            :param params (*)(dict): payload parameters.
            :returns str -- Url encoded query string.
        """
        if params:
            if not isinstance(params, dict):
                raise TypeError("params variable should be a dictionary!")

        q_str = ""
        for k, v in params.items():
            q_str += "{}={}&".format(k, v)
        url = "{}{}/?{}".format(self.API_BASE_URL, endpoint, q_str[:-1])
        return url

    def _check_production_code(self, prod_code):
        """ This private method checks prod_code.

            :param (*)(str): production code.
        """
        if not prod_code:
            raise StandardError("production_code is required!")

    def search(self, payload):
        """ This method is used for getting hotel information and properties on
            a specific date range (check-out - check-in), with a designated
            amount of people (pax) from /search endpoint.

            :param payload (*)(dict): parameters such as pax,checkin,checkout,
                              hotel code or destination code,currency,client
                              nationality.
            :returns json -- Detailed search result.
        """
        resp = self.req_session.get(self._generate_url("search", payload))
        return resp.json()

    def availability(self, prod_code):
        """ This method is used for getting information of a hotel(s) room
            availability via GET from /availability endpoint.

            :param prod_code (*)(str): A code coming from searching step.
            :returns json -- Result of availability step.
        """
        self._check_production_code(prod_code)
        resp = self.req_session.get(self.API_BASE_URL + "availability/" +
                                    prod_code)
        return resp.json()

    def provision(self, prod_code):
        """ This method is used to get the last second information of the
            product that either it is available or not by POST method.

            :param prod_code (str): A code coming from searching step.
            :returns json -- If the product is available, this method returns
                             with provision code.
        """
        self._check_production_code(prod_code)
        resp = self.req_session.post(self.API_BASE_URL + "provision/" +
                                     prod_code)
        return resp.json()

    def book(self, prov_code, pax):
        """ This method is the fourth and last step of hotel booking.
            The method is used to book a product that have made sure
            available with 'Provision' request. Carry the unique code which
            has got from Provision response.

            :param prov_code (*)(str): A code coming from provision step.
            :param pax (*)(json): Customer information.
            :returns json -- Booking informations.
        """
        if not prov_code or not pax:
            raise StandardError("provision code and pax information\
                                 is required!")
        if not isinstance(pax, dict):
            raise StandardError("pax must be a dictionary!")

        resp = self.req_session.post(self.API_BASE_URL + "book/" + prov_code,
                                     data=pax)
        return resp.json()

    def cancel(self, book_code):
        """ This method is used to cancel booking.

            :param book_code (*)(str): Value from the booking response.
            :returns json -- Cancellation process results.
        """
        if not book_code:
            raise StandardError("book_code is required for the cancellation!")
        resp = self.req_session.post(self.API_BASE_URL + "cancel/" + book_code)
        return resp.json()

    def bookings(self, code=""):
        """ This method is also known for 'booking list' and
            it is for retrieving past booking data.

            :param code (*)(str): a specific booking code.
            :returns json -- All consumer's bookings or specific booking info.
        """
        url = self.API_BASE_URL + "bookings/"
        if code:
            url += code
        resp = self.req_session.get(url)
        return resp.json()
