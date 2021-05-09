import EC
from a2 import sha256_2

def make_transaction(frm=None, to=None, coin=None, prv_key=None):
    if not (frm and to and coin and prv_key):
        frm = input('pub_key of owner > ')
        to = input('pub_key of receiver > ')
        coin = input('amount of coins > ')
        prv_key = input('prv_key of owner > ')

    if int(coin) <= 0:
        print('amount of coins must be greater that 0')
        import sys; sys.exit(1)
    
    message = frm + to + coin
    message = sha256_2(message)

    sig = EC.signiture(prv_key, message)
    sig = sig.decode()

    transaction = f'{frm};{to};{coin};{sig}'
    print('transaction:', transaction)
    return transaction

if __name__ == '__main__':
    make_transaction()





