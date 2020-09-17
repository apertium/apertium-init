#!/usr/bin/env python3

__author__ = 'Sushain K. Cherivirala, Kevin Brubeck Unhammer'
__copyright__ = 'Copyright 2014--2018, Sushain K. Cherivirala, Kevin Brubeck Unhammer'
__credits__ = ['Sushain K. Cherivirala', 'Kevin Brubeck Unhammer', 'Jonathan North Washington', 'Shardul Chiplunkar']
__license__ = 'GPLv3+'
__status__ = 'Production'
__version__ = '2.3.0'

import argparse
import base64
import getpass
import json
import os
import re
import shlex
import stat
import subprocess
import sys
import urllib.request
import zlib

if False:  # for mypy
    import http.client  # noqa: F401
    from typing import Dict, List, Tuple  # noqa: F401

# DO NOT MODIFY, USE `make` which calls `./updateBoostraper.py`
any_module_files = {}  # noqa: E501
lttoolbox_language_module_files = {}  # noqa: E501
hfst_language_module_files = {}  # noqa: E501
bilingual_module_files = {}  # noqa: E501
# DO NOT MODIFY, USE `make` which calls `./updateBoostraper.py`

english_lang_names = {'aa': 'Afar', 'ab': 'Abkhazian', 'ace': 'Achinese', 'ach': 'Acoli', 'ada': 'Adangme', 'ady': 'Adyghe', 'ae': 'Avestan', 'af': 'Afrikaans', 'afh': 'Afrihili', 'agq': 'Aghem', 'ain': 'Ainu', 'ak': 'Akan', 'akk': 'Akkadian', 'ale': 'Aleut', 'alt': 'Southern Altai', 'am': 'Amharic', 'an': 'Aragonese', 'ang': 'Old English', 'anp': 'Angika', 'ar': 'Arabic', 'ar-001': 'Modern Standard Arabic', 'arc': 'Aramaic', 'arn': 'Mapuche', 'arp': 'Arapaho', 'arw': 'Arawak', 'as': 'Assamese', 'asa': 'Asu', 'ast': 'Asturian', 'av': 'Avaric', 'awa': 'Awadhi', 'ay': 'Aymara', 'az': 'Azerbaijani', 'az-alt-short': 'Azeri', 'ba': 'Bashkir', 'bal': 'Baluchi', 'ban': 'Balinese', 'bas': 'Basaa', 'bax': 'Bamun', 'bbj': 'Ghomala', 'be': 'Belarusian', 'bej': 'Beja', 'bem': 'Bemba', 'bez': 'Bena', 'bfd': 'Bafut', 'bg': 'Bulgarian', 'bho': 'Bhojpuri', 'bi': 'Bislama', 'bik': 'Bikol', 'bin': 'Bini', 'bkm': 'Kom', 'bla': 'Siksika', 'bm': 'Bambara', 'bn': 'Bengali', 'bo': 'Tibetan', 'br': 'Breton', 'bra': 'Braj', 'brx': 'Bodo', 'bs': 'Bosnian', 'bss': 'Akoose', 'bua': 'Buriat', 'bug': 'Buginese', 'bum': 'Bulu', 'byn': 'Blin', 'byv': 'Medumba', 'ca': 'Catalan', 'cad': 'Caddo', 'car': 'Carib', 'cay': 'Cayuga', 'cch': 'Atsam', 'ce': 'Chechen', 'ceb': 'Cebuano', 'cgg': 'Chiga', 'ch': 'Chamorro', 'chb': 'Chibcha', 'chg': 'Chagatai', 'chk': 'Chuukese', 'chm': 'Mari', 'chn': 'Chinook Jargon', 'cho': 'Choctaw', 'chp': 'Chipewyan', 'chr': 'Cherokee', 'chy': 'Cheyenne', 'ckb': 'Sorani Kurdish', 'co': 'Corsican', 'cop': 'Coptic', 'cr': 'Cree', 'crh': 'Crimean Turkish', 'cs': 'Czech', 'csb': 'Kashubian', 'cu': 'Church Slavic', 'cv': 'Chuvash', 'cy': 'Welsh', 'da': 'Danish', 'dak': 'Dakota', 'dar': 'Dargwa', 'dav': 'Taita', 'de': 'German', 'de-AT': 'Austrian German', 'de-CH': 'Swiss High German', 'del': 'Delaware', 'den': 'Slave', 'dgr': 'Dogrib', 'din': 'Dinka', 'dje': 'Zarma', 'doi': 'Dogri', 'dsb': 'Lower Sorbian', 'dua': 'Duala', 'dum': 'Middle Dutch', 'dv': 'Divehi', 'dyo': 'Jola-Fonyi', 'dyu': 'Dyula', 'dz': 'Dzongkha', 'dzg': 'Dazaga', 'ebu': 'Embu', 'ee': 'Ewe', 'efi': 'Efik', 'egy': 'Ancient Egyptian', 'eka': 'Ekajuk', 'el': 'Greek', 'elx': 'Elamite', 'en': 'English', 'en-AU': 'Australian English', 'en-CA': 'Canadian English', 'en-GB': 'British English', 'en-GB-alt-short': 'U.K. English', 'en-US': 'American English', 'en-US-alt-short': 'U.S. English', 'enm': 'Middle English', 'eo': 'Esperanto', 'es': 'Spanish', 'es-419': 'Latin American Spanish', 'es-ES': 'European Spanish', 'es-MX': 'Mexican Spanish', 'et': 'Estonian', 'eu': 'Basque', 'ewo': 'Ewondo', 'fa': 'Persian', 'fan': 'Fang', 'fat': 'Fanti', 'ff': 'Fulah', 'fi': 'Finnish', 'fil': 'Filipino', 'fj': 'Fijian', 'fo': 'Faroese', 'fon': 'Fon', 'fr': 'French', 'fr-CA': 'Canadian French', 'fr-CH': 'Swiss French', 'frm': 'Middle French', 'fro': 'Old French', 'frr': 'Northern Frisian', 'frs': 'Eastern Frisian', 'fur': 'Friulian', 'fy': 'Western Frisian', 'ga': 'Irish', 'gaa': 'Ga', 'gay': 'Gayo', 'gba': 'Gbaya', 'gd': 'Scottish Gaelic', 'gez': 'Geez', 'gil': 'Gilbertese', 'gl': 'Galician', 'gmh': 'Middle High German', 'gn': 'Guarani', 'goh': 'Old High German', 'gon': 'Gondi', 'gor': 'Gorontalo', 'got': 'Gothic', 'grb': 'Grebo', 'grc': 'Ancient Greek', 'gsw': 'Swiss German', 'gu': 'Gujarati', 'guz': 'Gusii', 'gv': 'Manx', 'gwi': 'Gwichʼin', 'ha': 'Hausa', 'hai': 'Haida', 'haw': 'Hawaiian', 'he': 'Hebrew', 'hi': 'Hindi', 'hil': 'Hiligaynon', 'hit': 'Hittite', 'hmn': 'Hmong', 'ho': 'Hiri Motu', 'hr': 'Croatian', 'hsb': 'Upper Sorbian', 'ht': 'Haitian', 'hu': 'Hungarian', 'hup': 'Hupa', 'hy': 'Armenian', 'hz': 'Herero', 'ia': 'Interlingua', 'iba': 'Iban', 'ibb': 'Ibibio', 'id': 'Indonesian', 'ie': 'Interlingue', 'ig': 'Igbo', 'ii': 'Sichuan Yi', 'ik': 'Inupiaq', 'ilo': 'Iloko', 'inh': 'Ingush', 'io': 'Ido', 'is': 'Icelandic', 'it': 'Italian', 'iu': 'Inuktitut', 'ja': 'Japanese', 'jbo': 'Lojban', 'jgo': 'Ngomba', 'jmc': 'Machame', 'jpr': 'Judeo-Persian', 'jrb': 'Judeo-Arabic', 'jv': 'Javanese', 'ka': 'Georgian', 'kaa': 'Kara-Kalpak', 'kab': 'Kabyle', 'kac': 'Kachin', 'kaj': 'Jju', 'kam': 'Kamba', 'kaw': 'Kawi', 'kbd': 'Kabardian', 'kbl': 'Kanembu', 'kcg': 'Tyap', 'kde': 'Makonde', 'kea': 'Kabuverdianu', 'kfo': 'Koro', 'kg': 'Kongo', 'kha': 'Khasi', 'kho': 'Khotanese', 'khq': 'Koyra Chiini', 'ki': 'Kikuyu', 'kj': 'Kuanyama', 'kk': 'Kazakh', 'kkj': 'Kako', 'kl': 'Kalaallisut', 'kln': 'Kalenjin', 'km': 'Khmer', 'kmb': 'Kimbundu', 'kn': 'Kannada', 'ko': 'Korean', 'kok': 'Konkani', 'kos': 'Kosraean', 'kpe': 'Kpelle', 'kr': 'Kanuri', 'krc': 'Karachay-Balkar', 'krl': 'Karelian', 'kru': 'Kurukh', 'ks': 'Kashmiri', 'ksb': 'Shambala', 'ksf': 'Bafia', 'ksh': 'Colognian', 'ku': 'Kurdish', 'kum': 'Kumyk', 'kut': 'Kutenai', 'kv': 'Komi', 'kw': 'Cornish', 'ky': 'Kyrgyz', 'ky-alt-variant': 'Kirghiz', 'la': 'Latin', 'lad': 'Ladino', 'lag': 'Langi', 'lah': 'Lahnda', 'lam': 'Lamba', 'lb': 'Luxembourgish', 'lez': 'Lezghian', 'lg': 'Ganda', 'li': 'Limburgish', 'lkt': 'Lakota', 'ln': 'Lingala', 'lo': 'Lao', 'lol': 'Mongo', 'loz': 'Lozi', 'lt': 'Lithuanian', 'lu': 'Luba-Katanga', 'lua': 'Luba-Lulua', 'lui': 'Luiseno', 'lun': 'Lunda', 'luo': 'Luo', 'lus': 'Mizo', 'luy': 'Luyia', 'lv': 'Latvian', 'mad': 'Madurese', 'maf': 'Mafa', 'mag': 'Magahi', 'mai': 'Maithili', 'mak': 'Makasar', 'man': 'Mandingo', 'mas': 'Masai', 'mde': 'Maba', 'mdf': 'Moksha', 'mdr': 'Mandar', 'men': 'Mende', 'mer': 'Meru', 'mfe': 'Morisyen', 'mg': 'Malagasy', 'mga': 'Middle Irish', 'mgh': 'Makhuwa-Meetto', 'mgo': 'Meta\'', 'mh': 'Marshallese', 'mi': 'Maori', 'mic': 'Micmac', 'min': 'Minangkabau', 'mk': 'Macedonian', 'ml': 'Malayalam', 'mn': 'Mongolian', 'mnc': 'Manchu', 'mni': 'Manipuri', 'moh': 'Mohawk', 'mos': 'Mossi', 'mr': 'Marathi', 'ms': 'Malay', 'mt': 'Maltese', 'mua': 'Mundang', 'mul': 'Multiple Languages', 'mus': 'Creek', 'mwl': 'Mirandese', 'mwr': 'Marwari', 'my': 'Burmese', 'mye': 'Myene', 'myv': 'Erzya', 'na': 'Nauru', 'nap': 'Neapolitan', 'naq': 'Nama', 'nb': 'Norwegian Bokmål', 'nd': 'North Ndebele', 'nds': 'Low German', 'ne': 'Nepali', 'new': 'Newari', 'ng': 'Ndonga', 'nia': 'Nias', 'niu': 'Niuean', 'nl': 'Dutch', 'nl-BE': 'Flemish', 'nmg': 'Kwasio', 'nn': 'Norwegian Nynorsk', 'nnh': 'Ngiemboon', 'no': 'Norwegian', 'nog': 'Nogai', 'non': 'Old Norse', 'nqo': 'N’Ko', 'nr': 'South Ndebele', 'nso': 'Northern Sotho', 'nus': 'Nuer', 'nv': 'Navajo', 'nwc': 'Classical Newari', 'ny': 'Nyanja', 'nym': 'Nyamwezi', 'nyn': 'Nyankole', 'nyo': 'Nyoro', 'nzi': 'Nzima', 'oc': 'Occitan', 'oj': 'Ojibwa', 'om': 'Oromo', 'or': 'Oriya', 'os': 'Ossetic', 'osa': 'Osage', 'ota': 'Ottoman Turkish', 'pa': 'Punjabi', 'pag': 'Pangasinan', 'pal': 'Pahlavi', 'pam': 'Pampanga', 'pap': 'Papiamento', 'pau': 'Palauan', 'peo': 'Old Persian', 'pes': 'Iranian Persian', 'phn': 'Phoenician', 'pi': 'Pali', 'pl': 'Polish', 'pon': 'Pohnpeian', 'pro': 'Old Provençal', 'ps': 'Pashto', 'ps-alt-variant': 'Pushto', 'pt': 'Portuguese', 'pt-BR': 'Brazilian Portuguese', 'pt-PT': 'European Portuguese', 'qu': 'Quechua', 'raj': 'Rajasthani', 'rap': 'Rapanui', 'rar': 'Rarotongan', 'rm': 'Romansh', 'rn': 'Rundi', 'ro': 'Romanian', 'ro-MD': 'Moldavian', 'rof': 'Rombo', 'rom': 'Romany', 'root': 'Root', 'ru': 'Russian', 'rup': 'Aromanian', 'rw': 'Kinyarwanda', 'rwk': 'Rwa', 'sa': 'Sanskrit', 'sad': 'Sandawe', 'sah': 'Sakha', 'sam': 'Samaritan Aramaic', 'saq': 'Samburu', 'sas': 'Sasak', 'sat': 'Santali', 'sba': 'Ngambay', 'sbp': 'Sangu', 'sc': 'Sardinian', 'scn': 'Sicilian', 'sco': 'Scots', 'sd': 'Sindhi', 'se': 'Northern Sami', 'see': 'Seneca', 'seh': 'Sena', 'sel': 'Selkup', 'ses': 'Koyraboro Senni', 'sg': 'Sango', 'sga': 'Old Irish', 'sh': 'Serbo-Croatian', 'shi': 'Tachelhit', 'shn': 'Shan', 'shu': 'Chadian Arabic', 'si': 'Sinhala', 'sid': 'Sidamo', 'sk': 'Slovak', 'sl': 'Slovenian', 'sm': 'Samoan', 'sma': 'Southern Sami', 'smj': 'Lule Sami', 'smn': 'Inari Sami', 'sms': 'Skolt Sami', 'sn': 'Shona', 'snk': 'Soninke', 'so': 'Somali', 'sog': 'Sogdien', 'sq': 'Albanian', 'sr': 'Serbian', 'srn': 'Sranan Tongo', 'srr': 'Serer', 'ss': 'Swati', 'ssy': 'Saho', 'st': 'Southern Sotho', 'su': 'Sundanese', 'suk': 'Sukuma', 'sus': 'Susu', 'sux': 'Sumerian', 'sv': 'Swedish', 'sw': 'Swahili', 'swb': 'Comorian', 'swc': 'Congo Swahili', 'syc': 'Classical Syriac', 'syr': 'Syriac', 'ta': 'Tamil', 'te': 'Telugu', 'tem': 'Timne', 'teo': 'Teso', 'ter': 'Tereno', 'tet': 'Tetum', 'tg': 'Tajik', 'th': 'Thai', 'ti': 'Tigrinya', 'tig': 'Tigre', 'tiv': 'Tiv', 'tk': 'Turkmen', 'tkl': 'Tokelau', 'tl': 'Tagalog', 'tlh': 'Klingon', 'tli': 'Tlingit', 'tmh': 'Tamashek', 'tn': 'Tswana', 'to': 'Tongan', 'tog': 'Nyasa Tonga', 'tpi': 'Tok Pisin', 'tr': 'Turkish', 'trv': 'Taroko', 'ts': 'Tsonga', 'tsi': 'Tsimshian', 'tt': 'Tatar', 'tum': 'Tumbuka', 'tvl': 'Tuvalu', 'tw': 'Twi', 'twq': 'Tasawaq', 'ty': 'Tahitian', 'tyv': 'Tuvinian', 'tzm': 'Central Atlas Tamazight', 'udm': 'Udmurt', 'ug': 'Uyghur', 'ug-alt-variant': 'Uighur', 'uga': 'Ugaritic', 'uk': 'Ukrainian', 'umb': 'Umbundu', 'und': 'Unknown Language', 'ur': 'Urdu', 'uz': 'Uzbek', 'vai': 'Vai', 've': 'Venda', 'vi': 'Vietnamese', 'vo': 'Volapük', 'vot': 'Votic', 'vun': 'Vunjo', 'wa': 'Walloon', 'wae': 'Walser', 'wal': 'Wolaytta', 'war': 'Waray', 'was': 'Washo', 'wo': 'Wolof', 'xal': 'Kalmyk', 'xh': 'Xhosa', 'xog': 'Soga', 'yao': 'Yao', 'yap': 'Yapese', 'yav': 'Yangben', 'ybb': 'Yemba', 'yi': 'Yiddish', 'yo': 'Yoruba', 'yue': 'Cantonese', 'za': 'Zhuang', 'zap': 'Zapotec', 'zbl': 'Blissymbols', 'zen': 'Zenaga', 'zgh': 'Standard Moroccan Tamazight', 'zh': 'Chinese', 'zh-Hans': 'Simplified Chinese', 'zh-Hant': 'Traditional Chinese', 'zu': 'Zulu', 'zun': 'Zuni', 'zxx': 'No linguistic content', 'zza': 'Zaza'}  # noqa: E501
iso639_codes = {'roh': 'rm', 'gv': 'glv', 'gu': 'guj', 'ron': 'ro', 'oss': 'os', 'gd': 'gla', 'nld': 'nl', 'ga': 'gle', 'se': 'sme', 'gl': 'glg', 'oji': 'oj', 'oci': 'oc', 'ty': 'tah', 'jav': 'jv', 'tw': 'twi', 'tt': 'tat', 'hrv': 'hr', 'tr': 'tur', 'ts': 'tso', 'tn': 'tsn', 'to': 'ton', 'tl': 'tgl', 'tk': 'tuk', 'th': 'tha', 'ti': 'tir', 'ven': 've', 'tg': 'tgk', 'te': 'tel', 'ta': 'tam', 'fas': 'fa', 'ssw': 'ss', 'de': 'deu', 'da': 'dan', 'ay': 'aym', 'dz': 'dzo', 'fao': 'fo', 'dv': 'div', 'rn': 'run', 'hin': 'hi', 'qu': 'que', 'hye': 'hy', 'guj': 'gu', 'kua': 'kj', 'cre': 'cr', 'div': 'dv', 'bam': 'bm', 'bak': 'ba', 'tel': 'te', 'mi': 'mri', 'za': 'zha', 'mh': 'mah', 'ara': 'ar', 'ce': 'che', 'nbl': 'nr', 'zu': 'zul', 'wa': 'wln', 'sun': 'su', 'abk': 'ab', 'kur': 'ku', 'wol': 'wo', 'lub': 'lu', 'gn': 'grn', 'lug': 'lg', 'jv': 'jav', 'nep': 'ne', 'ms': 'msa', 'iku': 'iu', 'lg': 'lug', 'wo': 'wol', 'tur': 'tr', 'mr': 'mar', 'tuk': 'tk', 'ja': 'jpn', 'cos': 'co', 'ile': 'ie', 'gla': 'gd', 'bos': 'bs', 'gle': 'ga', 'glg': 'gl', 'aka': 'ak', 'bod': 'bo', 'glv': 'gv', 'aa': 'aar', 'ch': 'cha', 'co': 'cos', 'vie': 'vi', 'ipk': 'ik', 'ca': 'cat', 'bs': 'bos', 'por': 'pt', 'uzb': 'uz', 'na': 'nau', 'pol': 'pl', 'cs': 'ces', 'tgk': 'tg', 'bre': 'br', 'cv': 'chv', 'tgl': 'tl', 'aym': 'ay', 'cha': 'ch', 'fra': 'fr', 'che': 'ce', 'pt': 'por', 'swa': 'sw', 'twi': 'tw', 'swe': 'sv', 'pa': 'pan', 'chu': 'cu', 'chv': 'cv', 'vi': 'vie', 'fry': 'fy', 'pi': 'pli', 'msa': 'ms', 'am': 'amh', 'hmo': 'ho', 'iii': 'ii', 'ml': 'mal', 'mg': 'mlg', 'mlg': 'mg', 'ibo': 'ig', 'hat': 'ht', 'slv': 'sl', 'mn': 'mon', 'xho': 'xh', 'deu': 'de', 'mk': 'mkd', 'cat': 'ca', 'mt': 'mlt', 'mlt': 'mt', 'slk': 'sk', 'ful': 'ff', 'my': 'mya', 'tat': 'tt', 've': 'ven', 'jpn': 'ja', 'vol': 'vo', 'oc': 'oci', 'is': 'isl', 'iu': 'iku', 'it': 'ita', 'vo': 'vol', 'ii': 'iii', 'mya': 'my', 'ik': 'ipk', 'io': 'ido', 'spa': 'es', 'ia': 'ina', 'ave': 'ae', 'tah': 'ty', 'ava': 'av', 'ig': 'ibo', 'yo': 'yor', 'eng': 'en', 'ie': 'ile', 'ewe': 'ee', 'id': 'ind', 'nya': 'ny', 'sin': 'si', 'pan': 'pa', 'snd': 'sd', 'mar': 'mr', 'sna': 'sn', 'kir': 'ky', 'kik': 'ki', 'fa': 'fas', 'kin': 'rw', 'ff': 'ful', 'lat': 'la', 'mah': 'mh', 'lav': 'lv', 'mal': 'ml', 'fo': 'fao', 'ss': 'ssw', 'sr': 'srp', 'sq': 'sqi', 'sw': 'swa', 'sv': 'swe', 'su': 'sun', 'st': 'sot', 'sk': 'slk', 'epo': 'eo', 'si': 'sin', 'so': 'som', 'sn': 'sna', 'sm': 'smo', 'sl': 'slv', 'sc': 'srd', 'sa': 'san', 'ido': 'io', 'sg': 'sag', 'nb': 'nob', 'tha': 'th', 'sd': 'snd', 'ita': 'it', 'tsn': 'tn', 'tso': 'ts', 'lb': 'ltz', 'ell': 'el', 'la': 'lat', 'ln': 'lin', 'lo': 'lao', 'li': 'lim', 'lv': 'lav', 'lt': 'lit', 'lu': 'lub', 'fij': 'fj', 'fin': 'fi', 'hau': 'ha', 'eus': 'eu', 'yi': 'yid', 'amh': 'am', 'bih': 'bh', 'dan': 'da', 'nob': 'nb', 'ces': 'cs', 'mon': 'mn', 'bis': 'bi', 'nor': 'no', 'cy': 'cym', 'afr': 'af', 'el': 'ell', 'eo': 'epo', 'en': 'eng', 'ee': 'ewe', 'fr': 'fra', 'lao': 'lo', 'cr': 'cre', 'eu': 'eus', 'et': 'est', 'es': 'spa', 'ru': 'rus', 'est': 'et', 'smo': 'sm', 'cu': 'chu', 'fy': 'fry', 'rm': 'roh', 'sme': 'se', 'ro': 'ron', 'be': 'bel', 'bg': 'bul', 'run': 'rn', 'ba': 'bak', 'ps': 'pus', 'bm': 'bam', 'bn': 'ben', 'bo': 'bod', 'bh': 'bih', 'bi': 'bis', 'orm': 'om', 'que': 'qu', 'br': 'bre', 'ori': 'or', 'rus': 'ru', 'pli': 'pi', 'pus': 'ps', 'om': 'orm', 'oj': 'oji', 'srd': 'sc', 'ltz': 'lb', 'nde': 'nd', 'dzo': 'dz', 'ndo': 'ng', 'srp': 'sr', 'wln': 'wa', 'isl': 'is', 'os': 'oss', 'or': 'ori', 'zul': 'zu', 'xh': 'xho', 'som': 'so', 'sot': 'st', 'fi': 'fin', 'zh': 'zho', 'fj': 'fij', 'yid': 'yi', 'mkd': 'mk', 'kom': 'kv', 'her': 'hz', 'kon': 'kg', 'ukr': 'uk', 'ton': 'to', 'heb': 'he', 'kor': 'ko', 'hz': 'her', 'hy': 'hye', 'hr': 'hrv', 'hun': 'hu', 'ht': 'hat', 'hu': 'hun', 'hi': 'hin', 'ho': 'hmo', 'bul': 'bg', 'ha': 'hau', 'cym': 'cy', 'he': 'heb', 'ben': 'bn', 'bel': 'be', 'uz': 'uzb', 'azb': 'az', 'aze': 'az', 'ur': 'urd', 'zha': 'za', 'pl': 'pol', 'uk': 'ukr', 'aar': 'aa', 'ug': 'uig', 'zho': 'zh', 'nno': 'nn', 'ab': 'abk', 'ae': 'ave', 'san': 'sa', 'uig': 'ug', 'af': 'afr', 'ak': 'aka', 'arg': 'an', 'sag': 'sg', 'an': 'arg', 'as': 'asm', 'ar': 'ara', 'khm': 'km', 'av': 'ava', 'ind': 'id', 'az': 'aze', 'ina': 'ia', 'asm': 'as', 'nl': 'nld', 'nn': 'nno', 'no': 'nor', 'lim': 'li', 'lin': 'ln', 'nd': 'nde', 'ne': 'nep', 'tir': 'ti', 'ng': 'ndo', 'lit': 'lt', 'ny': 'nya', 'nav': 'nv', 'nau': 'na', 'grn': 'gn', 'nr': 'nbl', 'yor': 'yo', 'nv': 'nav', 'kv': 'kom', 'tam': 'ta', 'cor': 'kw', 'kan': 'kn', 'kal': 'kl', 'kas': 'ks', 'sqi': 'sq', 'rw': 'kin', 'kau': 'kr', 'kat': 'ka', 'kaz': 'kk', 'urd': 'ur', 'ka': 'kat', 'kg': 'kon', 'kk': 'kaz', 'kj': 'kua', 'ki': 'kik', 'ko': 'kor', 'kn': 'kan', 'km': 'khm', 'kl': 'kal', 'ks': 'kas', 'kr': 'kau', 'kw': 'cor', 'mri': 'mi', 'ku': 'kur', 'ky': 'kir', 'hbs': 'sh', 'sh': 'hbs'}  # noqa: E501
organization_name = 'apertium'
default_prefix = 'apertium'
default_email = 'apertium-stuff@lists.sourceforge.net'


