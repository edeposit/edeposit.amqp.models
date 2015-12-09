#! /usr/bin/env python
# -*- coding: utf-8 -*-,
#
# Interpreter version: python 2.7,
#
# Imports =====================================================================


# Variables ===================================================================
DEFAULT_LIBRARY = 'narodni-knihovna-ceske-republiky'  #:

#: Dictionary used to map libraries to their descriptions.
LIBRARY_MAP = {
    'moravska-zemska-knihovna-v-brne': 'Moravská zemská knihovna v Brně',
    'vedecka-knihovna-v-olomouci': 'Vědecká knihovna v Olomouci',
    'jihoceska-vedecka-knihovna-v-ceskych-budejovicich': 'Jihočeská vědecká knihovna v Českých Budějovicích',
    'studijni-a-vedecka-knihovna-v-hradci-kralove': 'Studijní a vědecká knihovna v Hradci Králové',
    'krajska-knihovna-karlovy-vary': 'Krajská knihovna Karlovy Vary',
    'stredoceska-vedecka-knihovna-v-kladne': 'Středočeská vědecká knihovna v Kladně',
    'moravskoslezska-vedecka-knihovna-v-ostrave': 'Moravskoslezská vědecká knihovna v Ostravě',
    'krajska-vedecka-knihovna-v-liberci': 'Krajská vědecká knihovna v Liberci',
    'krajska-knihovna-v-pardubicich': 'Krajská knihovna v Pardubicích',
    'studijni-a-vedecka-knihovna-plzenskeho-kraje': 'Studijní a vědecká knihovna Plzeňského kraje',
    'mestska-knihovna-v-praze': 'Městská knihovna v Praze',
    'severoceska-vedecka-knihovna-v-usti-nad-labem': 'Severočeská vědecká knihovna v Ústí nad Labem',
    'krajska-knihovna-vysociny-havlickuv-brod': 'Krajská knihovna Vysočiny (Havlíčkův Brod)',
    'krajska-knihovna-frantiska-bartose-ve-zline': 'Krajská knihovna Františka Bartoše ve Zlíně',
}

#: List of ID's of libraries.
LIBRARY_IDS = set(LIBRARY_MAP.keys())
