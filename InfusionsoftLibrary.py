class Infusionsoft:
    
    from xmlrpclib import ServerProxy, Error
    
    def __init__(self, name, api_key, server = ServerProxy, error = Error):
        self.client = server("https://" + name + ".infusionsoft.com/api/xmlrpc")
        self.client.error = error
        self.key = api_key
        return None
    
    def __getattr__(self, service):
        def function(method, *args):
            call = getattr(self.client, service + '.' + method)
            try:
                return call(self.key, *args)
            except self.client.error, v:
                return "ERROR", v
        return function
    
    def server(self):
        return self.client
