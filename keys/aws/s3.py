import logging

class S3(object):
    """S3 logic"""
    def __init__(self, bucket_name='bucket', **kwargs):
        super(S3, self).__init__()
        self._logger = logging.getLogger(type(self).__name__)
        
        self._logger.debug("init with kwargs %s" % str(kwargs))
        
        if 'bucket_name' in kwargs:
            bucket_name = kwargs['bucket_name']
            
        self.bucket_name = bucket_name
        
        self._logger.debug(self.bucket_name)    
        
    def list_stores(self):
        pass
        
    def use_store(self, store_name):
        pass    
        
    def set_encryption_key(self, encryption_key):
        pass
        
            
    def get_key(self, key):
        pass
        
    def set_key(self, key):
        pass        
        
        
        