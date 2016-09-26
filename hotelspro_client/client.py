# -*- coding: utf-8 -*-

import requests


class Coral(object):

    API_BASE_URL = "http://localhost:8000/api/v2/"

    def __init__(self, username=None, password=None):
        """ docstring """
        self.api_user = username
        self.api_pass = password
        self.req_session = self._authenticate()

    def _authenticate(self):
        ses = requests.session()
        ses.auth = (self.api_user, self.api_pass)
        return ses

    def _generate_url(self, action, params):
        if params:
            if not isinstance(params, dict):
                raise TypeError("params variable should be a dictionary!")

        q_str = ""
        for k, v in params.items():
            q_str += "{}={}&".format(k, v)
        url = "{}{}/?{}".format(self.API_BASE_URL, action, q_str[:-1])
        return url

    def _check_production_code(self, prod_code):
        if not prod_code:
            raise StandardError("production_code is required!")

    def search(self, payload):
        """ doctstring """
        resp = self.req_session.get(self._generate_url("search", payload))
        return resp.json()

    def availability(self, prod_code):
        """ docstring """
        self._check_production_code(prod_code)
        resp = self.req_session.get(self.API_BASE_URL + "availability/" +
                                    prod_code)
        return resp.json()

    def provision(self, prod_code):
        """ docstring """
        self._check_production_code(prod_code)
        resp = self.req_session.post(self.API_BASE_URL + "provision/" +
                                     prod_code)
        return resp.json()

    def book(self, prod_code, pax):
        """ docstring """
        self._check_production_code(prod_code)
        if pax and not isinstance(pax, dict):
            raise StandardError("pax must be a dictionary!")

        resp = self.req_session.post(self.API_BASE_URL + "book/" + prod_code,
                                     data=pax)
        return resp.json()
