from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup 
import requests
import time 

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
#driver = webdriver.Firefox(executable_path = '/home/mr/Downloads/geckodriver')
url = "https://bugcrowd.com/user/sign_in"
driver.get(url);

driver.find_element_by_id("user_email").send_keys("lilim19690@1092df.com")
driver.find_element_by_id("user_password").send_keys("t.M@2020TEST")
driver.find_element_by_name("commit").click()

time.sleep(4)
url2 = "https://bugcrowd.com/programs"
driver.get(url2);
'''for i in range(3):
	time.sleep(5);
	driver.find_element_by_class_name("rp-program-list__load-more__btn").click()'''
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

companies_href = [i['href'] for i in soup.find_all('a',{"class":"bc-program-card__logo-backdrop"})]

companies_urls = []
length = len(companies_href) 
for i in range(0,length):
	companies_urls.append("https://bugcrowd.com"+companies_href[i]) 
#print(companies_urls)

for i in range(len(companies_urls)):
	if(i==2):
		continue;
	else:
		time.sleep(4)
		driver.get(companies_urls[i])
		content = driver.page_source
		soup = BeautifulSoup(content, 'html.parser')
		inscope_domains = [i for i in soup.find_all('code')]
		print(inscope_domains)
	
