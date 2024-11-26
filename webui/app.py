from time import time
from hashlib import sha3_256 as keccak256
from flask import Flask, request, render_template
import os

CHALL_ID = int(os.environ['CHALL_ID'])
POW_TIMEOUT = int(os.environ['POW_TIMEOUT'])
POW_DIFFICULTY = int(os.environ['POW_DIFFICULTY'])
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proof', methods=['POST'])
def proof():
	res = make_response()
    
	proof = request.args.get('proof', '')
	if not proof:
		return "No proof given."
	elif len(proof.split('_')) != 3:
		return "Proof format is wrong."

	timestamp, challId, nonce = proof.split('_')
	if challId != CHALL_ID:
		return "Provided proof is intended for a different challenge."
	elif int(time()) - timestamp > POW_TIMEOUT:
		return "Proof expired."
	
	data = ('_'.join([str(int(timestamp)), str(challId), str(nonce)])).encode()
	calculatedProof = keccak256(data).hexdigest()
	if (int(calculatedProof, 16) >> (256-POW_DIFFICULTY)) != 0:
		return "Proof invalid."
	
	res.set_cookie('proof', proof)
	return "Success"

if __name__ == '__main__':
    app.run(debug=True)
