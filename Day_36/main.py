import os
import requests

from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API = os.environ.get("STOCK_API_KEY")

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API= os.environ.get("NEWS_API_KEY")

TwilioSID = os.environ.get("TW_SID")
TwilioAuth = os.environ.get("TW_AUTH_KEY")

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey':STOCK_API
}
stock_request = requests.get(STOCK_URL, params=stock_parameters)
stock_data = stock_request.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday = stock_data_list[0]
yesterday_closing_price = yesterday["4. close"]

day_prior = stock_data_list[1]
day_prior_closing_price = day_prior["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_prior_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_parameters = {
    'apikey':NEWS_API,
    'qInTitle':COMPANY_NAME
}
news_requests = requests.get(NEWS_URL, params=news_parameters)
news_articles = news_requests.json()["articles"]
first_three_articles = news_articles[:3]

if diff_percent > 0:
    print(first_three_articles)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in first_three_articles]

client = Client(TwilioSID, TwilioAuth)
for article in articles:
    message = client.messages.create(
            body=article,
            from="",
            to=""
        )
    print(message.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
