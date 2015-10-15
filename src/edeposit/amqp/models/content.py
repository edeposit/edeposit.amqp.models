#!/usr/bin/python
from schema import Schema, And, Use, Optional


epublication = Schema({
    'title': And(unicode,len),
    Optional('podnazev'): And(unicode,len),
    
})
