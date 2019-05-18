# EXCERPT
This is a training set for  who wants to learn the association between SQL with python.
You can learn from this contents how you cooperate MySQL with Python on the Jupyter Notebook!
The theme for scraping is "http://quotes.toscrape.com/" which is listed in "Pythonスクレイピングの基本と実践 データサイエンティストのためのWebデータ収集術 (impress top gear)"

# COMPONENTS DESCRIPTION 
・quotes_scraper.py: This is a main function.
・requirements.txt: This file is for creating virtualenv in which you can deploy quotes_scraper.py (I'll explain how to use it later)
・items_scraper.py: a helper funcion for "quotes_scraper.py", which inputs Beautifulsoup and outputs a quote and its author
・next_page_getter: also a helper function for "quotes_scraper.py", which enables you to crowl pages until it reaches its terminal.
・soup_from_url: also a helper function for "quotes_scraper.py", which inputs url and outputs its Beautifulsoup.
・store.py: also a helper function for "quotes_scraper.py", which inserts data into sql and commits.

# HOW TO MAKE A VIRTUALENV WITH "requirements.txt"
1.In "sql_trial" directory, make a virtualenv directory with pyvenv command.

	pyvenv sql_project

2.move into this directory.

	cd sql_project

3.activate virtualenv.

	source bin/activate

4.Now you switched into a virtualenv mode! Then you pip install what you need with "requirements.txt".

	pip install -r requirements.txt

Done!! You can check what libraries you have got with the following command.

	pip list

5.If you want to EXIT from your virtualenv mode. JUST

	deactivate        
