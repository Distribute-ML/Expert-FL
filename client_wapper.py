import requests
import subprocess
import pynvml


import pickle
import time
def req_train(serverIp,serverPort,name,dataroot):
    url = f'http://{serverIp}:{serverPort}/server/req_train'
    resp = pickle.loads(requests.post(url,data=pickle.dumps(name)).content)
    if resp['train']:
        cuda = resp['cuda']
        cmd = f'python client.py --name {name} --cuda {cuda} --dataroot {dataroot}'
        cmd = cmd.split(' ')
        subprocess.run(cmd, shell=False)
    time.sleep(0.1)


def url_build_core(serverIp,serverPort):
    return f'http://{serverIp}:{serverPort}/server'

    
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name')

if __name__=='__main__':
    args = parser.parse_args()
    while(True):
        name = args.name
        req_train('127.0.0.1','8080',name,'data')
    
    

