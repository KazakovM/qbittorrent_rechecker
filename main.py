from time import sleep
from qbittorrent import Client

HOST = "localhost"
PORT = "8081"

##login and password are not needed if "bypass authentication for clients on localhost" is checked.


def main():
    while True:
        try:
            qb = Client(f'http://{HOST}:{PORT}/')
            qb.login()
            try:
                if qb is not None:
                    torrents = qb.torrents()
                    for torrent in torrents:
                        if torrent['state'] == 'stalled' and torrent['progress'] > 0.98:
                            print(f'Torrent "{torrent["name"]}" is stuck. Rechecking...')
                            qb.recheck(torrent['hash'])
                            sleep(300)
            except Exception as e:
                print(f'Failed to get torrent list or recheck stuck torrent: {e}')
        except Exception as e:
            print(f'Failed to establish connection: {e}')



if __name__ == "__main__":
    main()