# main.py

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.wsgi import WSGIMiddleware
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

# REST API with FastAPI
app = FastAPI()

@app.api_route("/rest", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"])
async def rest_endpoint(request: Request):
    body = await request.body()
    return JSONResponse({
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "body": body.decode('utf-8'),
        "iy": "bflmpsvz"
    })

# SOAP Service with Spyne
class EchoService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def echo(ctx, request):
        return request

soap_app = Application(
    [EchoService],
    tns='spyne.examples.echo.soap',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_soap_app = WsgiApplication(soap_app)

# Mount the WSGI SOAP app onto the FastAPI app
app.mount("/soap", WSGIMiddleware(wsgi_soap_app))

# Now you can run this combined app using Uvicorn
# uvicorn main:app --reload
"""
Raw body SOPA request

<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:spy="spyne.examples.echo.soap">
   <soapenv:Header/>
   <soapenv:Body>
      <spy:echo>
         <spy:request>Hello World xxx </spy:request>
      </spy:echo>
   </soapenv:Body>
</soapenv:Envelope>

"""