import os
import modules.credentials_harvester.credentialsharvester as credentialsharvester
import modules.reddit_scraper.redditscraper as redditscraper
import modules.voice_generation.generatevoice as generatevoice
import modules.video_editor.videoeditor as videoeditor
import modules.description_generation.generatedescription as generatedescription 

#Define Script Directory to extrapolate place to save posts and read stock videos
scriptDir = os.path.dirname(os.path.abspath(__file__))
videoFilePath = os.path.join(scriptDir, 'videos')

#Gets API Info from terminal
credentialsharvester.RuntimeHarvest()

#Scrape Reddit and Return folder of stored stories
detailsArray = redditscraper.Scrape(scriptDir)
#Generates Voice File with Elevenlabs 
detailsArray = generatevoice.GenerateVoice(detailsArray)

# # #Test Array 
# #detailsArray = [{'folderLocation': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326', 
# #                  'textFilePath': 'f:\\Projects\\reddit-scraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt',
# #                  'audioPath': 'f:\\Projects\\reddit-sycraper\\reddit-scraper\\posts\\8d33f140-1b8d-11ef-bd0b-00933795e326\\Whoever_created_the_.txt.mp3'}]

for details in detailsArray:
    videoeditor.Edit(details, videoFilePath, '.mp4')
    generatedescription.GenerateDescription(details)