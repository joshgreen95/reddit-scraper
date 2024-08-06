import os
import uuid
import datetime

from .content_moderation import contentsanitizer 
import praw

from ..credentials_harvester.credentialsharvester import GetCredential

def Scrape(scriptDir):
    reddit = praw.Reddit(
        client_id = GetCredential('REDDIT', 'CLIENT_ID'),
        client_secret = GetCredential('REDDIT', 'CLIENT_SECRET'),
        user_agent = GetCredential('REDDIT', 'CLIENT_UA'),
        username = GetCredential('REDDIT', 'CLIENT_USERNAME'),
        password = GetCredential('REDDIT', 'CLIENT_PASSWORD')
    )

    subreddit = input('Which Subreddit should be scraped? (r/_____) \n').lower()
    subreddit = reddit.subreddit(subreddit)
    numPosts = int(input('How many posts should be retrieved? (Max 10) \n'))
    #Check Subreddit is valid from choice of 'Top, Hot, Rising, New, Controversial
    postCategory = input('How should posts be sorted? (Top, Hot, New, Rising, Controversial) \n').lower()
    timeFilter = input('How far back should we check? (Day, Week, Month, Hour, Year, All) \n').lower()
    
    validSelection = False
    posts = None

    while(not validSelection):
        match(postCategory):
            case 'top':
                posts = subreddit.top(time_filter=timeFilter, limit=numPosts)
                validSelection = True
            case 'hot':
                posts = subreddit.hot(time_filter=timeFilter, limit=numPosts)
                validSelection = True
            case 'new':
                posts = subreddit.new(time_filter=timeFilter, limit=numPosts)
                validSelection = True
            case 'rising':
                posts = subreddit.rising(time_filter=timeFilter, limit=numPosts)
                validSelection = True
            case 'controversial':
                posts = subreddit.controversial(time_filter=timeFilter, limit=numPosts)
                validSelection = True
            case __:
                print('Invalid Post Category Selection :^( \n')

    folderID = f'{subreddit}_{datetime.datetime.now().date()}' 
    print(folderID)
    folderLocation = os.path.join(scriptDir, 'posts', folderID)
    if(not os.path.exists(folderLocation)):
        os.makedirs(folderLocation)

    detailsArray = []

    for post in posts:
        sanitizedPost = contentsanitizer.Sanitize(post.title, post.selftext)
        fileName = sanitizedPost['title'].replace(' ', '_')[:20] + '.txt'
        fileLocation = os.path.join(folderLocation, fileName)
        
        with open(fileLocation, 'w') as postFile:
            postFile.writelines([sanitizedPost['title'], '\n', sanitizedPost['innerText']])
            postFile.close()

        fileDetails = {
            'folderLocation': folderLocation,
            'textFilePath': fileLocation,
        }

        print(f'-- Post Found : {post.title}')
        detailsArray.append(fileDetails)
    print('-- Reddit Scrape Complete')
    return detailsArray