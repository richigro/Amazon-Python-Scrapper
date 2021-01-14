import requests
# BeatifulSoup helps us parse the response from our GET request
from bs4 import BeautifulSoup

# Declaring a variable that is an url to the product page of the item you want
product_url = "https://www.amazon.com/Logitech-Dual-motor-Feedback-Responsive-PlayStation/dp/B00Z0UWWYC/ref=sr_1_1?crid=QWI8J1FZT74C&dchild=1&keywords=ps4+steering+wheel&qid=1610597104&sprefix=ps4+steering+whe%2Caps%2C215&sr=8-1"

max_product_price = 240

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

def check_product_price():

  page = requests.get(product_url, headers=headers)

  soup = BeautifulSoup(page.content, "html.parser")

  # Make sure you use the encoding type otherwise it might
  # not work
  # print(soup.prettify().encode('utf-8'))

  # find the div with id of Product title and then gets text ommiting 
  # any other html tags and finally strip() removes leading and 
  # trailing whitespace
  product_title = soup.find(id="productTitle").get_text().strip()

  # print product_title

  # I changed the encoding of the number from unicode to utf-8 in order to be able to
  # parse string into number with the float() function native in python
  product_price = soup.find(id="priceblock_ourprice").get_text().encode('utf-8')

  converted_product_price = float(product_price[1:len(product_price)])
  # print type(converted_product_price)

  # when the product's converted_product_price goes under the user defined max_product_price
  # alert the user
  if converted_product_price < product_price:
  # send an email to the user
    send_email()


# testing function
check_product_price()
