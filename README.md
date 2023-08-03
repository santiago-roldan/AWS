# AWS

The script in lambda-get-secret-secret-manager.py allows you to use values stored in the AWS secret manager as variables in your AWS Lambda functions, in order to increase security and avoid the sensitive data coded in plain text in the functions.

Note: to use this script, your Lambda function's role has to have permissions in Secret Manager
