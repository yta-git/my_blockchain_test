import ecdsa
from base64 import b64encode, b64decode

def make_key():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vk = sk.get_verifying_key()

    str_sk = sk.to_string()
    str_vk = vk.to_string()
    
    b_sk = b64encode(str_sk)
    b_vk = b64encode(str_vk)

    return b_sk.decode(), b_vk.decode()

def signiture(b_sk, message='sign'):
    str_sk = b64decode(b_sk)
    sk = ecdsa.SigningKey.from_string(str_sk, curve=ecdsa.SECP256k1)
    sig = sk.sign(message.encode())    
    b_sig = b64encode(sig)
    return b_sig

def verify(b_vk, b_sig, message='sign'):
    sig = b64decode(b_sig)
    str_vk = b64decode(b_vk)
    vk = ecdsa.VerifyingKey.from_string(str_vk, curve=ecdsa.SECP256k1)
    try:
        res = vk.verify(sig, message.encode())
        # print('Signature verified')
        return res
    except:
        # print('Signature verification failed')
        return False

if __name__ == '__main__':
    b_sk, b_vk = make_key()
    print('b_sk:', b_sk)
    print('b_vk:', b_vk)

    b_sig = signiture(b_sk, 'test')
    print(b_sig)
    print('sig:', b_sig)

    res = verify(b_vk, b_sig, 'tesa')
    print(res)




