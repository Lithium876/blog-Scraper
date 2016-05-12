import requests
from xlwt import Workbook
from bs4 import BeautifulSoup

authors=[]
descriptions=[]
urlLinks=[]
title=[]
category=[]

def write(author,col1, description, col2, linkURL, col3, site, col4, category, col5):
	wb = Workbook()
	sheet1 = wb.add_sheet('Sheet 1')
	sheet1.write(0,0,"Authors/Writers")
	sheet1.write(0,1,"Description")
	sheet1.write(0,2,"Link/URL")
	sheet1.write(0,3,"Name of company/ Site")
	sheet1.write(0,4,"Category")
	sheet1.col(0).width = 6000
	sheet1.col(1).width = 20000
	sheet1.col(2).width = 20000
	sheet1.col(3).width = 6000
	sheet1.col(4).width = 6000

	for i in range(len(description)):
		sheet1.write(i+1,col1,author[i])
		sheet1.write(i+1,col2,description[i])
		sheet1.write(i+1,col3,linkURL[i])
		sheet1.write(i+1,col4,site[i])
		sheet1.write(i+1,col5,category[i])
	wb.save('IOT.xls') #Save Excel File

def crawl(item_url):
    source_code=requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    urlLinks.append(item_url)
    title.append("Blog Code")
    category.append("IOT")
    for description in soup.find_all('h1', {'class': 'entry-title'}):
    	fin_des = description.string
    	descriptions.append(fin_des) #gets blog title
    for author in soup.find_all('div', {'class': 'entry-meta'}):
    	aut=author.find('a').string
    	authors.append(aut) #gets blog author

    write(authors,0,descriptions,1, urlLinks,2,title,3,category,4)

def company_scraper(max_pages):
  page=1
  while page <= max_pages:
    url = 'http://www.yelp.com/search?find_desc=chinese+food&find_loc=San+Francisco%2C+CA&ns='+str(page)
    source_code=requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for link in soup.find_all('h1',{'class':'entry-title'}):
    	url_link=link.find('a') #get href from between header(h2) tags
    	try:
    		href=url_link.get('href')
    		crawl(href)
            print(href)
    	except:
    		pass

    page += 1

company_scraper(6) #scrape 6 pages
