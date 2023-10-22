## Songsara-Music-Downloader

Download all the music available on the pages of [Songsara.Net](https://songsara.net)


### Usage
```python

from src.audio_url_scraper import AudioURLScraper

songsara = AudioURLScraper()
songsara.find_all_audio_url(<url>)  # Enter page url e.g. 'https://songsara.net/138538/'
songsara.download(<path>)  # Enter path to download files e.g. 'downloads'
```
