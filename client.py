import http.client

class Response:
    def __init__(self, status, content): 
        self.status = status
        self.content = content

def request(method, baseurl, path, timeout):
    conn = http.client.HTTPConnection(baseurl, timeout=timeout)
    conn.request(method,path)
    r1 = conn.getresponse()
    content = r1.read()
    conn.close()
    return Response(r1.status, str(content)[2:-1] )

def get_positions(baseurl, player, timeout=10): 
    '''
    baseurl: "http://www.example.com" or "127.0.0.1:8000"
    path: "/path/to/page/POST/DATA"
    '''
    response = request("POST", baseurl, f"/get_positions/{player}", timeout)
    if response.status == 200:
        return response.content
    else:
        raise Exception("Server error")

def set_positions(baseurl, player, posx, posy, timeout=10): 
    '''
    baseurl: "http://www.example.com" or "127.0.0.1:8000"
    path: "/path/to/page/POST/DATA"
    '''
    response = request("POST", baseurl, f"/set_positions/{player}/{posx}/{posy}", timeout)
    if response.status == 200:
        return response.content
    else:
        raise Exception("Server error")