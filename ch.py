import requests 
import hashlib 
import sys


## requesting the API to check for the query
def api_data(query_char):
	url ='https://api.pwnedpasswords.com/range/' + query_char
	res = requests.get(url)
	if res.status_code != 200:
		raise RunTimeError(f'Error Fetching: {res.status_code}, check the Api and try again.')	
	return res

## split the hashes(i.e the full hashed code) by colon, trying to know whether in the full hash code 
## there appears the tail (i.e hashes_to_check). If so, return the number of times that appear. 

def get_password_leaks_count(hashes, hashes_to_check):
	hashes = (line.split(':') for line in hashes.text.splitlines())
	for h, count in hashes:
		if h == hashes_to_check:
			return count
	return 0

## hashing the password, setting aside the beginning of the hashed password and the end.

def api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5_char, tail = sha1password[:5], sha1password[5:]
	## response is the totality of the hashed password
	response = api_data(first5_char) 
	return get_password_leaks_count(response, tail) ## hashes = response, hashes_to_check = tail

def main(args):
	for password in args:
		count = api_check(password)
		if count:
			print(f'{password} was found {count} times. You should change this.')
		else:
			print(f'{password} was not found. Looks secured')
	print('all done!')


main(sys.argv[1:])

