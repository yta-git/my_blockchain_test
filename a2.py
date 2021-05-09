import hashlib
import json
import time

def sha256_2(text):
    hash = hashlib.sha256(text.encode()).hexdigest()
    hash = hashlib.sha256(hash.encode()).hexdigest()
    return hash

flag = False

def create_block(index, prev_block, time, difficulty, tx):
    global flag
    data = {}
    data['index'] = index
    data['prev_block'] = prev_block
    data['time'] = time
    data['difficulty'] = difficulty
    data['tx'] = tx

    nonce = 0
    while True:
        data['nonce'] = nonce
        json_data = json.dumps(dict(sorted(data.items())), separators=(',', ':'))
        hash = sha256_2(json_data)

        if hash.startswith('0' * difficulty):
            # print(json_data)
            # print(hash)
            # print()
            return hash, json_data

        nonce += 1
        if flag:
            return False, False

def chain_block(q, index, prev_hash, transaction):
    hash, json_data = create_block(index, prev_hash, int(time.time()), 4, transaction)
    q.put((hash, json_data))
    return hash, json_data

if __name__ == '__main__':
    index = 0
    prev_hash = '0' * 64
    difficulty = 6 # difficulty 6 -> 4

    while True:
        transaction = input('transaction: ')
        prev_hash = create_block(index, prev_hash, int(time.time()), difficulty, transaction)
        index += 1

