import redditscraper
import generatevoice
#Scrape Reddit and Return folder of stored stories
folderLocation = redditscraper.Scrape()
generatevoice.GenerateVoice(folderLocation)