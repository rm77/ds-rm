import Pyro5.api
p = Pyro5.api.Proxy("PYRO:bank@127.0.0.1:46000")
p.deposit(1000,'deposit awal')
p.withdraw(700,'bu cpt')
print(p.gethistory())
print(p.getsaldo())

