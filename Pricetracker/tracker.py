import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Call-Duty-Modern-Warfare-PS4/dp/B07SPWYF9L/ref=sr_1_1?crid=3RMVAHXZNXTPN&keywords=call+of+duty+modern+warfare+ps4&qid=1573999412&sprefix=call+of+duty%2Caps%2C274&sr=8-1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price =float(price[3] + price[5:8])

    if(converted_price > 2000):
        send_mail()

    print(converted_price)
    print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('harsh956034@gmail.com', 'qumdvlavjiraqfrh')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Call-Duty-Modern-Warfare-PS4/dp/B07SPWYF9L/ref=sr_1_1?crid=3RMVAHXZNXTPN&keywords=call+of+duty+modern+warfare+ps4&qid=1573999412&sprefix=call+of+duty%2Caps%2C274&sr=8-1'
    
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'harsh956034@gmail.com',
        'beyourselfharsh@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT!!')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)