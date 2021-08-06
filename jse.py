# pip install selenium
# pip install bs4
# pip install pandas

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd


x=input('\n\n\n\t\t\t\t\t WELCOME TO JOB SEARCH ENGINE \n\n\n\t\t FIELD    :  ')
y=input('\n\t\t LOCATION :  ')

driver = webdriver.Chrome("D:\\MD\\Projects\\JSE\\chromedriver_win32\\chromedriver")
driver.get('https://www.indeed.co.in/jobs?q={fld}&l={loc}&ts=1579267502893&pts=1578979676714&rq=1&rsIdx=0&fromage=last&newcount=32'.format(fld=x,loc=y))
elements = driver.find_elements_by_class_name('result')

for i in elements:
        soup = BeautifulSoup(i.get_attribute('innerHTML'),"html.parser")

titles = []
locations = []
salarys = []
companys = []
for i in range(0,50,10):
    driver.get('https://www.indeed.co.in/jobs?q={fld}&l={loc}&fromage=last&start='.format(fld=x,loc=y)+str(i))
    elements = driver.find_elements_by_class_name('result')
    for i in elements:
        soup = BeautifulSoup(i.get_attribute('innerHTML'),"html.parser")
        try:
            t = soup.find(class_='jobTitle jobTitle-color-purple').text.replace('\n','').strip()
            titles.append(t)
        except:
            titles.append(None)
        
        try:
            location = soup.find( class_="companyLocation").text.replace("\n","").strip()
            locations.append(location)
        except:
            locations.append(None)
            
        try:
            company = soup.find(class_="companyName").text.replace("\n","").strip()
            companys.append(company)
        except:
            companys.append(None)
        
        try:
            salary = soup.find( class_="salary-snippet").text.replace("\n","").strip()
            salarys.append(salary)
        except:
            salarys.append(None)
        
            
df = pd.DataFrame({"Title":titles,"Location":locations,"Company":companys,"Salary":salarys})
df.to_csv('Job_availibility.csv')
driver.close()

print("\n\n\n\t\t\t A file containing information regarding possible jobs has been downloaded.")
