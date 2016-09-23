from hotelspro_client.client import Coral

_coral = Coral("API_USERNAME", "API_PASSWORD")

print cor.search({"pax": "1", "checkin": "2016-09-30",
                  "checkout": "2016-10-03", "currency": "USD",
                  "destination_code": "11260", "client_nationality": "tr"})
