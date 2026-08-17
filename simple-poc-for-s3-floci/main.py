import boto3
import json
import sys

s3 = boto3.client(
    "s3",
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)
BUCKET_NAME = "test-bucket"

def save_notes(title: str, body: str)->str:
    key = title.replace(" ", "-").lower() + ".json"
    s3.put_object(Bucket = BUCKET_NAME, Key = key, Body = json.dumps({"title": title, "body": body}))
    return f"Notes saved..."



def read_notes(key: str):
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
        print("note" , json.load(response['Body']))
    except:
       print("Key not found, please check key properly")



    

def delete_notes(key: str):
    s3.delete_object(Bucket=BUCKET_NAME, Key=key)
    print("Deleted ", key)


if  __name__  == "__main__":

    args = sys.argv

    if len(args) < 2:
        print("Usage python main.py [save][get][delete] [args]")
        sys.exit(1)


    command = args[1]

    if command == 'save':
        title = args[2]
        body = args[3]

        if not title or not body:
            print("Usage python main.py save '<title>' '<body>'")
            sys.exit(1)
        save_notes(title=title, body=body)
    elif command == 'get':
        key = args[2]

        if not key:
            print("Usage python main.py get '<key>'")
            sys.exit(1)

        read_notes(key=key)

    elif command == 'delete':
        key = args[2]

        if not key:
            print("Usage python main.py delete '<key>'")
            sys.exit(1)

        delete_notes(key=key)
    else:
        raise "Command not supported...!"


