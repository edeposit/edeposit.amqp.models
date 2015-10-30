#!/usr/bin/python
from schema import Schema, And, Use, Optional
from isbn_validator import is_valid_isbn
from functools import partial
from operator import contains
import .libraries
import .riv

producent = Schema({
    'title': And(unicode,len),
    'id':And(str,len),
    Optional('sysnumber'): And(str,len)
})

declarer = Schema({
    'username':And(str,len)
})

epublication = Schema({
    'title': And(unicode,len),
    Optional('podnazev'): And(unicode,len),
    Optional('cast'): And(unicode,len),
    Optional('nazev_casti'): And(unicode,len),
    Optional('isbn'): is_valid_isbn,
    Optional('generated_isbn'): partial(isinstance,bool),
    Optional('isbn_souboru_publikaci'): is_valid_isbn,
    Optional('author1'): And(unicode,len),
    Optional('author2'): And(unicode,len),
    Optional('author3'): And(unicode,len),
    'poradi_vydani': And(unicode,len),
    'misto_vydani': And(unicode,len),
    'rok_vydani': int,
    'misto_vydani': And(unicode,len),
    'nakladatel_vydavatel': producent.validate,
    Optional('vydano_v_koedici_s'): And(unicode,len),
    Optional('cena'):Decimal,
    libraries_accesing: partial(isinstance,bool),
    libraries_that_can_access: partial(contains,libraries.ids),
    Optional(offer_to_riv): partial(isinstance,bool),
    Optional(category_for_riv):And(int,partial(contains,riv.ids)),
    'zpracovatel_zaznamu': declarer.validate,
    Optional(url): And(str,len),
    Optional(anotace): And(unicode,len)
})
