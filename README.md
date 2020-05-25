# Streaming-Finance-Data-with-AWS-Lambda

In this project, I provisioned two Lambda functions to generate near real time finance data records 
for downstream processing and interactive querying. 

I collect one full day’s worth of stock HIGH and LOW prices for each company listed below on Thursday, May 14th 2020, at an one minute interval

● Facebook (FB)
● Shopify (SHOP)
●	Beyond Meat (BYND)
●	Netflix (NFLX)
●	Pinterest (PINS)
●	Square (SQ)
●	The Trade Desk (TTD)
●	Okta (OKTA)
●	Snap (SNAP)
●	Datadog (DDOG)

This repo includes:

Lambda Source Code For DataCollector
Lambda function file data_collector.py
S3 Content From DataTransformer
CSV Output From Query in DataAnalyzer

### AWS Lambda configuration
DataCollector API endpoint: https://ayctpvzsp3.execute-api.us-east-1.amazonaws.com/default/DataCollector
<img width="1393" alt="Screen Shot 2020-05-15 at 10 04 16 PM" src="https://user-images.githubusercontent.com/46945617/82107763-2846b600-96f8-11ea-99a4-07a8e0cfc313.png">

