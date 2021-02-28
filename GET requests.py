import requests

 url = input("Target_Website Url >")
 try:
     get_response = requests.get("https://" + url)
     print(get_response)
 except requests.exceptions.ConnectionError:
     pass

#Discovering Website Subdomains Using Wordlist

 import requests


 def request(url) :
     try:
         return requests.get("http://" + url)
     except requests.exceptions.ConnectionError:
         pass


target_url = input("Target Url >")

with open(" directory of your wordlist","r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        test_url = word+ "." + target_url
        response = request(test_url)
        if response:
            print("[+] Discovered subdomain --> " + test_url)