def get_lang_name(code):  # type: (str) -> str
    code = iso639_codes[code] if len(code) > 2 and code in iso639_codes else code
    if code in english_lang_names:
        return english_lang_names[code]
    else:
        sys.stdout.write('Unable to find English language name for %s, using ISO code instead.\n' % code)
        return code


def init_pair(args, email):  # type: (argparse.Namespace, str) -> Tuple[Dict[str, bytes], Dict[str, str], List[str]]
    language_code_1, language_code_2 = args.name.split('-')
    replacements = {
        'languageCode1': language_code_1,
        'languageCode2': language_code_2,
        'languageName1': get_lang_name(language_code_1),
        'languageName2': get_lang_name(language_code_2),
        'email': email,
    }

    if args.analyser == 'hfst' or (args.analyser1 == 'hfst' and args.analyser2 == 'hfst'):
        conditionals = ['hfst', 'hfst1', 'hfst2']
    elif args.analyser1 == 'hfst' and args.analyser2 in ['lt', 'lttoolbox']:
        conditionals = ['hfst', 'hfst1', 'lttoolbox2']
    elif args.analyser1 in ['lt', 'lttoolbox'] and args.analyser2 == 'hfst':
        conditionals = ['hfst', 'lttoolbox1', 'hfst2']
    else:
        conditionals = ['lttoolbox1', 'lttoolbox2']

    if not args.no_prob1:
        conditionals.append('prob1')
    if not args.no_prob2:
        conditionals.append('prob2')

    if not args.no_rlx1:
        conditionals.append('rlx1')
    if not args.no_rlx2:
        conditionals.append('rlx2')

    if not args.no_pgen1:
        conditionals.append('pgen1')
    if not args.no_pgen2:
        conditionals.append('pgen2')

    files = dict(bilingual_module_files, **any_module_files)

    if args.with_lsx:
        conditionals.append('lsx')
    else:
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.lsx']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.lsx']

    if args.with_anaphora:
        conditionals.append('anaphora')
    else:
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.arx']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.arx']

    if args.transfer == 'chunk':
        conditionals.append('chunk')
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.rtx']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.rtx']
    else:
        conditionals.append('rtx')
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t1x']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t2x']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode1}}-{{languageCode2}}.t3x']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t1x']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t2x']
        del files['apertium-{{languageCode1}}-{{languageCode2}}.{{languageCode2}}-{{languageCode1}}.t3x']

    return files, replacements, conditionals


