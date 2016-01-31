from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.servers import FTPServer
from pyftpdlib.handlers import FTPHandler
import getpass
username=raw_input("Enter ftp username:")
password=getpass.getpass()
path=raw_input("Enter complete path:")
authorizer = DummyAuthorizer()
authorizer.add_user(username,password,path)
handler = FTPHandler
handler.authorizer = authorizer
address = ('127.0.0.1', 21)
server = FTPServer(address, handler)
server.max_cons=512
server.max_cons_per_ip=2
server.serve_forever()
