import os

# import modules.reddit_scraper.redditscraper as redditscraper
# import modules.voice_generation.generatevoice as generatevoice
import modules.video_editor.videoeditor as videoeditor

scriptDir = os.path.dirname(os.path.abspath(__file__))
videoFilePath = os.path.join(scriptDir, 'videos')

#Scrape Reddit and Return folder of stored stories
#detailsArray = redditscraper.Scrape('SHOWERTHOUGHTS', 1, scriptDir)

#detailsArray = generatevoice.GenerateVoice(detailsArray)

# #Test Array - No need to gen a voice everytime
detailsArray = [{'folderLocation': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326', 
                 'textFilePath': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt',
                 'audioPath': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt.mp3'}]

for details in detailsArray:
    videoeditor.Edit(details, videoFilePath, '.mp4')