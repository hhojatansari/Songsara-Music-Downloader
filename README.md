## Songsara-Music-Downloader

Download all the music available on the pages of [Songsara.Net](https://songsara.net)

### Usage
```python
from src.audio_url_scraper import AudioURLScraper

songsara = AudioURLScraper()
songsara.find_all_audio_url(<url>)  # Enter page url e.g. 'https://songsara.net/138538/'
songsara.download(<path>)  # Enter path to download files e.g. 'downloads'
```

### How To Run?
- #### Clone
  ```bash
  git clone git@github.com:hhojatansari/Songsara-Music-Downloader.git
  cd Songsara-Music-Downloader
  ```
- #### Requirements
  ```bash
  python3 -m venv venv
  . venv/bin/activate
  pip3 install -r requirements.txt
  ```
- #### Run
  ```bash
  python app.py
  ```
