# Python

### Project_1 

```
import requests
import smtplib
my_email = "hsupcseba@gmail.com"
my_password = "zxsegstlwhshebeh"
from stock_price import nvda_price, aapl_price, googl_price


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "H0BMOR4H4DXZYFD4"

content_1 = googl_price()
content_2 = aapl_price()
content_3 = nvda_price()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, my_password)

    connection.sendmail(from_addr=my_email,
                        to_addrs=["aloneflyy@yahoo.com.tw","seba.hsu@hotmail.co.uk"],

                        msg= f"Subject: Daily_Stock_Closing_Price\n\n{content_1}\n\n{content_2}\n\n{content_3}"
                        )

```
