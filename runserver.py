from waitress import serve
from session2.wsgi import application

#this final app
serve(application, host="127.0.0.1", port= "8080")