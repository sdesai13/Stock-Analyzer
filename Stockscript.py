STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
import statistics
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
import os

from twilio.rest import Client
import requests

apikey = "[INSERT YOUR APIKEY HERE.]"
parameters = {"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME ,
              "outputsize": "compact",  "apikey":apikey}


url = STOCK_ENDPOINT
r = requests.get(url, params=parameters)

data = r.json()
dailydata = data["Time Series (Daily)"]
iterdic = dailydata.items()
first_two= list(iterdic)[:2]
closing_prices = []
for prices in first_two:
    closing_prices.append(prices[1]["4. close"])
day1 = float(closing_prices[0])

day2 = float(closing_prices[1])
average = (statistics.mean([day1,day2]))

percent_change = (abs (day2-day1) / average) * 100



# Now we will write code to retrieve 3 news article and send them if an abnormal change is seen.
if percent_change > 5:
    news_apikey = "[INSERT YOUR NEWS API KEY HERE]"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    news_parameters = {"apiKey": news_apikey, "qInTitle": COMPANY_NAME ,
                  "language": "en"}

    res_news = requests.get(NEWS_ENDPOINT, params= news_parameters)
    news_data = res_news.json()
    #articles = news_data["articles"]

    articles = news_data["articles"]

    title_one = (articles[0]["title"])
    title_two = (articles[1]["title"])
    title_three = (articles[2]["title"])

    brief_one = (articles[0]["description"])
    brief_two = (articles[1]["description"])
    brief_three = (articles[2]["description"])

    url_one = (articles[0]["url"])
    url_two = (articles[1]["url"])
    url_three = (articles[2]["url"])
    if day1 > day2:
        roundedstat = round(percent_change, 2)
        msg = "TSLA: 🔺{}%\nHeadline:{}\nBrief:{}\nLink: {}"
        msg1 = msg.format(roundedstat, title_one, brief_one, url_one)
        msg2 = msg.format(roundedstat, title_two, brief_two, url_two)
        msg3 = msg.format(roundedstat, title_three, brief_three, url_three)
        msg_lst = [msg1,msg2,msg3]
        for message in msg_lst:
            fromnum = os.environ.get("[INSERT YOUR TWILIO NUMBER]")
            tonum = os.environ.get("[INSERT THE NUMBER YOU WANT TO SEND TO]")
            account_sid = os.environ.get("[INSERT YOUR TWILIO ACCOUNT SID]")
            auth_token = os.environ.get("[INSERT YOUR TWILIO AUTHTOKEN]")
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message,
                from_=fromnum,
                to=tonum
            )

            print(message.status)
    elif day1 < day2:
        roundedstat = round(percent_change, 2) * -1
        msg = "TSLA: 🔻{}%\nHeadline:{}\nBrief:{}\nLink: {}"
        msg1 = msg.format(roundedstat, title_one, brief_one, url_one)
        msg2 = msg.format(roundedstat, title_two, brief_two, url_two)
        msg3 = msg.format(roundedstat, title_three, brief_three, url_three)
        msg_lst = [msg1,msg2,msg3]
        for message in msg_lst:
            fromnum = os.environ.get("FROMNUM")
            tonum = os.environ.get("TONUM")
            account_sid = os.environ.get("ACCOUNTSID")
            auth_token = os.environ.get("AUTHTOKEN")
            client = Client(account_sid, auth_token)
            message = client.messages \
                .create(
                body=message,
                from_=fromnum,
                to=tonum
            )

            print(message.status)




#print (day2)
#print (day1)
#print (percent_change)

