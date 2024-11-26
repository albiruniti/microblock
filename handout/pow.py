### WARNING
### DO NOT CHANGE THESE IF YOU ARE A
### PARTICIPANT IN A CTF COMPETITION

from hashlib import sha3_256 as keccak256
from time import time

### TODO: For problem setter, change these variables then remove this comment.
challID = 0     # general identifier
difficulty = 22 # how many leading 0 bits (max. 256, rec. 22)
### ENDTODO

timestamp = time()
nonce = -1

proof = ''
data = b''

def makedata():
	global data
	data = ('_'.join([str(int(timestamp)), str(challID), str(nonce)])).encode()

makedata()
h = keccak256(data)
proof = h.hexdigest()

while (int(proof, 16) >> (256-difficulty)) > 0:
	timestamp = time()
	nonce += 1
	makedata()

	h = keccak256(data)
	proof = h.hexdigest()

print(data.decode())
