import requests
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_driver_path = 'C:/users/user/Desktop/data/chromedriver.exe' # chrome driver의 경로
driver = webdriver.Chrome(chrome_driver_path)
url = 'https://some.co.kr/media/home#none'
driver.get(url)

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://some.co.kr/media/home#none',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


driver.find_elements_by_xpath('//*[@id="mediaList"]/div[5]/div[2]/div/ul/li[2]/div[1]/div[3]/a')

driver.quit()