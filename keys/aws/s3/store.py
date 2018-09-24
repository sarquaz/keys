from keys.store.store import Store

class S3Store(Store):
    """docstring for S3Sti"""
    def __init__(self, store_name="default"):
        super(S3Store, self).__init__(store_name)
        
        self._logger.debug(self)    
        