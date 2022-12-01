from logic_model import *


if __name__=='__main__':
    a = Account('royyana')
    a.deposit(1000,'deposit awal')
    a.withdraw(10,'ambil')
    print(a.gethistory())
    print(a.getsaldo())

    b = Account('ibrahim')
    b.deposit(1000,'deposit awal')
    b.withdraw(900,'ambil')
    print(b.gethistory())
    print(b.getsaldo())

    c = Account('ananda')
    c.deposit(1000,'deposit awal')
    c.withdraw(500,'ambil')
    print(c.gethistory())
    print(c.getsaldo())



    t = BankOperasi()
    t.nasabah['royyana']=a
    t.nasabah['ibrahim']=b
    t.nasabah['ananda']=c
    t.transfer('royyana','ananda',100)
    t.transfer('ananda','ibrahim',10)


    print('----------------------')
    print(a.gethistory())
    print(b.gethistory())
    print(c.gethistory())
