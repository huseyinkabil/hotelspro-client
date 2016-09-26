from hotelspro_client.client import Coral

_coral = Coral("API_USERNAME", "API_PASSWORD")

print _coral.search({"pax": "1", "checkin": "2016-09-30",
                     "checkout": "2016-10-03", "currency": "USD",
                     "destination_code": "11260", "client_nationality": "tr"})

print _coral.availability("E186IT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAv0z5f1sESqaj3TH\
                          _Hjv9uyAAAAAAAAAAAAAAAATDQAAAAAPF0EBAAOmoe41a0ghJAAI\
                          AgAAAAAAAAAAABA")
