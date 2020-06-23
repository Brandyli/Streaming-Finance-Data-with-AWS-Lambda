# Streaming-Finance-Data-with-AWS-Lambda

For this project, you are tasked with provisioning a few Lambda functions to generate near real time finance data records for downstream processing and interactive querying.

This project leads us through the process of consuming “real time” data, processing the data and then dumping it in a manner that facilitates querying and further analysis, either in real time or near real time capacity.

In doing so, we will familiarize ourselves with a process that one can leverage in their professional or personal endeavors that require consumption of data that is “always on” and changing very quickly, in sub hour (and typically) sub minute intervals.

* Facebook (FB)
*	Beyond Meat (BYND)
*	Netflix (NFLX)
*	Pinterest (PINS)
*	Square (SQ)
*	The Trade Desk (TTD)
*	Okta (OKTA)
*	Snap (SNAP)
*	Datadog (DDOG)

This repo includes:

Lambda Source Code For DataCollector
Lambda function file data_collector.py
S3 Content From DataTransformer
CSV Output From Query in DataAnalyzer

### AWS Lambda configuration
DataCollector API endpoint: https://ayctpvzsp3.execute-api.us-east-1.amazonaws.com/default/DataCollector
<img width="1393" alt="Screen Shot 2020-05-15 at 10 04 16 PM" src="https://user-images.githubusercontent.com/46945617/82107763-2846b600-96f8-11ea-99a4-07a8e0cfc313.png">

### AWS kinesis firehose delivery stream “Monitoring” page
<img width="370" alt="Screen Shot 2020-05-25 at 1 01 52 AM" src="https://user-images.githubusercontent.com/46945617/82779955-9b9ca600-9e23-11ea-9475-1693cddd5950.png">
<img width="369" alt="Screen Shot 2020-05-25 at 1 01 58 AM" src="https://user-images.githubusercontent.com/46945617/82779961-9dff0000-9e23-11ea-9018-4fedea289518.png">

