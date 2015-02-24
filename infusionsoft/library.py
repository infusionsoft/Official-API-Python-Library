import sys

if sys.version_info[0] == 3:
    from xmlrpc.client import ServerProxy, Error
elif sys.version_info[0] == 2:
    from xmlrpclib import ServerProxy, Error
else:
    print('Unrecognised python environment. Not python 2.x or 3.x')
    

class Infusionsoft:

    def __init__(self, name, api_key):
        self.client = ServerProxy("https://" + name + ".infusionsoft.com/api/xmlrpc")
        self.client.error = Error
        self.key = api_key

    def __getattr__(self, service):
        def function(method, *args):
            call = getattr(self.client, service + '.' + method)
            try:
                return call(self.key, *args)
            except self.client.error as v:
                return "ERROR", v
        return function

    def server(self):
        return self.client

class InfusionsoftOAuth(Infusionsoft):

    def __init__(self, access_token):
        self.client = ServerProxy("https://api.infusionsoft.com/crm/xmlrpc/v1?access_token=%s" % access_token)
        self.client.error = Error
        self.key = access_token
