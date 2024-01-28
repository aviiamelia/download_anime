import requests

from environs import Env
from os import getenv
env = Env()
env.read_env()

def start_torrent(scrape_website):
    qbittorrent_url = getenv('QBIT_TORRENT_URL')
    username = getenv('QBIT_TORRENT_USERNAME')
    password = getenv('QBIT_TORRENT_PASSWORD')

    login_url = f'{qbittorrent_url}/api/v2/auth/login'
    login_data = {'username': username, 'password': password}
    response = requests.post(login_url, data=login_data)

    if response.status_code == 200:

        cookie = response.cookies.get('SID')
        save_path = getenv('SAVEPATH')
        url = getenv('URL_ANIMES_TOSHO')
        download_links = scrape_website(url)
        for links in download_links:
            add_torrent_url = f'{qbittorrent_url}/api/v2/torrents/add'
            add_torrent_data = {'urls': links,'savepath':fr'{save_path}'}
            headers = {'Cookie': f'SID={cookie}'}
            response = requests.post(add_torrent_url, data=add_torrent_data, headers=headers)
        if response.status_code == 200:
            print("All torrents are being downloaded successfully")
        else:
            print(f"Failed to downloaded torrents. Status code: {response.status_code}")

    else:
        print(f"Failed to authenticate. Status code: {response.status_code}")