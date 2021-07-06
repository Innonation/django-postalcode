=====
postal_code
=====

postal_code is a Django app to verify if the cap of a Nation is valid.

Quick start
-----------

1. Add "postal_code" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'postal_code',
    ]


use the function verify_cap

Given in input the country code relating to the nation and the postal code to be verified,
returned the validity of the zip code for that country.

country_code:  nation code id (Codice ISO 3166 alpha2)

cap: postal code

return StatusCAP object (Enum)

example:

from postal_code.utils import verify_cap

country = 'IT'

cap = '95000'

result = verify_cap(country, cap)


