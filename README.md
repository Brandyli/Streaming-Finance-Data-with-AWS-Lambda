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
<img width="1393" alt="Screen Shot 2020-05-15 at 10 04 16 PM" src="https://user-images.githubusercontent.com/46945617/82107763-2846b600-96f8-11ea-99a4-07a8e0cfc313.png">

In order to run lambda functions that also manage dependencies, we must leverage a "deployment package", basically a zip file containing your lambda code and all the dependencies it needs all packaged into a single artifact.

This repo provides a few tools that will help you manage your lambda functions and the dependencies.

Developing
To develop your function:

Build your docker container - when you do this, your requirements.txt will be installed inside the container
```
docker build -t local_lambda .
```
As you make changes, run them like so:
```
docker run -v $(pwd):/app local_lambda python lambda_function.py
```
NOTE: if you want to use a new dependency, you will have to rebuild the container

Artifact
You want to create a zip file that you can upload to AWS. To do so, run the following:
```
docker build -t deployment -f Dockerfile.deployment_artifact .
```
This builds your zip file.
```
docker run -v $(pwd):/app/artifact deployment
```
This copies the file into your host filesystem so that you can upload it into Lambda.
