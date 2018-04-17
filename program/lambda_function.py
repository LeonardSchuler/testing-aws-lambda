import boto3
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(
	level=logging.INFO,
	format="%(asctime)s - %(name)s (%(lineno)s) - %(levelname)s: %(message)s",
	datefmt='%Y.%m.%d %H:%M:%S')

def lambda_handler(event, context):
    log.info("Starting lambda.")
    log.info("We are using boto3 version: " + boto3.__version__)
    log.info("Ending lambda.")
