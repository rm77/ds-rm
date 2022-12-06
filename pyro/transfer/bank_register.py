import Pyro5.api


bank1uri = "PYRO:bank1@127.0.0.1:47000"
bank2uri = "PYRO:bank2@127.0.0.1:47000"

if __name__=='__main__':
    #mendaftar di bank1
    p1 = Pyro5.api.Proxy(bank1uri)
    p1.register_nasabah('user1')
    p1.register_nasabah('user2')

    #mendaftar di bank2
    p2 = Pyro5.api.Proxy(bank2uri)
    p2.register_nasabah('user3')
    p2.register_nasabah('user4')




