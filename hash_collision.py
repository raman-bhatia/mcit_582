import hashlib
import os

def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k < 0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    
    bin_dict = {}
    
    while True:
        random_str = os.urandom(k)
        hashed_int = int(hashlib.sha256(random_str).hexdigest(), 16)
        hashed_bin = bin(hashed_int)[-k:]
        
        if hashed_bin in bin_dict:
            y = bin_dict[hashed_bin]
            return (random_str, y)
        else:
            bin_dict[hashed_bin] = random_str
