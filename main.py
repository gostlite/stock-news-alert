import requests
from twilio.rest import Client
from keys import *

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_api = the_stock_api
Twillio_auth = T_auth
Twillio_ssid = t_ssid
news_api =the_news_api
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


parameters = {"function":"TIME_SERIES_DAILY",
              "symbol":STOCK_NAME,
              "apikey":stock_api}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_list = data_list[0]
yesterday_close = yesterday_list["4. close"]
print(yesterday_close)

day_before_yesterday = data_list[1]
day_before_close =  day_before_yesterday["4. close"]
print(day_before_close)
# print(data.json()["Time Series (Daily)"]["2021-08-20"]['4. close'])

differnece_btween = float(yesterday_close) - float(day_before_close)
print(differnece_btween)

diff_perc = (differnece_btween/float(yesterday_close))*100


news_params = {"q":COMPANY_NAME,
               "apiKey":news_api}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
three_aricles = news_response.json()["articles"][:3]

formated_news = [f"Header:{article['title']} \n .Brief:{article['description']}" for article in three_aricles]

client = Client(Twillio_ssid, Twillio_auth)


for article in formated_news:
    client.messages.create(
        body=article,
        from_=from_num,
        to=to_num
    )
# if diff_perc > 0:
#     print("Get News")


