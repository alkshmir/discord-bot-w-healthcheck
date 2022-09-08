from aiohttp import web
import socket
import discord

class healthcheck(object):
    def __init__(self, client: discord.client, port: int=8080):
        self.host = "0.0.0.0"
        self.port = port
        client.loop.run_until_complete(self.start_server())
        
    async def handle(self, request):
        text = "Hello" 
        return web.Response(text=text)

    def mk_socket(self, reusePort=False):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if reusePort:
            SO_REUSEPORT = 15
            sock.setsockopt(socket.SOL_SOCKET, SO_REUSEPORT, 1)
        sock.bind((self.host, self.port))
        return sock

    async def start_server(self):
        reusePort = True
        app = web.Application()
        app.add_routes([web.get('/', self.handle)])
        #handler = app.make_handler()
        runner = web.AppRunner(app)
        await runner.setup()
        sock = self.mk_socket(reusePort=reusePort)
        srv = web.SockSite(runner, sock)
        await srv.start()
        print("Listening on port {}".format(self.port))
