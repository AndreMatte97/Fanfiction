# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:46:58 2019

@author: Andrea
"""

# -*- coding: utf-8 -*-
import scrapy
from fanfiction.items import FanfictionItem
import re
import json



   
def authentication_failed(response):
    # TODO: Check the contents of the response and return True if it failed
    # or False if it succeeded.
    pass


class Spider1Spider(scrapy.Spider):
    name = 'spider2'
    
    allowed_domains = ["efpfanfic.net"]
    
    start_urls = ["https://efpfanfic.net/user.php"]
    
    def parse(self, response):
        #login
        USER_NAME = 'YourUsername'
        PASSWORD = 'YourPassword'
        return scrapy.FormRequest.from_response(response,
            formxpath='//form', formdata={'penname': USER_NAME,             
                'password': PASSWORD}, callback=self.afterlogin)
       

    def afterlogin(self, response):
        
        if authentication_failed(response):
            self.logger.error("Login failed")
            return
        
        START_PAGES = []
        with open('.\PadriHPv2.json') as f:
            lista_padri = json.load(f)
            
        for padre in lista_padri:
            if padre['Next_ID_List'] != []:
                for ID in padre['Next_ID_List']:
                    urlfiglio = "https://efpfanfic.net/viewstory.php?sid=" + str(ID) + "&i=1"
                    START_PAGES.append(urlfiglio)
                    
#        
        for pagina in START_PAGES:
            yield scrapy.Request(pagina, callback=self.parse_pag_racconto)
    
    
#    def parse2(self, response):
#        for href in response.xpath("//div[@class='titlestoria']/a/@href"):
#            url_parziale = href.get()
#            url = "https://efpfanfic.net/" + url_parziale
#            yield scrapy.Request(url, callback=self.parse_pag_racconto)
#        
#        
    
        
    def parse_pag_racconto(self, response):
        
        
        item = FanfictionItem()
        
        link = response.url
        
        base_ID = int(link[40:-4], 10) 
        
        #Info di Base
        #item['url'] = link       
        item['ID'] = base_ID
        
        Link_List = response.xpath("//select//option/@value").getall()
        ID_List = []
        for x in Link_List[:len(Link_List)//2]: 
            ID_List.append(int(x[18:-4]))
        
            
        
        item['ID_Rif'] = ID_List[0]
        
        
        item['Titolo_Rif'] = response.xpath("//div[@id='corpo']//div[@style='font-weight: bold; font-variant: small-caps; font-size: 1.3em;']/a/text()").get()        
        item['Rating'] = response.xpath("//div[@id='corpo']//div[@style=' padding:4px; width: 99%; vertical-align:middle;']/div/@id").get() #se "None" = Rosso!
        item['Nome_Autore'] = response.xpath("//div[@id='gen_contenitore']//a/text()").get()
        
        #Data Pubblicazione
        data_raw = response.xpath("//div[@id='gen_contenitore']/text()[4]").get()
        data_pubbl = data_raw.strip()[0:10]        
        item['Data'] = data_pubbl
        
        #Numero di capitoli: Esistono capitoli oltre al primo?
        capitoliYN = response.xpath("//select")
        if capitoliYN != []:
            capitoli = response.xpath("//select[1]//option/text()").getall()
            numero = int(len(capitoli)/2)
            item['Numero_Capitoli'] = numero-1                              
        else:  
            numero = 1
            item['Numero_Capitoli'] = 1
            
        #ListaID Capitoli Successivi: So che il racconto ha piu di un capitolo. Siamo almeno al secondo. Prendo ID del padre e posizione del corrente.
        
        
        position = ID_List.index(base_ID)
        item['Position'] = position+1
        item['Next_ID_List'] = ID_List[position+1:] 
            
            
        
        #Testo
        TextList = response.xpath("//div[@class='storia']/article//text()").getall()
        Text = ""
        Text = Text.join(TextList)
        Text = Text.strip()
        item['Racconto_Text_Only'] = re.sub(r'<![\s\S]*?>', '', Text)
        
        #Url Pagina delle Recensioni
        parziale_recensioni = response.xpath("//div[@id='gen_contenitore']//a/img[@src='images/icone/comment.png']/parent::a/@href").get()        
        url_rec = "https://efpfanfic.net/"+parziale_recensioni                
        requestRec = scrapy.Request(url_rec, callback=self.parse_pag_recensioni)
        requestRec.meta['item'] = item
        
        yield requestRec
        
#        
#        
#        
#        
    def parse_pag_recensioni(self, response):
        item = response.meta['item']
        
        Rec_Tot_Raw = response.xpath("//div[@style='text-align:left; margin: 0px 40px;']/text()[1]").get()
        Rec_Pos_Raw = response.xpath("//div[@style='text-align:left; margin: 0px 40px;']/text()[2]").get()
        #Rec_Neg_Raw = response.xpath("//div[@style='text-align:left; margin: 0px 40px;']/text()[3]").get()
                
        totale = Rec_Tot_Raw.strip()
        item['N_Tot_Rec'] = int(re.sub(r'[^0-9]+', '', totale), 10)
        item['N_Tot_Rec_Pos'] = int(Rec_Pos_Raw.strip()[11:], 10)
        item['N_Tot_Rec_Neg'] = item['N_Tot_Rec'] - item['N_Tot_Rec_Pos']
        
        
        numeropagine = len(response.xpath("//div[@class='elencopagine']//a").getall())//2
        item['This_Rec'] = (numeropagine-1)*15 #temp
        url_bottom_rec = "https://efpfanfic.net/reviews.php?sid=" + str(item['ID']) + "&a=1&offset=" + str((numeropagine-1)*15)
        request_more_rec = scrapy.Request(url_bottom_rec, callback = self.parse_more_rec)
        request_more_rec.meta['item'] = item
        yield request_more_rec
            
        
            
    def parse_more_rec(self, response):
        
        item = response.meta['item']
        
        bottom_rec_list = response.xpath("//div[@class='rec_riq_generale']").getall()
        parziale = item['This_Rec']        
        item['This_Rec'] = len(bottom_rec_list) + parziale
        if item['This_Rec'] < 0 :
            item['This_Rec'] = item['This_Rec'] + 15
        return item
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       