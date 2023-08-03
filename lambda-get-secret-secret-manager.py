import boto3

def get_secret():
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name='us-east-1'
    )
    secret = get_secret_value_response = client.get_secret_value(
            SecretId="<SECRET_NAME>"
    )
    secret_string = secret['SecretString']
    secret_dict = json.loads(secret_string)
    
    return secret_dict

api_key = get_secret()['<SECRET_KEY>']
