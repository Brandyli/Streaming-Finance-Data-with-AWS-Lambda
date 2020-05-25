# Importing necessary libraries
import boto3
import os
import subprocess
import sys
import json

# Installing the yfinance package to get the stocks
subprocess.check_call([sys.executable, "-m", "pip", "install", "--target", "/tmp", 'yfinance'])
sys.path.append('/tmp')

# Import yfinance package to download stocks
import yfinance as yf

def lambda_handler(event, context):
    
    # Initialize boto3 client
    fh = boto3.client("firehose", "us-east-1”)
    
    # Define required variables and arrays for compamny stocks we will analyze
    tickers = ['fb', 'shop', 'bynd', 'nflx', 'pins', 'sq', 'ttd', 'okta', 'snap', 'ddog']
    
    # Fetch stock values for each company
    for ticker in range(len(tickers)):
        records = yf.download(tickers[ticker], start = '2020-05-14', end = '2020-05-15', interval = '1m')
        data = []
        
        # Cleaning the data and store them as a dict
        for r in range(len(records)):
            output = {"High":records['High'][r],"Low":records['Low'][r],"Timestamp":records.index[r].strftime('%m/%d/%Y %X'),"Name":tickers[ticker]}
            
            # Convert the data into JSON
            as_jsonstr = json.dumps(output)
    
            # Pass the stream info where the data should be stored as a single batch
            fh.put_record(
                DeliveryStreamName="finance", 
                Record = {'Data': as_jsonstr.encode('utf-8')})
            data.append(output)
            
    # Return the JSON file dump    
    return {
        'statusCode': 200,
        'body': json.dumps(f'Done! Recorded: {as_jsonstr}')
    }
