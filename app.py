from src.audio_url_scraper import AudioURLScraper

songsara = AudioURLScraper()
songsara.find_all_audio_url('https://songsara.net/138538/')
songsara.download('downloads')
