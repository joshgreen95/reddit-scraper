import os

import modules.reddit_scraper.redditscraper as redditscraper
import modules.voice_generation.generatevoice as generatevoice
import modules.video_editor.videoeditor as videoeditor

from moviepy.editor import TextClip

scriptDir = os.path.dirname(os.path.abspath(__file__))
videoPath = os.path.join(scriptDir, 'videos', 'vid.mp4')

# #Scrape Reddit and Return folder of stored stories
# detailsArray = redditscraper.Scrape('SHOWERTHOUGHTS', 1, scriptDir)

# detailsArray = generatevoice.GenerateVoice(detailsArray)

detailsArray = [{'folderLocation': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326', 
                'textFilePath': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt',
                'audioPath': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt.mp3'}]

for details in detailsArray:
    videoeditor.Edit(details, videoPath, '.mp4')