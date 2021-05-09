import requests
import configparser
import json
import socket

def register():
    config = configparser.ConfigParser()
    config.read('./config.ini', 'UTF-8')
    headers = {"content-type": "application/json"}
    url = "http://" + config.get('server', 'host') + ":" + config.get('server', 'port') + "/cgi-bin/register_ip_addr.py"
    r = requests.get(url, headers=headers)

    if r.status_code == requests.codes.ok:
        print('😀 ip registerd 😀')
    else:
        print('😵 ip register failed 😵')

def get():
    config = configparser.ConfigParser()
    config.read('./config.ini', 'UTF-8')
    headers = {"content-type": "application/json"}
    url = "http://" + config.get('server', 'host') + ":" + config.get('server', 'port') + "/cgi-bin/get_ip_addr.py"

    ip_addrs = requests.get(url, headers=headers).json()
    peers = [ip_addr["ip_addr"] for ip_addr in ip_addrs]
    # print(peers)
    return peers

def get_last_block(url='http://fire-b22.naist.jp:8000/blocks.txt'):
    
    for b in requests.get(url).text.split('\n')[::-1]:
        if b.startswith('{"difficulty":'):
            return b

if __name__ == '__main__':
    register()
    get()
    get_last_block()