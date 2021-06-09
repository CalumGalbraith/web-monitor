import requests

def url_ok(url):
    r = requests.head(url)
    if r.status_code == 200:
        print(url + " is live")
    else:
        print(url + " has an issue, status code: " + str(r.status_code))

site = input("Enter the web address you want to check (including https://): ")

url_ok(site)