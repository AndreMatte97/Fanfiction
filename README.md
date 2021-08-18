# Fanfiction
Web Crawlers for [EFPFanfic](https://efpfanfic.net/), a website containing user-generated fanfictions and original stories written in Italian. A corpus made up of fanfictions inspired by the popular fantasy saga 'Harry Potter' extracted from this portal has been analyzed in the Computational Linguistics study presented in [Mattei, Brunato, Dell'Orletta (2021)](http://ceur-ws.org/Vol-2769/paper_52.pdf).

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
6. In 'spider1.py' only, you should find a line like this: `depthHP = 3 #depth>=2`. The variable depthHP tells the spider how many stories we want to collect. Stories are ordered based on more recent update, and by default shown 15 at a time. To put it simply, spider1.py will collect the 15-times-depthHP more recently updated stories. You can go [on the website itself](https://efpfanfic.net/categories.php?catid=47&parentcatid=47&offset=0&pagina=1&ratinglist=&charlist1=&charlist2=&genrelist=&warninglist1=&warninglist2=&completelist=&capitolilist=&colloclist=&tipocoplist=&coppielist=&avvertlist1=&avvertlist2=) and scroll down to see how many pages there are and so which is the maximum value you can input for depthHP. 

## Running the spiders
1. Navigate to the 'spiders' directory in your Scrapy project folder.
2. Start by running spider1, using the command `scrapy crawl spider1 -O PadriHPv2.json`. This runs spider1.py, which collects the first chapter of each story and saves their text and some metadata about them in a .json file called 'PadriHPv2', automatically created in the same folder of the spiders. A couple of things to note: 
  * If for whatever reason you wish to rename the .py files containing the spider, remember that you'll still need to call them 'spider1' and 'spider2' when running them using `scrapy crawl`. This is because the command actually checks for the variable 'name' declared inside the Python script, and not for the filename. 
  * If you wish to give a different name to the .json file containing the output, you also need to open 'spider2.py' in a text editor, search for the line `with open('.\PadriHPv2.json') as f:` and change the name of the file there too. The reason for this will become apparent in the next point.
3. After waiting patiently for the first spider to finish crawling, you can run the second spider. This one will look in the data collected by the first one, collect the URLs of every single first chapter and use them to retrieve all the subsequent chapters of those stories. This time you can name the output file however you want, so for example: `scrapy crawl spider2 -O FigliHP.json`. Keep in mind, on average each story has 3.6 chapters, so this spider will take nearly 3 times longer to run!

## But... What did these Spiders get me?
Each entry in the json files corresponds to a chapter of a story, and contains the following information:
* ID: the number with which the website univocally identifies that particular chapter.
* ID_Rif: the ID for the first chapter of a particular story. You can use it to group together the chapters belonging to the same story.
* Titolo_Rif: the title for the first chapter of a story.
* Rating: an estimate given by the author about the crudeness and maturity of the described scenes and the dealt with themes.
* Nome_Autore: the author's nickname.
* Data: Date in which the chapter has been posted.
* **Racconto_Text_Only**: The actual text of the chapter. Due to the heavy customization on the page appearance done by most authors through HTML markup, the spiders clean the data beforehand and output a 'Text-Only version. 

* Elenco_Capitoli: a list of the IDs of all chapters beloning to that story.
* Numero_Capitoli: how many chapters does this story have.
* Next_ID_List: the ID of the next chapter in the story.
* Position: where this chapter is situated in its story.

