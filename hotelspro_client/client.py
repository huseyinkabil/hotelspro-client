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
        q_str = ""
        for k, v in params.items():
            q_str += "{}={}&".format(k, v)
        url = "{}{}/?{}".format(self.API_BASE_URL, action, q_str[:-1])
        return url

    def search(self, params):
        """ """
        resp = self.req_session.get(self._generate_url("search", params))
        return resp.json()
