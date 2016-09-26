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
                raise TypeError("params variable should be a dictionary.")

        q_str = ""
        for k, v in params.items():
            q_str += "{}={}&".format(k, v)
        url = "{}{}/?{}".format(self.API_BASE_URL, action, q_str[:-1])
        return url

    def search(self, params):
        """ doctstring """
        resp = self.req_session.get(self._generate_url("search", params))
        return resp.json()

    def availability(self, production_code):
        """ docstring """
        if not production_code:
            raise StandardError("production_code is required!")

        resp = self.req_session.get(self.API_BASE_URL + "availability/" +
                                    production_code)
        return resp.json()
