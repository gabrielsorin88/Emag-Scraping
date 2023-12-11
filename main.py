import requests
from bs4 import BeautifulSoup
from send_email import SendEmail


user_url = "https://www.emag.ro/smartwatch-garmin-instinct-2x-solar-graphite-010-02805-00/pd/DWT118MBM/"
user_price = "2700"#input("I want to get notified if the price drops under this value: ")
set_price = float(user_price)

to_address = "pygabrielsorin@yahoo.com" #input("Email")

response = requests.get(user_url)
response_text = response.text
soup = BeautifulSoup(response_text, "html.parser")

product_price_string= soup.find(name="p", class_="product-new-price").get_text().split()[0]
product_name = soup.find(name = "h1", class_="page-title").get_text().strip()

product_price = float(product_price_string.replace(".", "").replace(",", "."))
print(product_price_string)
print(product_name)
send_email = SendEmail(to_address, product_name, product_price, set_price )

send_email.send_email()