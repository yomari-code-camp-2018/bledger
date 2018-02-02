import hashlib as hasher
import datetime as date
import gnupg as gpg
import os
import json
import hexdump

gpg = gpg.GPG('/home/dineshdb/gpgtest')
gpg.encoding = 'utf-8'

class Block:
    def __init__(self, index, timestamp, frm, to, previous_hash):
        
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()
        pass
    
    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + 
                   str(self.timestamp) + 
                   str(self.data) + 
                   str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()
       
    def sign():
        pass
    
class BlockChain:
    def __init__(self, blocks = []):
        this.blocks = blocks
        this.keys = []
        if len(this.blocks) == 0:
            this.blocks = [create_genesis_block()]
        this.index = len(this.blocks)
        pass
    
    def create_genesis_block():
        return Block(0, date.datetime.now(), "0", "0", "0")
    
    def new_transaction(self, frm, to, amount, comment):        
        block = Block(this.index+1, date.datetime.now(), frm, to, this.blocks[this.index].hash)
        
    def add_block():
        pass
    
        
    def get_block(self, index):
        if index > len(this.blocks):
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
        
        
    def generate_key(email, pas):
        input_data =  gpg.gen_key_input(
            name_email = email,
            passphrase = pas
        )
            
        key = gpg.gen_key(input_data)
        json_dump = json.dumps({"email" : email, "key" : str(key)})
        return json_dump

def list_keys():
    gpg.list_keys()
    pass



def remove_keys():
    pass
