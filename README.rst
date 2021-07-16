=====
postal_code
=====

postal_code is a Django app to verify if the cap of a Nation is valid.

Quick start
-----------

use the function verify_cap

Given in input the country code relating to the nation and the postal code to be verified,
returned the validity of the zip code for that country.

country_code:  nation code id (Codice ISO 3166 alpha2 or alpha3)

cap: postal code

alpha2: True if you want to pass an alpha2 code, False otherwise (default True)

return StatusCAP object (Enum)

example:

::

    from postal_code.utils import verify_cap
    from postal_code.choices import StatusCAP

    country = 'IT'
    cap = '95000'
    result = verify_cap(country, cap)
    if result == StatusCAP.VALID:
        print("Perfect!")
or:

::

    from postal_code.utils import verify_cap
    from postal_code.choices import StatusCAP

    country = 'ITA'
    cap = '95000'
    result = verify_cap(country, cap, False)
    if result == StatusCAP.VALID:
        print("Perfect!")

