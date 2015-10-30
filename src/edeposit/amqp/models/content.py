#!/usr/bin/python
from schema import Schema, And, Use, Optional

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
    Optional('isbn_souboru_publikaci'): And(unicode,len),
    'poradi_vydani': And(unicode,len),
    'misto_vydani': And(unicode,len),
    'rok_vydani': int,
    'nakladatel_vydavatel': producent.validate,
    'zpracovatel_zaznamu': declarer.validate,
})
