from sys import argv, exit
from json import loads
import transaction_verifier

from collections import defaultdict
from datetime import datetime


def count(file='blocks.txt'):

    bank = defaultdict(int)

    print('### TRANSACTIONS ###')

    with open(file) as f:
        for l in f.readlines():
            json_data = loads(l)
            tx = json_data['tx']
            time = json_data['time']
            time = datetime.utcfromtimestamp(time)

            verify = transaction_verifier.verify_transaction(tx)
            if not verify:
                print('!!! this block chain is blocken !!!')
                exit(1)

            frm, to, coin, sig = tx.split(';')

            bank[frm] -= int(coin)
            bank[to] += int(coin)

            frm = frm[:15] + '...'
            to = to[:15] + '...'

            print(f'[{time}]')
            print(f'{frm} ----- {coin} coins -----> {to}: ({"verified" if verify else "ERROR"})')
            print()

    print('### CURRENT COIN ###')
    for user in bank.keys():
        print(f'{user}   have   {bank[user]} coins')


if __name__ == '__main__':
    print('block file:', argv[1])
    count(argv[1])

