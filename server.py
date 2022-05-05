import wsgiserver

class Players:
    def __init__(self):
        self.players = {}
    def set_pos(self, player, pos):
        self.players[player] = pos
    def del_player(self, player):
        del self.players[player]
    def get_pos(self, player):
        return self.players[player]

class BaseServer:
    def __init__(self, port=8000, **pages):
        '''
        pages: dict of pages
        e.g.
        BaseServer(main=MainPage, about=AboutPage)
        main will be the index page
        If the page is not specified in the browser, the main page will be loaded
        '''
        self.pages = pages
        self.port = port

        self.setup_pages()

    def setup_pages(self):
        pages = {}
        for page in self.pages:
            if page != "main":
                pages[f"/{page}"] = self.pages[page]
            else:
                pages["/"] = self.pages[page]

        # self.d = wsgiserver.WSGIPathInfoDispatcher(self.pages)
        self.d = wsgiserver.WSGIPathInfoDispatcher(pages)

        self.server = wsgiserver.WSGIServer(self.d, port=self.port)

    def start_server(self):
        self.server.start()

    def stop_server(self):
        self.server.stop()

def set_positions(environ, start_response):
    address = environ["REMOTE_ADDR"]
    arg = environ["PATH_INFO"][1:]
    method = environ["REQUEST_METHOD"]
    player, *pos = arg.split("/")
    players.set_pos(player, pos)
    body = "Success".encode()
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    yield body

def get_positions(environ, start_response):
    address = environ["REMOTE_ADDR"]
    arg = environ["PATH_INFO"][1:]
    method = environ["REQUEST_METHOD"]
    player = arg
    body = f"Success:{player},{players.get_pos(player)}".encode()
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    yield body


players = Players()

server = BaseServer(set_positions=set_positions, get_positions=get_positions)
server.start_server()