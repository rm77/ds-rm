import Pyro5.api


nama_account = 'royyana'
uri = "PYRO:account@127.0.0.1:46000"

if __name__=='__main__':
    p = Pyro5.api.Proxy(uri)
    p.setAccount(nama_account)
    p.deposit(1000,'deposit awal')
    print(p.getinfo())
    print(p.gethistory())
    print(p.getsaldo())

