class Provider(object):
    """abstract store provider class"""
    def __init__(self):
        super(GenericProvider, self).__init__()
        
    def list_stores(self):
        pass
        
    def use_store(self):
        pass    
        