import json
import os
from pushbullet import Pushbullet

def ping(event, context):
    pb = Pushbullet(os.environ["PUSHBULLET_API_KEY"])
    auth_key = os.environ["AUTH_KEY"]
    query = event['queryStringParameters']

    if  query['auth_key'] == auth_key:
        if not "type" in query.keys(): # default msg type to note
            query.type = "note"
        getattr(pb, "push_%s" % query['type'])(query['header'], query['body'])
        body = {
            "message": "Auth succeful",
            "input": event
        }
    else:
        body = {
            "message": "Auth failed",
            "input": event
        }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
