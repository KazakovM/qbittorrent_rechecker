from datetime import datetime
import json
from time import sleep
from qbittorrent import Client


def load_configs():
    with open('config.json', 'r', encoding="UTF-8") as file:
        js = json.load(file)
        global HOST, PORT, LOGIN, PASSWORD
        HOST = js["HOST"]
        PORT = js["PORT"]
        LOGIN = js["LOGIN"]
        PASSWORD = js["PASSWORD"]


def main():
    while True:
        try:
            qb = Client(f'http://{HOST}:{PORT}/')
            qb.login(LOGIN, PASSWORD)
            try:
                if qb is not None:
                    torrents = qb.torrents()
                    for torrent in torrents:
                        print(torrent["state"])
                        if torrent['state'] != 'stalledDL' and torrent['progress'] > 0.98:
                            print(f'{datetime.now()}: torrent "{torrent["name"]}" is stuck. Rechecking...')
                            qb.recheck(torrent['hash'])
                            sleep(300)
            except Exception as e:
                print(f'{datetime.now()}: Failed to get torrent list or recheck stuck torrent: {e}')
        except Exception as e:
            print(f'{datetime.now()}: Failed to establish connection: {e}')


if __name__ == "__main__":
    print(f'{datetime.now()}: Starting script...')
    load_configs()
    main()