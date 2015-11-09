#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================


# Variables ===================================================================
RIV_CATEGORIES = [
    (1, "společenské, humanitní a umělecké vědy (SHVa)"),
    (2, "společenské vědy (SHVb)"),
    (3, "společenské vědy (SHVc)"),
    (4, "technické a informatické vědy"),
    (5, "zemědělské vědy (rostlinná výroba, živočišná výroba a potravinářství)"),
    (6, "vědy o Zemi"),
    (7, "matematické vědy"),
    (8, "fyzikální vědy (pouze pilíř II.)"),
    (9, "chemické vědy (pouze pilíř II.)"),
    (10, "biologické vědy (pouze pilíř II.)"),
    (11, "lékařské vědy (pouze pilíř II.)"),
]

RIV_CAT_IDS = [
    row[0]
    for row in RIV_CATEGORIES
]
