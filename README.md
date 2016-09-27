hotelspro-client
==================

A python client library for <a href="https://api.hotelspro.com">HotelsPro</a>

### Installation
===================

```bash
$ python setup.py install
```

or

```bash
$ (sudo) pip install -e /path/to/directory
```

***notes***
- If you are using virtualenv you don't need to use sudo command.

### Usage
```python
from hotelspro_client.client import Coral

_coral = Coral("API_USERNAME", "API_PASSWORD")

```
**example call: search()**

```python
from hotelspro_client.client import Coral

_coral = Coral("API_USERNAME", "API_PASSWORD")

print _coral.search({"pax": "1", "checkin": "2016-09-30",
                             "checkout": "2016-10-03", "currency": "USD",
                             "hotel_code": "135f3a",
                             "client_nationality": "tr"})
```

**response**
```javascript
{
  u"count": 1,
  u"code": "5076c71344dd4e308900939393707bff",
  u"next_page_code": null,
  u"results": [
    {
      u"hotel_code": "135f3a",
      u"checkout": "2016-10-03",
      u"checkin": "2016-09-30",
      u"destination_code": "206ec",
      u"products": [
        {
          u"code":"PRODUCT_CODE",
          u"list_price": "137.27",
          u"offer": false,
          u"pay_at_hotel": false,
          u"price": "137.27",
          u"currency": "GBP",
          u"cost": "137.27",
          u"rooms": [
            {
              u"pax": {
                u"adult_quantity": 1,
                u"children_ages": []
              },
              u"room_category": "Standard",
              u"room_description": "TWIN STANDARD",
              u"room_type": "TW"
            }
          ],
          u"nonrefundable": false,
          u"providers": [
            "hbeds"
          ],
          u"supports_cancellation": true,
          u"hotel_currency": null,
          u"hotel_price": null,
          u"meal_type": "BC",
          u"policies": [
            {
              u"ratio": "0.34",
              u"days_remaining": 4
            }
          ],
          u"minimum_selling_price": null,
          u"view": false
        }
      ]
    }
  ]
}
```

**notes**
- check out examples for other methods.
