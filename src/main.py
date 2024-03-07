import requests
import bs4
from dotenv import load_dotenv
import os
import random
import time

# Court data
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

# create a session
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

login_url = "https://spotery.auth0.com/usernamepassword/login"
login_body = {
    "client_id": "344ivdsIpmftbSnxNXolghXUsNB0INWf",
    "redirect_uri": "https://www.spotery.com:443/callback",
    "tenant": "spotery",
    "response_type": "code",
    "scope": "openid email profile",
    "state": "hKFo2SBWMVhtRWhSSFA2aUpYT2FucmtBaHpNM1hMYmpCZ19tdKFupWxvZ2luo3RpZNkgYWFic0RqNGlaOTYxVnVOSE11ZFhWMFIwV0o1RnhKVjCjY2lk2SAzNDRpdmRzSXBtZnRiU254TlhvbGdoWFVzTkIwSU5XZg",
    "connection": "Username-Password-Authentication",
    "username": username,
    "password": password,
    "popup_options": {},
    "sso": "true",
    "protocol": "oauth2",
    "audience": "https://spotery.auth0.com/userinfo",
    "_csrf": "CbTcIkba-Z0edz2ULmoIwvrV9S5b259rwtb0",
    "_intstate": "deprecated",
}

session = requests.Session()
session.headers.update({
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Auth0-Client": "eyJuYW1lIjoibG9jay5qcy11bHAiLCJ2ZXJzaW9uIjoiMTEuMTcuMyIsImVudiI6eyJhdXRoMC5qcy11bHAiOiI5LjExLjIifX0=",
    "Content-Type": "application/json",
    "Cookie": "_csrf=tM05RYZvfrXkpPVrON9KGmDX; did=s%3Av0%3Af9ea45f0-dc18-11ee-a397-a566f1d123c9.YNUahKjPxcvmhGtkNj5pyrH6FuFXZqMMEa%2B7dpAHZck; did_compat=s%3Av0%3Af9ea45f0-dc18-11ee-a397-a566f1d123c9.YNUahKjPxcvmhGtkNj5pyrH6FuFXZqMMEa%2B7dpAHZck; auth0=s%3Av9HOfpUpqpg81NltiFbiJLds-H376JP-.q%2BwFctMVz2D6Qd%2BalXWXaPCCxNkrAwMajrAzMAVuS68; auth0_compat=s%3Av9HOfpUpqpg81NltiFbiJLds-H376JP-.q%2BwFctMVz2D6Qd%2BalXWXaPCCxNkrAwMajrAzMAVuS68",
    "Origin": "https://spotery.auth0.com",
    "Referer": "https://spotery.auth0.com/login?state=hKFo2SBWMVhtRWhSSFA2aUpYT2FucmtBaHpNM1hMYmpCZ19tdKFupWxvZ2luo3RpZNkgYWFic0RqNGlaOTYxVnVOSE11ZFhWMFIwV0o1RnhKVjCjY2lk2SAzNDRpdmRzSXBtZnRiU254TlhvbGdoWFVzTkIwSU5XZg&client=344ivdsIpmftbSnxNXolghXUsNB0INWf&protocol=oauth2&redirect_uri=https%3A%2F%2Fwww.spotery.com%3A443%2Fcallback&audience=https%3A%2F%2Fspotery.auth0.com%2Fuserinfo&scope=openid%20email%20profile&response_type=code",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
})
login_response = session.post(url=login_url, json=login_body)

if login_response.ok:
    print("Login successful")
    rand_int = random.randint(0, 6)
    print(f"Sleeping for {rand_int} seconds")
    time.sleep(rand_int)
    
    POFA_3_response = session.post(
        url=POFA_3_request_URL, headers=POFA_3_headers, data=POFA_3_body
    )

    if POFA_3_response.status_code == 200:
        print("Success")
        print(POFA_3_response.text)
    else:
        print("Failed")
        print(POFA_3_response.status_code)
else:
    print("Login failed", login_response.text)
    

    

