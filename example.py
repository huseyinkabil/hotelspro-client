from hotelspro_client.client import Coral

coral = Coral(username="API_USERNAME", password="API_PASSWORD")

search_resp = coral.search({"pax": "1", "checkin": "2016-11-10",
                            "checkout": "2016-11-15", "currency": "USD",
                            "destination_code": "18faa",
                            "client_nationality": "tr"})
print "=" * 10, "SEARCH", "=" * 10
print search_resp

prod_code = search_resp[u'results'][0][u'products'][0][u'code']

print "=" * 10, "AVAILABILITY", "=" * 10
print coral.availability(prod_code)

provision_resp = coral.provision(prod_code)
print "=" * 10, "PROVISION", "=" * 10
print provision_resp

book_resp = coral.book(provision_resp.get('code', ''),
                       {"name": "1,Huseyin,Kabil,adult"})
print "=" * 10, "BOOK", "=" * 10
print book_resp

print "=" * 10, "CANCELLATION", "=" * 10
print coral.cancel(book_resp.get('code', ''))

# print "=" * 50
# print "BOOKINGS"
# print "=" * 50
# print coral.bookings()  # list all consumer's bookings
# print coral.bookings(book_resp[u'code'])
