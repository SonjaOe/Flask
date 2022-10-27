from flask import Flask, request, json
import logging
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    details = {
        'name': 'sonja',
        "email": "sonja.esimerkki@gmail.com"
    }
    return details

@app.route("/hello", methods=['POST'])
def post_demo():
    data = json.loads(request.data)

    try:
        s3_client = boto3.client('s3')
        se3_client.create_bucket(Bucket=data['sonja-flask-bucket'])

    except ClientError as e:
        logging.error(e)
        return {"failure": "bucket creation failed"}
    return { "success": "bucket created successfully"}

app.run()