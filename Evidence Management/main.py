import json
from web3 import Web3, HTTPProvider
import ipfshttpclient
import os
import subprocess

getName =  subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE).stdout
gName =  getName.read()

getTime = subprocess.Popen("date", shell=True, stdout=subprocess.PIPE).stdout
gTime = getTime.read()

blockchain_address = 'http://127.0.0.1:7545'

web3 = Web3(HTTPProvider(blockchain_address))
client = ipfshttpclient.connect()
web3.eth.defaultAccount = web3.eth.accounts[0]

ChainContract = 'build/contracts/Evidence.json'


ChainAddress = '0x8a7B379F51E3c6CE2bF2Ba21268bf1D1319a3D15'


with open(ChainContract) as file1:
	contract_json1 = json.load(file1)
	contract_abi1 = contract_json1['abi']


contract1 = web3.eth.contract(address=ChainAddress, abi=contract_abi1)


inGame = True

while inGame:


	print("\n[1] Upload Evidence ")
	print("[2] Verify if Evidence Exists ")
	print("[3] Download Evidence File ")
	print("[4] Exit \n")

	choice = int(input("[+] Choose Option: "))

	if choice == 1:
		print("Add New Evidence - ")

		evID = int(input("Enter ID: "))
		evName = input("Enter Evidence File Name: ")
		a = os.popen("ipfs add /home/adam/Desktop/Evidence\ Management/Evidence/" + evName + " -w").readline().strip("added ")
		print("Enter Evidence Owner: ")
		evCID = a[:46]
		evOwner = str(input())
		evLocation = str(input("Enter Evidence Location: "))

		contract1.functions.addEvidence(
			evID,
			evName,
			evCID,
			evOwner,
			evLocation
		).transact()

		print("Evidence Uploaded Successfully ...")

	elif choice == 2:
		aa = int(input("Enter ID: "))
		myEvidence = contract1.functions.getEvidence(aa).call()
		myArray = ["Name", "Hash", "Owner", "Location"]
		n = 0
		for x in myEvidence:
			print("\n[*] Evidence " + myArray[n] + ": " + x)
			n += 1
			
	elif choice == 3:
		print("Download Evidence - ")
		evCID = input("Enter Evidence CID: ")
		evName = input("Name It As: ")
		os.system("ipfs get {} -o /home/adam/Desktop/Evidence\ Management/Evidence/{}".format(evCID, evName))
			
	elif choice == 4:
		print("Exiting ...")
		inGame == False
		break
