from jsonrpc import JSONRPCResponseManager, dispatcher
import shelve
import uuid
import os
from datetime import datetime
import time


class BankOperasi:
    def __init__(self):
        self.nasabah={}
    def version(self):
        return 'v1.0'
    def transfer(self,asal='',tujuan='',amount=0):
        if (amount==0):
            return False
        if ((asal in self.nasabah) and (tujuan in self.nasabah)):
            self.nasabah[asal].withdraw(amount,f"transfer ke {tujuan}")
            self.nasabah[tujuan].deposit(amount,f"transfer dari {asal}")


class Account:
    def __init__(self,nama):
        self.dbfile=nama+'_account.db'
        self.db = shelve.open(self.dbfile,writeback=True)
        if len(self.db)==0:
            self.deposit(0,'saldo awal')
        self.nama = nama
    def getinfo(self):
        info = f"nama akun : {self.nama} balance: {self.getsaldo()}"
        return info
    def gettime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    def setrekening(self,amount,desc=''):
        id = str(time.time())
        bal = self.getsaldo()+amount
        self.db[id]=dict(
            waktu=self.gettime(),
            amount=amount,
            balance = bal,
            description=desc
        )
        return True
    def gethistory(self):
        history = ""
        db = sorted(self.db.keys(),key=lambda d:float(d))
        for i in db:
            waktu = self.db[i]['waktu']
            amount = self.db[i]['amount']
            balance = self.db[i]['balance']
            desc = self.db[i]['description']
            history=f"{history}\n{i} {self.nama} {waktu} {amount} {balance} {desc}"
        return history
    def getsaldo(self):
        saldo = 0
        db = sorted(self.db.keys(),key=lambda d:float(d))
        for i in db:
            saldo = saldo + self.db[i]['amount']
        return saldo
    def deposit(self,amount=0,desc=''):
        if (amount==0):
            return False
        return self.setrekening(amount,desc)
    def withdraw(self,amount=0,desc=''):
        if (amount==0):
            return False
        elif self.getsaldo() > amount:
            return self.setrekening(-amount,desc)
        else:
            return False


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
