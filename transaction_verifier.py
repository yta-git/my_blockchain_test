import EC
from a2 import sha256_2

def verify_transaction(transaction=None):
    if not transaction:
        transaction = input('transaction > ')

    try:
        owner, rec, coin, sig = transaction.split(';')
    except:
        return False

    message = owner + rec + coin
    message = sha256_2(message)
    return EC.verify(owner, sig, message)

if __name__ == '__main__':
    verify_transaction()
