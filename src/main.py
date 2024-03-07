import requests
import bs4
from dotenv import load_dotenv
import os

# create a session
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

login_url = ""
login_body = {
    "client_id": "344ivdsIpmftbSnxNXolghXUsNB0INWf",
    "redirect_uri": "https://www.spotery.com:443/callback",
    "tenant": "spotery",
    "response_type": "code",
    "scope": "openid email profile",
    "state": "hKFo2SBWMVhtRWhSSFA2aUpYT2FucmtBaHpNM1hMYmpCZ19tdKFupWxvZ2luo3RpZNkgYWFic0RqNGlaOTYxVnVOSE11ZFhWMFIwV0o1RnhKVjCjY2lk2SAzNDRpdmRzSXBtZnRiU254TlhvbGdoWFVzTkIwSU5XZg",
    "connection": "Username-Password-Authentication",
    "username": "johnwdunn20@gmail.com",
    "password": "q87pjGz!MRacW3k",
    "popup_options": {},
    "sso": "true",
    "protocol": "oauth2",
    "audience": "https://spotery.auth0.com/userinfo",
    "_csrf": "CbTcIkba-Z0edz2ULmoIwvrV9S5b259rwtb0",
    "_intstate": "deprecated",
}

# session = requests.Session()
# send login request

# selections
month = 3
day = 6
year = 2024

# urls
POFA_3_request_URL = f"https://www.spotery.com/f/tf-faci-detail/faciDetail?Adf-Window-Id=umie1rph7&Adf-Page-Id=17"
POFA_3_headers = {
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://www.spotery.com/f/adf.task-flow?adf.tfDoc=%2FWEB-INF%2Ftaskflows%2Ffacility%2Ftf-faci-detail.xml&adf.tfId=tf-faci-detail&psOrgaSk=3333238",
    "Origin": "https://www.spotery.com",
}
POFA_3_body = {
    "pt1:idDate": "3/7/2024",
    "pt1:pt_soc1": "",
    "org.apache.myfaces.trinidad.faces.FORM": "f1",
    "Adf-Window-Id": "umie1rph7",
    "Adf-Page-Id": "17",
    "javax.faces.ViewState": "!14iffi0ij5",
    "event": "pt1:idDate",
    "event.pt1:idDate": """<m xmlns="http://oracle.com/richClient/comm"><k v="autoSubmit"><b>1</b></k><k v="suppressMessageShow"><s>true</s></k><k v="type"><s>valueChange</s></k></m>""",
    "oracle.adf.view.rich.PROCESS": "pt1:idDate",
}

POFA_3_cookies = {
    "JSESSIONID": "6JEWLKfuAnakZ7e0s_uDh3kNX8YbguNe5MC4AiKkJMGFdkKefL4K!-1818095560"
}
# testing pulling the data
response = requests.post(
    url=POFA_3_request_URL, headers=POFA_3_headers, data=POFA_3_body
)

if response.status_code == 200:
    print("Success")
    print(response.text)
else:
    print("Failed")
    print(response.status_code)

# Basic ideas:
"""
Need to be able to login (if you login, you might be able to save favorite places)
Should be able to look for a date (or dates) and a time range
Need to limit to near you (could pre-configure the close urls or the names of places)
If it's available, should book
It should only book one
"""
