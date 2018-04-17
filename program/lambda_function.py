import boto3
import logging
import module as m
import libs.module2 as m2
import os

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(name)s (%(lineno)s) - %(levelname)s: %(message)s",
	datefmt='%Y.%m.%d %H:%M:%S')

def lambda_handler(event, context):
    log.info("Starting lambda.")
    log.info("We are using boto3 version: " + boto3.__version__)
    log.info(m.greeting("leonard"))
    log.info(m2.strong_greeting("leonard"))
    log.info(str(os.listdir()))
    log.info("Ending lambda.")
    print(event)
    print(context.get_remaining_time_in_millis())
    print(context.aws_request_id)
    if context.client_context:
        print(context.client_context)
    print(context.function_name)
    print(context.function_version)
    print(context.identity.cognito_identity_id)
    print(context.identity.cognito_identity_pool_id)
    print(context.invoked_function_arn)
    print(context.log('Log this for me please'))
    print(context.log_group_name)
    print(context.log_stream_name)
    print(context.memory_limit_in_mb)

    return 'It works!'
