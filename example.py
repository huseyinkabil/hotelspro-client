from hotelspro_client.client import Coral

_coral = Coral("API_USERNAME", "API_PASSWORD")

search_resp = _coral.search({"pax": "1", "checkin": "2016-09-30",
                             "checkout": "2016-10-03", "currency": "USD",
                             "hotel_code": "135f3a",
                             "client_nationality": "tr"})
print search_resp
print "======================="

prod_code = search_resp[u'results'][0][u'products'][0][u'code']

print _coral.availability(prod_code)

provision_resp = _coral.provision(prod_code)
print provision_resp
print "======================="

book_resp = _coral.book(provision_resp[u'code'],
                        {"name": "1,Huseyin,Kabil,adult"})
print book_resp
print "======================="

print _coral.cancel(book_resp[u'code'])
