import Pyro5.server
from logic_model import *


if __name__=='__main__':
    account_exposed = Pyro5.server.expose(Account)
    bank_exposed = Pyro5.server.expose(BankOperasi)
    custom_daemon = Pyro5.server.Daemon(host='0.0.0.0',port=46000)

    #uri untuk account server
    uri = custom_daemon.register(account_exposed,'account')
    print(uri)

    #uri untuk bank server
    uri = custom_daemon.register(bank_exposed,'bank')
    print(uri)

    #memulai server
    custom_daemon.requestLoop()
