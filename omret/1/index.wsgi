import sae
from omret import wsgi

application = sae.create_wsgi_app(wsgi.application)