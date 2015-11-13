#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import copy

from schema import And
from schema import Use
from schema import Schema
from schema import Optional

from isbn_validator import is_valid_isbn

import riv
import libraries


# Variables ===================================================================
_REMAPS = {
    "riv": "category_for_riv",
    "nazev": "title",
    "autor1": "author1",
    "autor2": "author2",
    "autor3": "author3",
    "zpristupneni": "libraries_that_can_access",
}


# Validators ==================================================================
def _str_error(what):
    return "Špatně zadána položka `%s`. Očekáván neprázdný řetězec." % what


def _str_and(item_name):
    return And(basestring, len, error=_str_error(item_name))


def _str_and_ISBN(item_name):
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
    'nazev': _str_and("title"),
    'poradi_vydani': _str_and("poradi_vydani"),
    'misto_vydani': _str_and("misto_vydani"),
    'rok_vydani': Use(
        int,
        error="Nesprávný formát pro `rok_vydani`. Očekáván int."
    ),
    'zpracovatel_zaznamu': _str_and("zpracovatel_zaznamu"),

    # optionals
    Optional('podnazev'): _str_and("podnazev"),
    Optional('cast'): _str_and("cast"),
    Optional('nazev_casti'): _str_and("nazev_casti"),
    Optional('isbn'): _str_and_ISBN("isbn"),
    Optional('isbn_souboru_publikaci'): _str_and_ISBN("isbn_souboru_publikaci"),
    Optional('autor1'): _str_and("autor1"),
    Optional('autor2'): _str_and("autor2"),
    Optional('autor3'): _str_and("autor3"),
    Optional('nakladatel_vydavatel'): _str_and("nakladatel_vydavatel"),
    Optional('vydano_v_koedici_s'): _str_and("vydano_v_koedici_s"),
    Optional('cena'): Use(
        float,
        error="Špatně zadaný parametr `cena`. Očekávána hodnota typu float."
    ),
    Optional('jednotka_ceny'): _str_and("jednotka_ceny"),
    Optional("url"): _str_and("url"),
    Optional("anotace"): _str_and("anotace"),
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


def czech_to_edeposit_dict(czech_dict):
    """
    This function may be used to remap czech dict validated by
    :class:`EpublicationValidator` to terms used in edeposit.

    For example to remap ``zpristupneni`` to ``libraries_that_can_access``.

    Args:
        czech_dict (dict): Dictionary with czech terms.

    Returns:
        dict: Dictionary with edeposit terms.
    """
    edep_dict = copy.deepcopy(czech_dict)

    for czech_key, edep_term in _REMAPS.iteritems():
        if czech_key in edep_dict:
            edep_dict[edep_term] = edep_dict[czech_key]
            del edep_dict[czech_key]

    return edep_dict


def edeposit_to_czech_dict(edep_dict):
    """
    Remap edeposit's terms to czech terms used by
    :class:`EpublicationValidator`.

    Args:
        edep_dict (dict): Dictionary with edeposit terms.

    Returns:
        dict: Dictionary with czech terms.
    """
    czech_dict = copy.deepcopy(edep_dict)

    for czech_key, edep_term in _REMAPS.iteritems():
        if edep_term in czech_dict:
            czech_dict[czech_key] = czech_dict[edep_term]
            del czech_dict[edep_term]

    return czech_dict