def init_lang_module(args, email):  # type: (argparse.Namespace, str) -> Tuple[Dict[str, bytes], Dict[str, str], List[str]]
    replacements = {
        'languageCode': args.name,
        'languageName': get_lang_name(args.name),
        'email': email,
    }

    conditionals = []

    if args.analyser in ['lt', 'lttoolbox']:
        files = dict(lttoolbox_language_module_files, **any_module_files)
    elif args.analyser == 'hfst':
        files = dict(hfst_language_module_files, **any_module_files)
        if args.with_twoc:
            conditionals.append('twoc')
        else:
            del files['apertium-{{languageCode}}.{{languageCode}}.twoc']
        if args.with_spellrelax:
            conditionals.append('spellrelax')
        else:
            del files['apertium-{{languageCode}}.{{languageCode}}.spellrelax']
    else:
        raise Exception('Unrecognized analyser: ' % args.analyser)

    return files, replacements, conditionals


def make_replacements(s, replacements, conditionals):  # type: (str, Dict[str, str], List[str]) -> str
    for _ in range(2):
        s = re.sub(r'{{if_(\w+)[^\n]*(.*?)\nif_\1}}', lambda x: x.group(2) if x.group(1) in conditionals else '', s, flags=re.DOTALL)
        s = re.sub(r'{{ifnot_(\w+)[^\n]*(.*?)\nifnot_\1}}', lambda x: x.group(2) if x.group(1) not in conditionals else '', s, flags=re.DOTALL)
    for replacement_name, replacement_value in replacements.items():
        s = s.replace('{{%s}}' % replacement_name, replacement_value)
    return s


