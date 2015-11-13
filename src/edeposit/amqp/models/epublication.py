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


def strAnd(item_name):
    return And(basestring, len, error=_str_error(item_name))


def strAndISBN(item_name):
    return And(
        basestring,
        len,
        is_valid_isbn,
        error=(
            "`%s` je špatného datového typu, či s neplatným "
            "kontrolním součtem."
        ) % item_name
    )


EpublicationValidator = Schema({
    'nazev': strAnd("title"),
    'poradi_vydani': strAnd("poradi_vydani"),
    'misto_vydani': strAnd("misto_vydani"),
    'rok_vydani': Use(
        int,
        error="Nesprávný formát pro `rok_vydani`. Očekáván int."
    ),
    'zpracovatel_zaznamu': strAnd("zpracovatel_zaznamu"),

    # optionals
    Optional('podnazev'): strAnd("podnazev"),
    Optional('cast'): strAnd("cast"),
    Optional('nazev_casti'): strAnd("nazev_casti"),
    Optional('isbn'): strAndISBN("isbn"),
    Optional('isbn_souboru_publikaci'): strAndISBN("isbn_souboru_publikaci"),
    Optional('autor1'): strAnd("autor1"),
    Optional('autor2'): strAnd("autor2"),
    Optional('autor3'): strAnd("autor3"),
    Optional('nakladatel_vydavatel'): strAnd("nakladatel_vydavatel"),
    Optional('vydano_v_koedici_s'): strAnd("vydano_v_koedici_s"),
    Optional('cena'): Use(
        float,
        error="Špatně zadaný parametr `cena`. Očekávána hodnota typu float."
    ),
    Optional('jednotka_ceny'): strAnd("jednotka_ceny"),
    Optional("url"): strAnd("url"),
    Optional("anotace"): strAnd("anotace"),
    Optional("zpristupneni"): And(
        lambda x: set(x).issubset(libraries.LIBRARY_IDS),
        error=(
            "Špatně zadaný parametr `libraries_that_can_access`. "
            "Očekávána hodnota ze subsetu %s." % repr(libraries.LIBRARY_IDS)
        )
    ),
    Optional("riv"): And(
        int,
        lambda x: x in riv.RIV_CAT_IDS,
        error=(
            "Špatně zadaná hodnota pro riv. Očekáván "
            "0 >= int < %d." % riv.RIV_CAT_IDS[-1]
        )
    ),
})
