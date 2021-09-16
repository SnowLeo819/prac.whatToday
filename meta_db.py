import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from flask import Flask, render_template

app = Flask(__name__)

# 옵션 생성
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")

# driver 실행
driver = webdriver.Chrome("C:/Users/user/Desktop/data/chromedriver.exe", options=options)
driver.get("https://map.kakao.com/")

url = 'https://map.kakao.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


@app.route('/')
def direction():
    return render_template('main.html')


@app.route('/answer')
def result():
    direction = soup.select_one('#search\.tab3 > a').text
    return render_template('answer.html', direc = direction)



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


# driver 종료
driver.quit()