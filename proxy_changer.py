import socket
import socks
import requests

def connect_tor():
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    socket.socket = socks.socksocket

def check_ip():
    connect_tor()
    print('connected Tor')
    session = requests.Session()
    response = session.get('http://www.icanhazip.com')
    print(response.text)




