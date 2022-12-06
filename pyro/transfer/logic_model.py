import shelve
import uuid
import os
import json
from datetime import datetime
import time


class Bank(object):
    def __init__(self):
        self.nasabah={}
    def register_nasabah(self,nama=None):
        if (nama is None):
            return False
        self.nasabah[nama]=Account(nama)
        return True
    def get_nasabah(self,nama=''):
        if (nama not in self.nasabah.keys()):
            return False
        return self.nasabah[nama]
    def version(self):
        return 'bank-v1.0'
    def transfer(self,asal='',tujuan='',amount=0):
        if (amount==0):
            return False
        if (asal not in self.nasabah.keys()):
            return False
        if ((asal in self.nasabah) and (tujuan in self.nasabah)):
            self.nasabah[asal].withdraw(amount,f"transfer ke {tujuan}")
            self.nasabah[tujuan].deposit(amount,f"transfer dari {asal}")


class Account(object):
    def __init__(self,nama='default'):
        self.setAccount(nama)
    def setAccount(self,nama='default'):
        self.dbfile=nama+'_account.db'
        self.db = shelve.open(self.dbfile,writeback=True)
        if len(self.db)==0:
            self.deposit(0,'saldo awal')
        self.nama = nama
        return True
    def version(self):
        return 'account-v1.0'
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
    b1 = Bank()
    b1.register_nasabah('user1')
    b1.register_nasabah('user2')



    b2 = Bank()
    b2.register_nasabah('user3')
    b2.register_nasabah('user4')


    b1.get_nasabah('user1').deposit(1000,'deposit awal')
    b1.get_nasabah('user1').withdraw(100,'ambil 100')


    b1.get_nasabah('user2').deposit(1000,'deposit awal')


    b1.transfer('user1','user2',100)
    b2.transfer('user3','user4',10)


    print('----------------------')
    try:
        print(b1.get_nasabah('user1').gethistory())
        print(b1.get_nasabah('user2').gethistory())

        print(b2.get_nasabah('user3').gethistory())
        print(b2.get_nasabah('user4').gethistory())

        #not found
        print(b1.get_nasabah('user3').gethistory())


    except Exception as ee:
        print(str(ee))
