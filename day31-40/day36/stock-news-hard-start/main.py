from dotenv import load_dotenv
import requests
import os
from pkg_resources import load_entry_point
from twilio.rest import Client

load_dotenv()

# STOCK = "TSLA"
STOCK = "NFLX"
# COMPANY_NAME = "Tesla Inc"
COMPANY_NAME = "Netflix, Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = os.getenv('STOCK_API_KEY')
stock_parameters = {
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_API_KEY
}


response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
response.raise_for_status()
daily_data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in daily_data.items()]

yesterday_closing_price= float(data_list[0]['4. close'])
day_before_yesterday_closing_price = float(data_list[1]['4. close'])

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 
closing_difference = yesterday_closing_price - day_before_yesterday_closing_price
up_down = None
if closing_difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percent = round((closing_difference / yesterday_closing_price) * 100)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator

if abs(diff_percent) >= 5:
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    news_parameters = {
        'apiKey': NEWS_API_KEY,
        'q': COMPANY_NAME,
        'searchIn': 'title',
        'sortBy': 'publishedAt'
    }

    response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    response.raise_for_status()
    articles = response.json()["articles"]
    first_three_articles = articles[:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # Send a separate message with each article's title and description to your phone number. 
    #HINT 1: Consider using a List Comprehension.

    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]

    twilio_sid = os.getenv('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    contact_no = os.getenv('PHONE_NO')

    client = Client(twilio_sid, twilio_auth_token)

    for article in formatted_articles:
        message = client.messages \
                    .create(
                        body=article,
                        from_='+18302132262',
                        to=contact_no
                    )

    print(message.sid)







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

