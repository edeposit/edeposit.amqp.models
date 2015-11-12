#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from schema import And
from schema import Use
from schema import Schema
from schema import Optional

from isbn_validator import is_valid_isbn

import riv
import libraries


# Validators ==================================================================
def _str_error(what):
    return "Špatně zadána položka `%s`. Očekáván neprázdný řetězec." % what


EpublicationValidator = Schema({
    'title': And(
        basestring,
        len,
        error=_str_error("title")
    ),
    'poradi_vydani': And(
        basestring,
        len,
        error=_str_error("poradi_vydani")
    ),
    'misto_vydani': And(
        basestring,
        len,
        error=_str_error("misto_vydani")
    ),
    'rok_vydani': Use(
        int,
        error="Nesprávný formát pro `rok_vydani`. Očekáván int."
    ),
    'zpracovatel_zaznamu': And(
        basestring,
        len,
        error=_str_error("zpracovatel_zaznamu")
    ),

    # optionals
    Optional('podnazev'): And(
        basestring,
        len,
        error=_str_error("podnazev")
    ),
    Optional('cast'): And(
        basestring,
        len,
        error=_str_error("cast")
    ),
    Optional('nazev_casti'): And(
        basestring,
        len,
        error=_str_error("nazev_casti")
    ),
    Optional('isbn'): And(
        basestring,
        len,
        is_valid_isbn,
        error=(
            "`isbn` je špatného datového typu, či s neplatným kontrolním "
            "součtem."
        )
    ),
    Optional('isbn_souboru_publikaci'): And(
        basestring,
        len,
        is_valid_isbn,
        error=(
            "`isbn_souboru_publikaci` je špatného datového typu, či s "
            "neplatným kontrolním součtem."
        )
    ),
    Optional('author1'): And(
        basestring,
        len,
        error=_str_error("author1")
    ),
    Optional('author2'): And(
        basestring,
        len,
        error=_str_error("author2")
    ),
    Optional('author3'): And(
        basestring,
        len,
        error=_str_error("author3")
    ),
    Optional('nakladatel_vydavatel'): And(
        basestring,
        len,
        error=_str_error("nakladatel_vydavatel")
    ),
    Optional('vydano_v_koedici_s'): And(
        basestring,
        len,
        error=_str_error("vydano_v_koedici_s")
    ),
    Optional('cena'): Use(
        float,
        error="Špatně zadaný parametr `cena`. Očekávána hodnota typu float."
    ),
    Optional('jednotka_ceny'): And(
        basestring,
        len,
        error=_str_error("jednotka_ceny")
    ),
    Optional("url"): And(
        basestring,
        len,
        error=_str_error("url")
    ),
    Optional("anotace"): And(
        basestring,
        len,
        error=_str_error("anotace")
    ),
    Optional("libraries_that_can_access"): And(
        lambda x: set(x).issubset(libraries.LIBRARY_IDS),
        error=(
            "Špatně zadaný parametr `libraries_that_can_access`. "
            "Očekávána hodnota ze subsetu %s." % repr(libraries.LIBRARY_IDS)
        )
    ),
    Optional("category_for_riv"): And(
        int,
        lambda x: x in riv.RIV_CAT_IDS,
        error=(
            "Špatně zadaná hodnota pro riv. Očekáván "
            "0 >= int < %d." % riv.RIV_CAT_IDS[-1]
        )
    ),
})