def make_all_replacements(destination, files, replacements, conditionals):  # type: (str, Dict[str, bytes], Dict[str, str], List[str]) -> None
    for filename, encoded_file in files.items():
        replacements_filename = make_replacements(filename, replacements, conditionals)
        path = os.path.join(destination, replacements_filename)
        folder = os.path.dirname(path)
        if not os.path.isdir(folder):
            os.mkdir(folder)
        if os.path.exists(path):
            backup = os.path.join(folder, '.bak')
            if not os.path.isdir(backup):
                os.mkdir(backup)
            os.rename(path, os.path.join(backup, replacements_filename))
        with open(path, 'wb') as f:
            decomp = zlib.decompress(base64.b85decode(encoded_file))
            try:
                f.write(make_replacements(str(decomp, encoding='utf-8'), replacements, conditionals).encode('utf-8'))
            except UnicodeDecodeError:  # binary file
                f.write(decomp)


def push_to_github(args, folder, username):  # type: (argparse.Namespace, str, str) -> None
    remote_name = 'origin'
    repository_name = '{}-{}'.format(args.prefix, args.name)
    if '-' in args.name:
        code1, code2 = args.name.split('-')
        description = 'Apertium translation pair for {} and {}'.format(get_lang_name(code1), get_lang_name(code2))
    else:
        description = 'Apertium linguistic data for {}'.format(get_lang_name(args.name))

    def create_github_repository():  # type: () -> http.client.HTTPResponse
        password = getpass.getpass(prompt='GitHub Password ({}): '.format(username))
        data = bytes(json.dumps({
            'name': repository_name,
            'description': description,
        }), encoding='utf-8')
        req = urllib.request.Request('https://api.github.com/orgs/{}/repos'.format(organization_name), data=data)
        credentials = '{}:{}'.format(username, password)
        encoded_credentials = base64.b64encode(credentials.encode('ascii'))
        req.add_header('Authorization', 'Basic {}'.format(encoded_credentials.decode('ascii')))
        try:
            response = urllib.request.urlopen(req)
            print('Successfully created GitHub repository {}/{}.'.format(organization_name, repository_name))
            return response  # type: ignore
        except urllib.error.HTTPError as e:  # type: ignore
            if e.getcode() == 401:
                print('Authentication failed. Retrying...')
                return create_github_repository()
            else:
                sys.stderr.write('Failed to create GitHub repository: {}.'.format(e))
                sys.exit(-1)

    response = create_github_repository()
    body = json.loads(response.read().decode('utf-8'))

    try:
        remote_url = body['ssh_url']
        subprocess.check_output(shlex.split('git remote add {} {}'.format(remote_name, remote_url)), cwd=args.destination, stderr=subprocess.STDOUT)
        print('Added GitHub remote {}.'.format(remote_url))
    except subprocess.CalledProcessError as e:
        sys.stderr.write('Adding remote {} ({}) failed: {}'.format(remote_name, remote_url, e.output))

    try:
        subprocess.check_output(shlex.split('git push {} master'.format(remote_name)), cwd=args.destination, stderr=subprocess.STDOUT)
        print('Pushed to GitHub. Visit your new repository at {}.'.format(body['html_url']))
    except subprocess.CalledProcessError as e:
        sys.stderr.write('Pushing to remote {} failed: {}'.format(remote_name, e.output))


