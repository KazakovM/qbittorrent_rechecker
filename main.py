from datetime import datetime
import json
from time import sleep, strftime, localtime
from qbittorrent import Client


def load_configs():
    with open('config.json', 'r', encoding="UTF-8") as file:
        js = json.load(file)
        global HOST, PORT, LOGIN, PASSWORD, MIN_SIZE, MAX_SIZE
        HOST = js["HOST"]
        PORT = js["PORT"]
        LOGIN = js["LOGIN"]
        PASSWORD = js["PASSWORD"]
        MIN_SIZE = float(js["MIN_SIZE"])
        MAX_SIZE = float(js["MAX_SIZE"])


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())

def main():
    try:
        qb = Client(f'http://{HOST}:{PORT}/')
        qb.login(LOGIN, PASSWORD)
        try:
            if qb is not None:
                while True:
                    torrents = qb.torrents()
                    for torrent in torrents:
                        sleep(2) #без задержки может вернуть "-1"
                        if (MIN_SIZE*1073741824 > torrent['size'] or torrent['size'] > MAX_SIZE*1073741824) and float(str(torrent["progress"])[0]) != 1:
                            print(f'{datetime.now()}: Torrent "{torrent["name"]}" is out of size limit: {round(torrent["size"]/1073741824, 2)} GB. Deleting...')
                            qb.delete_permanently(torrent['hash'])
                            sleep(3)
                        if torrent['state'] == 'stalledDL' and float(str(torrent["progress"])[0:4]) > 0.98:
                            print(f'{datetime.now()}: Torrent "{torrent["name"]}" is stuck. Rechecking...')
                            qb.recheck(torrent['hash'])
                            qb.increase_priority(torrent['hash'])
                            sleep(300) #после проверки торрент может недолго быть в stalled, нужна задержка
        except Exception as e:
            print(f'{datetime.now()}: Failed to get torrent list or recheck stuck torrent: {e}')
    except Exception as e:
        print(f'{datetime.now()}: Failed to establish connection: {e}')


if __name__ == "__main__":
    print(f'{datetime.now()}: Starting script...')
    load_configs()
    main()