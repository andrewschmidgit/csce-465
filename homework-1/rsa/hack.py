import os
import subprocess
from subprocess import PIPE
from itertools import islice

PRES_PUB_KEY = 'presidentpub.pem'
TRES_PUB_KEY = 'treasurypub.pem'

def getFilePath(filename):
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    return currentDirectory + '/' + filename

def openFile(filename, mode):
    return open(getFilePath(filename), mode)

def getEncrypted(text, pub_key):
    # Pad with null bytes
    text = text.ljust(214, chr(0))
    
    # use openssl rsautl
    rsa_result = subprocess.run(['openssl', 'rsautl', '-encrypt', '-pubin', '-inkey', pub_key], input=text.encode('utf-8'), stdout=PIPE).stdout

    # base64 encode
    encode_result = subprocess.run(['openssl', 'base64'], input=rsa_result, stdout=subprocess.PIPE).stdout

    return encode_result


banks = list(openFile("banks.txt", "r").readlines())
encryptedMessageLines = openFile("messages.txt", "r")

while True:
    message = ''.join(islice(encryptedMessageLines, 5))
    if not message:
        break
    crackedText = None
    for bank in banks:
        bank = bank.strip()
        clear = f'How much to {bank}?\n'
        encrypt = getEncrypted(clear, TRES_PUB_KEY).decode('utf-8')
        print(f'Bank: {bank}')
        print(f'clear: {clear}')
        print(f'encrypt: {encrypt}')
        print(f'message: {message}')
        
        if message == encrypt:
            crackedText = bank
            break
        exit()
    
    if crackedText is None:
        for i in range(1, 999):
            encrypt = getEncrypted('$' + str(i) + 'B\n', PRES_PUB_KEY)
            if message == encrypt:
                crackedText = bank
                break
    
    if crackedText is None:
        print('not today\n')
    else:
        print(crackedText)

encryptedMessageLines.close()
banks.close()