# Fanfiction
Web Crawlers for [EFPFanfic](https://efpfanfic.net/), a website containing user-generated fanfictions and original stories written in Italian. A corpus made up of fanfictions extracted from this portal has been analyzed in the Computational Linguistics study presented in [Mattei, Brunato, Dell'Orletta (2021)](http://ceur-ws.org/Vol-2769/paper_52.pdf).

Please remember that the distribution of the material found on that website is prohibited without the author's consent, except for short quotes. This is why we deemed appropriate to only share the spiders employed to extract this data, instead of the whole corpus.

## Requisites
* Python installed on your machine (guaranteed functionality with Python 3.6.4)
* The Python module Scrapy ([See the website of the module here](https://scrapy.org/), or simply `pip install scrapy`)
* An account on EFP: the spiders need you username and password to log in on the website. This is because stories containing mature content are hidden unless you are logged in (and have declared to be at least 18 years old). To register, go at: https://efpfanfic.net/newaccount.php

## Set-up Instructions
1. Navigate to the directory where you wish to locate the spiders.
2. Create a new Scrapy project (called 'fanfiction') with the command `scrapy startproject fanfiction`. This is going to create a folder containing all the necessary component of a functioning web crawler... except we are missing the crawlers! We are going to make up for it in the next step.
3. Download the files 'spider1.py' and 'spider2.py' from this repository and put them in the 'spiders' folder found in your project folder. 
4. Go back a level up in the folder and locate the file 'items.py'. Replace it with the one found in this repository. At this point the project folder is all setup, but the spiders still need a bit of info from us to be able to run correctly.
5. Open both 'spider1.py' and 'spider2.py' with the text editor of your choice. In both files you should locate the lines `USER_NAME = 'YourUsername'` and `USER_NAME = 'YourUsername'` inside the function named 'parse'. Change 'YourUsername' and 'YourPassword' with the credentials of your account on EFPfanfic.net.
6. In 'spider1.py' only, you should find a line like this: `depthHP = 3 #depth>=2`. The variable depthHP tells the spider how many stories we want to collect. Stories are ordered based on more recent update, and by default shown 15 at a time. To put it simply, spider1.py will collect the 15-times-depthHP more recently updated stories. You can go [on the website itself](https://efpfanfic.net/categories.php?catid=47&parentcatid=47&offset=0&pagina=1&ratinglist=&charlist1=&charlist2=&genrelist=&warninglist1=&warninglist2=&completelist=&capitolilist=&colloclist=&tipocoplist=&coppielist=&avvertlist1=&avvertlist2=) to see how many 15-story pages are there and so which is the maximum value you can input for depthHP.
