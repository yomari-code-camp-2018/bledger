import hashlib as hasher
import datetime as date
import gnupg as gpg
import os
from sys import exit
import json
import hexdump
from pathlib import Path

gpg_home = os.path.join(Path.home(), 'gpgtests')

class Block:
    def __init__(self, index, timestamp, frm, to, previous_hash):
        
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        pass
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + 
                   str(self.timestamp) + 
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
       
    def sign():
        pass

def create_genesis_block():
    return Block(0, date.datetime.now(), "0", "0", "0")
    
class BlockChain:
    def __init__(self, blocks = []):
        self.blocks = blocks
        self.keys = []
        if len(self.blocks) == 0:
            self.blocks = [create_genesis_block()]
        self.index = len(self.blocks)
        pass
    
    def new_transaction(self, frm, to, amount, comment):        
        block = Block(self.index+1, date.datetime.now(), frm, to, self.blocks[self.index].hash)
        
    def add_block():
        pass
    
        
    def get_block(self, index):
        if index > len(self.blocks):
            pass
        
    def generate_key(email, pas):
        input_data =  gpg.gen_key_input(
            name_email = email,
            passphrase = pas)
            
        key = gpg.gen_key(input_data)
        json.dumps({email : email})
        
    def import_key():
        pass
    
    def export_key():
        pass
        
    def get_key(self, email):
        pass
        
        
    def generate_key(self, email, pas):
        input_data =  gpg.gen_key_input(
            name_email = email,
            passphrase = pas
        )
            
        key = gpg.gen_key(input_data)
        json_dump = json.dumps({"email" : email, "key" : str(key)})
        return json_dump

    def remove_keys():
        pass
        
def find_available_keys():
    pass
    
def get_key(key):
    pass
    
def delete_keys():
    gpg.delete_keys(fp)

chain = BlockChain()
gpg = gpg.GPG( homedir = gpg_home)
gpg.encoding = 'utf-8'

keys = gpg.list_keys()

if len(keys) == 0:
    q = input("No keys found, would you like to generate one?")
    if q != "y":
    	quit(1)
    
    email = input("Email : ")  
    key = chain.generate_key(email, "")
    
email = input("Email : ")
    
print("Using email " + email)

