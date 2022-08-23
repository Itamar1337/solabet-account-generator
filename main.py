import requests, random, logging, os
from threading import Thread
logging.basicConfig(
    level=logging.INFO,
    format="\x1b[38;5;63m[\x1b[0m%(asctime)s\x1b[38;5;63m]\x1b[0m %(message)s",
    datefmt="%H:%M:%S"
)
os.system("")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
}
count = 0
def create():
    chars = ("abcdefghijklmnopqrstuvwxyz")
    email1 = "".join(random.choice(chars) for x in range(8))
    email = (email1 + "@gmail.com")
    json_data = {
        'email': (email),
        'name': email1,
        'password': 'bandana!1',
        }
    response = requests.post('https://solabet.gg/auth/register',headers=headers, json=json_data)
    if response.status_code == 200:
        logging.critical (f'{(email)}:{"bandana!1"}:{email1}')
        open('./credentials.txt', 'a').write(f'{(email)}:{"bandana!1"}:{email1}')
    else:
        logging.critical("Error")
while True:
    x = Thread(target=create)
    x.start()
