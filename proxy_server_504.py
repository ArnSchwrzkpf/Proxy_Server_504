from twisted.internet import reactor
from twisted.web import proxy, server
from twisted.web.http import NOT_FOUND
 
class CustomProxy(proxy.Proxy):
    def _handleRequest(self, request):
        # Returns 504 Gateway Timeout
        request.setResponseCode(504)
        request.write(b'Gateway Timeout')
        request.finish()
 
    def requestReceived(self, method, uri, version):
        # Returns 504 when receiving a request
        self._handleRequest(self)
 
if __name__ == '__main__':
    # Start a proxy server on port 8080
    factory = server.Site(CustomProxy())
    reactor.listenTCP(8080, factory)
    print("Proxy server is running on http://localhost:8080")
    reactor.run()
