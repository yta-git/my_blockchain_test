from random import choice, randint
from pprint import pprint
import time
import transaction_maker
import a2 as block_manage
import a4 as ip_manage
import EC
import a2
import os

def make_users(user_n=5):
    users = []
    for _ in range(user_n):
        prv_key, pub_key = EC.make_key()
        users.append({'prv_key': prv_key, 'pub_key': pub_key})

    return users

def make_transaction(users, transaction_n=10):

    # ip_manage.register()

    prev_hash = '0' * 64
    index = 0

    for _ in range(transaction_n):
        frm = choice(users)
        to = choice(users)
        coin = str(randint(1, 100))

        transaction = transaction_maker.make_transaction(frm['pub_key'], to['pub_key'], coin, frm['prv_key'])
        # print(transaction)
        prev_hash, data = a2.create_block(index, prev_hash, int(time.time()), 4, transaction)
        index += 1
        print(data)

        with open('transactions_random.txt', 'a') as f:
            f.write(transaction + '\n')

        with open('blocks_random.txt', 'a') as f:
            f.write(data + '\n')

        # for ip in ip_manage.get():
        #     try:
        #         # client.client(ip, 8888, data)
        #         pass
        #     except:
        #         pass



if __name__ == '__main__':

    os.system('\\rm ./blocks_random.txt')
    os.system('\\rm ./transactions_random.txt')
    
    a = make_users()
    pprint(a)
    make_transaction(a, 100)




