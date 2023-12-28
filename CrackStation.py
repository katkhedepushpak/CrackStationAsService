import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):
    ShaHash = event['path'].split('/')[-1]
    data = client.get_item(TableName='LookupTable', Key={'ShaHash': {'S': ShaHash}})
    if "Item" in data:
        ans  = data["Item"]["password"]["S"]
        response = {'statusCode': 200, 'body': json.dumps({ShaHash:ans})}
    else:
        response = {'statusCode': 404}
    return response