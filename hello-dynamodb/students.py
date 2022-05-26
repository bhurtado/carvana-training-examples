from botocore.exceptions import ClientError
import boto3

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table("Students")

table.put_item(Item={
    "CI": 123456,
    "Name": "juan perez",
    "Age": 17
})

table.put_item(Item={
    "CI": 654321,
    "Name": "sara rivera",
    "Grade": "A"
})


# get data
def get_student(ci, name, table):
    try:
        response = table.get_item(
            Key={'CI': ci, 'Name': name})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


print(get_student(654321, "sara rivera", table))
