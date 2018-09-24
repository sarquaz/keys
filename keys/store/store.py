import logging

class Store(object):
    """abstract encrypted store class"""
    def __init__(self, store_name):
        super(Store, self).__init__()
        self.store_name = store_name
        self._logger = logging.getLogger(type(self).__name__)
        
    def set_encryption_key(self, encryption_key):
        pass
        
    def get_key(self, key):
        pass
        
    def set_key(self, key):
        pass    