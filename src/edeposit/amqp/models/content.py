#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from functools import partial
from operator import contains

from schema import And
from schema import Schema
from schema import Optional

from isbn_validator import is_valid_isbn

import riv
import libraries


# Validators ==================================================================
EpublicationValidator = Schema({
    'title': And(unicode, len),
    'poradi_vydani': And(unicode, len),
    'misto_vydani': And(unicode, len),
    'rok_vydani': int,
    'zpracovatel_zaznamu': "",

    Optional('podnazev'): And(unicode, len),
    Optional('cast'): And(unicode, len),
    Optional('nazev_casti'): And(unicode, len),
    Optional('isbn'): is_valid_isbn,
    Optional('isbn_souboru_publikaci'): is_valid_isbn,
    Optional('author1'): And(unicode, len),
    Optional('author2'): And(unicode, len),
    Optional('author3'): And(unicode, len),
    Optional('nakladatel_vydavatel'): And(unicode, len),
    Optional('vydano_v_koedici_s'): And(unicode, len),
    Optional('cena'): int,
    Optional("url"): And(str, len),
    Optional("anotace"): And(unicode, len),
    Optional("libraries_that_can_access"): partial(
        contains,
        libraries.LIBRARY_IDS
    ),
    Optional("category_for_riv"): And(int, partial(contains, riv.RIV_CAT_IDS)),
})
