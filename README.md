# Fanfiction
Web Crawlers for [EFPFanfic](https://efpfanfic.net/), a website containing user-generated fanfictions and original stories written in Italian. A corpus made up of fanfictions extracted from this portal has been analyzed in the Computational Linguistics study presented in [Mattei, Brunato, Dell'Orletta](http://ceur-ws.org/Vol-2769/paper_52.pdf).

Please remember that the distribution of the material found on that website is prohibited without the author's consent, except for short quotes. This is why we deemed appropriate to only share the spiders employed to extract this data, instead of the whole corpus.

## Requisites
* Python installed on your machine (guaranteed functionality with Python 3.6.4)
* The Python module Scrapy ([See the website of the module here](https://scrapy.org/), or simply `pip install scrapy`)
* An account on EFP: the spiders need you username and password to log in on the website. This is because stories containing mature content are hidden unless you are logged in (and have declared to be at least 18 years old). To register, go at: https://efpfanfic.net/newaccount.php

## Instructions
1. Navigate to the directory where you wish to locate the spiders.
2. Create a new Scrapy project (called 'fanfiction') with the command `scrapy startproject fanfiction`. This is going to create a folder containing all the necessary component of a functioning web crawler... except we are missing the crawlers! We are going to make up for it in the next step.
3. Download the files 'spider1.py' and 'spider2.py' from this repository and put them in the 'spiders' folder found in your project folder. 
4. Go back a level up in the folder and locate the file 'items.py'. Replace it with the one found in this repository. 
