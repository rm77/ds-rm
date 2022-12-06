import Pyro5.api


bank1uri = "PYRO:bank1@127.0.0.1:47000"
bank2uri = "PYRO:bank2@127.0.0.1:47000"

if __name__=='__main__':
    #mendaftar di bank1
    p1 = Pyro5.api.Proxy(bank1uri)
    print(p1.get_nasabah('user1'))





