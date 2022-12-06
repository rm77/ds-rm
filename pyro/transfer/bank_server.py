from  Pyro5.api import expose, behavior
import Pyro5.server
from logic_model import *


if __name__=='__main__':
    custom_daemon = Pyro5.server.Daemon(host='0.0.0.0',port=47000)
    BankClass = Pyro5.api.expose(Bank)

    Bank1Object = BankClass()
    uri1 = custom_daemon.register(Bank1Object,'bank1',behavior(instance_mode='single'))
    print(uri1)

    Bank2Object = BankClass()
    uri2 = custom_daemon.register(Bank2Object,'bank2',behavior(instance_mode='single'))
    print(uri2)

    #memulai server
    custom_daemon.requestLoop()
