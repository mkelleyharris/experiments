from wsgiref.simple_server import make_server, demo_app

def demo_app(environ, start_response):
    """A WSGI application that greets the world"""
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!']


httpd = make_server('', 8001, demo_app)
print "Serving HTTP on port 8001..."

# Respond to requests until process is killed
httpd.serve_forever()