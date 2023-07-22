import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_API_NEWS = "5d12d240957247eeb7c1f0055528a9c1"
MY_API_STOCKS = "PU5549K5KHK695KN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": MY_API_STOCKS
}

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response_stock = requests.get(url="https://www.alphavantage.co/query", params=params)
dic_time = response_stock.json()["Time Series (Daily)"]

list_time = [value for (key,value) in dic_time.items()]
yesturday = float(list_time[0]["4. close"])
before_yesturday =  float(list_time[1]["4. close"])

##Difference in price
difference = abs(before_yesturday-yesturday)
print(difference)
#Percentage difference
print(yesturday)
print(before_yesturday)
percentage = round((difference / yesturday) * 100,1)
print(percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage > 5:
    print("Get News")
    # response_news = requests.get(url = )
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

