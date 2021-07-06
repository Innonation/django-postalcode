# Import
import re, logging

# Django Import
from django.shortcuts import render

# cap_verification Import
from .choices import StatusCAP, CapRegex


def verify_cap(country_code, cap):
    """
     Dato in input il countrycode relativo alla nazione e il cap che si vuole verificare,
     restituisce la validità del cap per quella nazione.
    :param country_code: codice identificativo della nazione da controllare
    :param cap: cap da controllare
    :return: Oggetto di tipo StatusCAP (Enum) che contiene i dettagli di stato
    """
    try:
        for row in CapRegex:
            if row.name == country_code:
                for regex in row.value[0][1:]:
                    if re.match(regex, cap):
                        return StatusCAP.VALID
                return StatusCAP.NOT_VALID
        return StatusCAP.NOT_FOUND
    except:
        return StatusCAP.EXCEPTION
