import Pyro5.server
from logic_model import *


if __name__=='__main__':
    Pyro5.server.expose(BankOperasi)
    Pyro5.server.serve(
        {
            BankOperasi: 'bank'
        },
        use_ns=False, verbose=True,host='0.0.0.0',port=45000)