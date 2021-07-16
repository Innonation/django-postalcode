# Import
import re, logging

# Django Import
from django.shortcuts import render

# cap_verification Import
from .choices import StatusCAP, CapRegexApha2, CapRegexApha3


def verify_cap(country_code, cap, alpha2=True):
    """
     Dato in input il countrycode relativo alla nazione e il cap che si vuole verificare,
     restituisce la validità del cap per quella nazione.
    :param country_code: codice identificativo della nazione da controllare
    :param cap: cap da controllare
    :return: Oggetto di tipo StatusCAP (Enum) che contiene i dettagli di stato
    """
    try:
        enum_class = CapRegexApha2 if alpha2 else CapRegexApha3
        for row in enum_class:
            if row.name == country_code and re.match(row.value[1], cap):
                return StatusCAP.VALID
            else:
                return StatusCAP.NOT_VALID
        return StatusCAP.NOT_FOUND
    except:
        return StatusCAP.EXCEPTION
