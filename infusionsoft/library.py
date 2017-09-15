try:
    from xmlrpclib import ServerProxy, Error
except ImportError:
    from xmlrpc.client import ServerProxy, Error


class Infusionsoft(object):
    base_uri = 'https://%s.infusionsoft.com/api/xmlrpc'

    def __init__(self, name, api_key, use_datetime=False):
        uri = self.base_uri % name
        self.client = ServerProxy(uri, use_datetime=use_datetime)
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
    base_uri = 'https://api.infusionsoft.com/crm/xmlrpc/v1?'

    def __init__(self, access_token, use_datetime=False):
        uri = '%saccess_token=%s' % (self.base_uri, access_token)

        self.client = ServerProxy(uri, use_datetime=use_datetime)
        self.client.error = Error
        self.key = access_token
