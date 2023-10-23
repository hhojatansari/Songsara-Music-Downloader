import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from datetime import datetime


class AudioURLScraper:
    def __init__(self):
        self._page_url = None
        self._soup = None
        self._audio_elements = None
        self._audio_urls_dict = None
        self._title = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # if title not found

    def _get_page_source(self):
        page_source_text = requests.get(url=self._page_url).text
        self._soup = BeautifulSoup(page_source_text, "html.parser")

    def _find_title(self):
        title = self._soup.find_all("h2", {"class": "AL-Si"})[0].text
        if title not in ['', None]:
            self._title = title

    def _find_audio_elements(self):
        self._audio_elements = self._soup.find_all("div", {"class": "audioplayer-source"})
        print(f'#{len(self._audio_elements)} audio url founded!')

    def _get_audio_urls(self):
        for element in tqdm(self._audio_elements, desc='Check urls reachability'):
            url = element.get('data-src')
            name = url.split('/')[-1].replace(" ", "-")
            self._audio_urls_dict[name] = {
                'url': url,
                'reachable': self._check_reachable(url)
            }

    def find_all_audio_url(self, page_url):
        self._audio_urls_dict = {}
        self._page_url = page_url
        self._get_page_source()
        self._find_title()
        self._find_audio_elements()
        self._get_audio_urls()
        return self._audio_urls_dict

    def download(self, path):
        try:
            path = os.path.join(path, self._title)
            os.makedirs(path, exist_ok=True)
            for audio_name in tqdm(self._audio_urls_dict, desc="Downloading"):
                if self._audio_urls_dict[audio_name]['reachable']:
                    with open(os.path.join(path, audio_name), 'wb') as file:
                        file.write(
                            requests.get(self._audio_urls_dict[audio_name]['url']).content
                        )
        except ConnectionError:
            print('An exception occurred in download!')

    @staticmethod
    def _check_reachable(url):
        try:
            if requests.head(url).status_code == 200:
                return True
            else:
                return False
        except ConnectionError:
            return False
