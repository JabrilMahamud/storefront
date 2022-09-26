import boto3
from datetime import date, datetime
import json



def dictionaryCreator():
    dynamodb = boto3.resource("dynamodb", region_name="eu-west-2")
    table = dynamodb.Table("MetadataJson")
    tableDict = table.scan(
        ProjectionExpression="#AN, account, #S",
        ExpressionAttributeNames={
            "#AN": "account-name",
            "#S": "status",
        },
    )
    with open("MetaData.json", "w") as fp:
        json.dump(tableDict, fp, sort_keys=True)

dictionaryCreator()
print("Complete")