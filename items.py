# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"

class FanfictionItem(scrapy.Item):
    ID = scrapy.Field()
    ID_Rif  = scrapy.Field()
    Titolo_Rif = scrapy.Field()
    Elenco_Capitoli = scrapy.Field()
    Numero_Capitoli = scrapy.Field()
    Next_ID_List = scrapy.Field()
    Position = scrapy.Field()
    Rating = scrapy.Field()
    Nome_Autore = scrapy.Field()
    Data = scrapy.Field()
    Racconto_Text_Only = scrapy.Field()    
    N_Tot_Rec = scrapy.Field()
    N_Tot_Rec_Pos = scrapy.Field()
    N_Tot_Rec_Neg = scrapy.Field()
    This_Rec = scrapy.Field()	
    pass