def main(cli_args):  # type: (List[str]) -> None
    parser = argparse.ArgumentParser(description='Bootstrap an Apertium language module/pair')
    parser.add_argument('name', help='name of new Apertium language module/pair using ISO-639-3 language code(s)')
    parser.add_argument('-d', '--destination', help='destination directory for new language module/pair (default: cwd)', default=os.getcwd())
    parser.add_argument('-p', '--push-new-to-github', help='push newly created repository to incubator on the Apertium organisation on GitHub (use with -u)',
                        action='store_true', default=False)
    parser.add_argument('-pe', '--push-existing-to-github', help='push existing repository to incubator on the Apertium organisation on GitHub', default=None)
    parser.add_argument('-u', '--username', help='override GitHub username (for pushing repository to GitHub); otherwise git config is used', default=None)
    parser.add_argument('--prefix', help='directory prefix (default: {})'.format(default_prefix), default=default_prefix)
    parser.add_argument('-r', '--rebuild', help='construct module or pair with different features using existing files',
                        action='store_true', default=False)

    parser.add_argument('-a', '--analyser', help='analyser to use for all languages', choices=['lt', 'lttoolbox', 'hfst'], default='lt')
    parser.add_argument('-a1', '--analyser1', help='analyser to use for first language of pair', choices=['lt', 'lttoolbox', 'hfst'], default='lt')
    parser.add_argument('-a2', '--analyser2', help='analyser to use for second language of pair', choices=['lt', 'lttoolbox', 'hfst'], default='lt')

    parser.add_argument('-t', '--transfer', help='structural transfer module to use', choices=['chunk', 'rtx'], default='chunk')

    rlx_prob_group1 = parser.add_mutually_exclusive_group()
    rlx_prob_group1.add_argument('--no-rlx1', help='no .rlx present in first language of pair (only used for bilingual pairs)',
                                 action='store_true', default=False)
    rlx_prob_group1.add_argument('--no-prob1', help='no .prob present in first language of pair (only used for bilingual pairs)',
                                 action='store_true', default=False)

    rlx_prob_group2 = parser.add_mutually_exclusive_group()
    rlx_prob_group2.add_argument('--no-prob2', help='no .prob present in second language of pair (only used for bilingual pairs)',
                                 action='store_true', default=False)
    rlx_prob_group2.add_argument('--no-rlx2', help='no .rlx present in second language of pair (only used for bilingual pairs)',
                                 action='store_true', default=False)

    parser.add_argument('--no-pgen1', help='no post-dix present in first language of pair (only used for bilingual pairs)', action='store_true', default=False)
    parser.add_argument('--no-pgen2', help='no post-dix present in second language of pair (only used for bilingual pairs)', action='store_true', default=False)
    parser.add_argument('--with-twoc', help='include .twoc file (only used for monolingual hfst modules)', action='store_true', default=False)
    parser.add_argument('--with-lsx', help='include apertium-separable .lsx files (only used for bilingual pairs)', action='store_true', default=False)
    parser.add_argument('--with-spellrelax', help='include spellrelax file (only used for monolingual hfst modules)', action='store_true', default=False)
    parser.add_argument('--with-anaphora', help='include anaphora resolution file (only used for bilingual pairs)', action='store_true', default=False)

    args = parser.parse_args(cli_args)

    if args.analyser in ['lt', 'lttoolbox'] and args.with_twoc:
        parser.error('--with-twoc can only be used in hfst modules')
    if args.analyser in ['lt', 'lttoolbox'] and args.with_spellrelax:
        parser.error('--with-spellrelax can only be used in hfst modules')

    try:
        email = subprocess.check_output(shlex.split('git config user.email')).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        email = default_email
        sys.stderr.write('Unable to get email, defaulting to %s: %s\n' % (email, str(e).strip()))

    username = args.username or email
    args.name = re.sub(r'^{}-'.format(re.escape(args.prefix)), '', args.name)
    repository_name = '{}-{}'.format(args.prefix, args.name)
    args.destination = os.path.join(args.destination, repository_name)

    if args.push_existing_to_github:
        if not os.path.isdir(args.push_existing_to_github):
            parser.error('--push_existing_to_github requires an existing directory')
        push_to_github(args, args.destination, username)
        return

    if '-' in args.name and args.name.count('-') == 1:
        files, replacements, conditionals = init_pair(args, email)
    elif '-' not in args.name:
        files, replacements, conditionals = init_lang_module(args, email)
    else:
        parser.error('Invalid language module name: %s' % args.name)

    if args.rebuild:
        if not os.path.exists(args.destination):
            sys.stderr.write('Directory {} does not exist, cannot rebuild, quitting.\n'.format(args.destination))
            sys.exit(-1)
        files_to_delete = []
        for filename in files:
            if filename in ['README', 'modes.xml', 'autogen.sh', 'configure.ac', 'Makefile.am']:
                continue
            if filename.endswith('.pc.in'):
                continue
            fname = make_replacements(filename, replacements, conditionals)
            if os.path.exists(os.path.join(args.destination, fname)):
                files_to_delete.append(filename)
        for filename in files_to_delete:
            del files[filename]
    elif os.path.exists(args.destination):
        sys.stderr.write('Directory {} already exists, quitting.\n'.format(args.destination))
        sys.exit(-1)
    else:
        os.makedirs(args.destination)

    make_all_replacements(args.destination, files, replacements, conditionals)

    autogen_path = os.path.join(args.destination, 'autogen.sh')
    os.chmod(autogen_path, os.stat(autogen_path).st_mode | stat.S_IEXEC)

    try:
        readme_path = os.path.join(args.destination, 'README')
        if args.rebuild:
            readme_md_path = os.path.join(args.destination, 'README.md')
            if os.path.exists(readme_md_path):
                os.remove(readme_md_path)
        if os.path.exists(readme_path):
            os.symlink('README', os.path.join(args.destination, 'README.md'))
    except OSError as err:  # e.g. on Windows without running as an admin
        sys.stderr.write('Unable to create symlink from README.md -> README: {}\n'.format(err))

    print('Successfully created %s.' % args.destination)

    try:
        subprocess.check_output(shlex.split('git init .'), cwd=args.destination, universal_newlines=True, stderr=subprocess.STDOUT)
        print('Initialized git repository {}.'.format(repository_name))
    except subprocess.CalledProcessError as e:
        sys.stderr.write('Unable to initialize git repository: {}'.format(e.output))
        sys.exit(-1)

    try:
        subprocess.check_output(shlex.split('git add .'), cwd=args.destination, universal_newlines=True, stderr=subprocess.STDOUT)
        msg = 'Rebuild with apertium-init' if args.rebuild else 'Initial commit'
        subprocess.check_output(shlex.split('git commit -m "{}"'.format(msg)), cwd=args.destination, universal_newlines=True, stderr=subprocess.STDOUT)
        print('Successfully added and committed files to git repository {}.'.format(repository_name))
    except subprocess.CalledProcessError as e:
        sys.stderr.write('Unable to add/commit files to git repository {}: {}'.format(repository_name, e.output))
        sys.exit(-1)

    if args.push_new_to_github:
        push_to_github(args, args.destination, username)
    else:
        print('To push your new local repository to incubator in the {} organisation on GitHub:'.format(organization_name))
        print('\tapertium-init.py -pe {} {}'.format(args.destination, repository_name))


if __name__ == '__main__':
    main(sys.argv[1:])
