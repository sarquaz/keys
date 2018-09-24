import boto3

from keys.store.provider import Provider

class S3Provider(Provider):
    """S3 store provider"""
    def __init__(self, **kwargs):
        super(S3Provider, self).__init__()
        self.arg = arg
        
        s3_endpoint_url = None
        s3_bucket_name = 'default'
        
        if 's3_endpoint_url' in kwargs:
            s3_endpoint_url = kwargs['s3_endpoint_url']
            
            
        
        
        