import xmlrpc.client
info = xmlrpc.client.ServerProxy('http://chocotech.trustcode.com.br/').start()
url, username, password = \
    info['107.170.32.11'],  info['demo'], info['demo']

# To test connection
print('Ping', info.ping())
