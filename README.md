# Stock-Analyzer

This program uses multiple api endpoints and HTTP get requests to collect relevant data about stock prices and news articles pertaining to the company. The user can choose any stock they wish to receive notifications about, and the program will use API endpoints and get requests to collect relevant data about stock prices and closing prices.

The stock analyzer will then use Python, along with the statistics module to analyze the prices and detect if there is an abnormal change in the prices. This threshold can be manually adjusted. If the program detects an abnormal change, it will then use HTTP get requests to collect relevant news information from a News API. This information will then be sent via text message to the user using the Twilio API. The message will signify the approximate percent change in the stock price, and send three relevant news articles indicating why this change might have happened along with the link to each article.

To use this program, you will need to set up your own API keys for the News API and Stock API, and their endpoint links can be found in the script. You will also need to decide what stock you wish to receive information about and input its symbol and company name. Lastly, you can choose to set up your own Twilio API account to receive text notifications. Please reach out to me if you have any questions about the code or how to set the program up correctly.


