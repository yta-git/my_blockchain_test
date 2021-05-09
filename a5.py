import a2 as block_manage
import a4 as ip_manage
import client
import server
import transaction_verifier

import threading
from queue import Queue
import json
import os

myip = '163.221.124.239'
myport = 8888
difficulty = 4

# os.system('\\rm ./blocks.txt')
# os.system('\\touch ./blocks.txt')

try:
    first_block = False
    last_block = ip_manage.get_last_block('http://163.221.124.239:8080/blocks.txt')
    if last_block:
        data_json = json.loads(last_block)
        prev_index = data_json['index']
        prev_hash = block_manage.sha256_2(last_block)
        print('## last block ##')
        print(last_block)
        print(prev_hash)

        with open('blocks.txt', 'a') as f:
            f.write('---------------\n')
            f.write(last_block + '\n')

    else:
        prev_index = -1
        prev_hash = '0' * 64
        first_block = True

except:
    prev_index = -1
    prev_hash = '0' * 64
    first_block = True


# ip_manage.register()

while True:

    q = Queue()

    server_thread = threading.Thread(target=server.server, args=(q, myip, myport))
    server_thread.start()

    while True:

        try:
            if q.qsize():
                data = q.get()
                data_json = json.loads(data)
                hash = block_manage.sha256_2(data)
                

                if  hash.startswith('0' * difficulty) and (first_block or data_json['prev_block'] == prev_hash) and transaction_verifier.verify_transaction(data_json['tx']):
                    print('😍 verified 😍')
                    prev_hash = hash
                    prev_index = data_json['index']
                    first_block = False

                    with open('blocks.txt', 'a') as f:
                        f.write(data + '\n')

                else:
                    print('😭 discarded 😭')
                
                # print('############################')
                # print(data)
                # hash = block_manage.sha256_2(data)
                # print(hash)
                # print('############################')

        except:
            transaction = input('transaction ?> ')
            if not transaction_verifier.verify_transaction(transaction):
                print('😡 Signature verification failed 😡')
                continue
            else:
                print('😁 Signature verified 😁')


            submit = False

            while True:
                q2 = Queue()
                local_thread = threading.Thread(target=block_manage.chain_block, args=(q2, prev_index + 1, prev_hash, transaction))
                block_manage.flag = False
                local_thread.start()

                while True:
                    if q.qsize():

                        print('😇 new block appeared 😇')

                        data = q.get()
                        data_json = json.loads(data)

                        print('############################')
                        print(data)
                        hash = block_manage.sha256_2(data)
                        print(hash)
                        print('############################')
                        
                        try:
                            if  hash.startswith('0' * difficulty) and (first_block or data_json['prev_block'] == prev_hash):
                                print('😍 verified 😍')
                                block_manage.flag = True
                                prev_hash = hash
                                prev_index = data_json['index']
                                first_block = False
                                
                                with open('blocks.txt', 'a') as f:
                                    f.write(data + '\n')

                                break
                            else:
                                print('😭 discarded 😭')
                        except:
                            pass

                    if q2.qsize():

                        print('🤑 nonce found 🤑')

                        hash, data = q2.get()
                        print('++++++++++++++++++++++++++++')
                        print(data)
                        print(hash)
                        print('++++++++++++++++++++++++++++')

                        with open('blocks.txt', 'a') as f:
                            f.write(data + '\n')
                        
                        prev_hash = hash
                        prev_index += 1

                        for ip in ip_manage.get():
                            
                            if ip == myip:
                                continue

                            try:
                                client.client(ip, 8888, data)
                                pass
                            except:
                                pass

                        print('😎 submitted 😎')
                        submit = True
                        break

                if submit:
                    break
            



