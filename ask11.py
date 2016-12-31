import urllib2
import requests
response = urllib2.urlopen('https://api.punkapi.com/v2/beers/random')
html = response.read()
to = raw_input()
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox2304176a7de14cbfa2380b8520f3e967.mailgun.org/messages",
        auth=("api", "key-0faacefef4ab5bef2fa255f758e615b4"),
        data={"from": "Not main mail <ptech1998@gmail.com>",
              "to": [to],
              "subject": "TSAKO MIA MPYRA",
              "text": html.split('"')[5] })
send_simple_message()
