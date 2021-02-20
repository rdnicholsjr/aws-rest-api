import json
import boto3

def lambda_handler(event, context):

	reqbody = json.loads(event['body'])

	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table('userdb')

	table.put_item(
		Item={
			'name': reqbody['name'],
			'email': reqbody['email']
		}
	)
	response = (
		{
			'headers': {
        	  'Content-Type': 'application/json',
        	  'Access-Control-Allow-Origin': '*',
        	},
        	'statusCode': 200
    	}
    )
	return response
