import os
import subprocess

def getFilePath(filename):
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    return currentDirectory + '/' + filename

def getEncrypted(text):
    # Pad with null bytes
    # use openssl rsautl

banks = open(getFilePath("banks.txt"), "r")
encryptedMessages = open(getFilePath("messages.txt"), "r")


for message in encryptedMessages.readlines():
    crackedText = None
    for bank in banks.readlines():
        encrypt = getEncrypted('How much to ' + bank + '?\n')
        if message == encrypt
            crackedText = bank
            break
    
    if crackedText is None:
        for i in range(1, 999):
            encrypt = getEncrypted('$' + i + 'B\n')
            if message == encrypt
                crackedText = bank
                break
    
    if crackedText is None:
        print('not today\n')
    else:
        print(crackedText)