from urllib.request import Request, urlopen, ssl, socket
from urllib.error import URLError, HTTPError
import json

base_url = input('Enter the web address you would like to check: ')
port ='443'

hostname = base_url
context = ssl.create_default_context()

with socket.create_connection((hostname, port)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())
        data = json.dumps(ssock.getpeercert())
        dict = json.loads(data)
        print('SSL Cert start date: ' + dict['notBefore'])
        print('SSL Cert end date: ' + dict['notAfter'])
        
