import logging

from keys.aws.s3.store import S3Store

logging.basicConfig(level=logging.DEBUG)

store = S3Store()


