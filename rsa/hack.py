import os
import subprocess
from subprocess import PIPE

from itertools import islice


def getFilePath(filename):
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    return currentDirectory + '/' + filename

def openFile(filename, mode):
    return open(getFilePath(filename), mode)

PRES_KEY = getFilePath('presidentpub.pem')
TRES_KEY = getFilePath('treasurypub.pem')

def getEncrypted(text, key):
    # Pad with null bytes
    text = text.ljust(256, chr(0))

    # use openssl rsautl
    rsa_result = subprocess.run(['openssl', 'rsautl', '-encrypt', '-raw', '-pubin', '-inkey', key], input=text.encode('utf-8'), stdout=PIPE).stdout

    # use base64 encode
    base_result = subprocess.run(['openssl', 'base64', '-A'], input=rsa_result, stdout=PIPE).stdout

    return base_result.decode('utf-8')

banks = openFile("banks.txt", "r").readlines()
hacked = openFile('hacked.txt', 'w')

with openFile("messages.txt", "r") as messagesFile:
    while True:
        message = list(islice(messagesFile, 5))
        if message is None: 
            exit()
        
        message = [m.strip() for m in message]
        message = "".join(message)

        crackedText = None
        test = openFile('test.txt', 'w')
        for bank in banks:
            bank = bank.strip()
            encrypt = getEncrypted('How much to ' + bank + '?\n', PRES_KEY)
            test.write(encrypt)
            if message == encrypt:
                crackedText = bank
                break

        if crackedText is None:
            for i in range(1, 999):
                encrypt = getEncrypted('$' + str(i) + 'B\n', TRES_KEY)
                if message == encrypt:
                    crackedText = str(i)
                    break
        
        if crackedText is None:
            print('not today son')
        else:
            hacked.write(crackedText + '\n')

banksFile.close()
hacked.close()