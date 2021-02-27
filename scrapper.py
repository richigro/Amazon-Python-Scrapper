#modify to work for other web scrapping tools easy to modify 
# allow you to make hhtp requests and get back data
import requests
# BeatifulSoup helps us parse the response from our GET request
from bs4 import BeautifulSoup
# a simple mail protocol 
import smtplib
# to make function run for an extended period of time
import time
#stuff todo

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
  if converted_product_price < max_product_price:
  # send an email to the user
    send_email(converted_product_price)
  else:
    print "Price hasn't gone down from the max price of ${} USD".format(max_product_price)


# testing function
# check_product_price()

def send_email(newPrice):
  # set up a connection between computer and gmail service
  server = smtplib.SMTP('smtp.gmail.com', 587)
  # this identifies itself to server 
  server.ehlo()
  # encrypts connection
  server.starttls()
  # again identifies itself
  server.ehlo()

  # login to server
  server.login('richigro@gmail.com', 'mnkbrsfscwphbivd')

  # email subject line
  subject = "Price fell Down to ${} !".format(newPrice)
  # using older format of interpolating string
  # because running python 2.7.17
  body = "Check the Amazon link: {}".format(product_url)

  msg = 'Subject: {} \n\n {}'.format(subject, body)
  # send email from and to and message 
  server.sendmail(
    'richigro@gmail.com',
    'richigro@gmail.com',
    msg
  )

  print 'Email has been sent out!'
  # close the connection to the open server
  server.quit()

# Be careful! this will always run
# until it is stopped from terminal with 'crtl + c'
while(True):
  check_product_price()
  # the period two wait in between function calls
  # currently set to make a function call every 60 seconds
  time.sleep(60)
