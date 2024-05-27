import os
import uuid

from .content_moderation import contentsanitizer 
import praw

from .reddit_api_details import details

def Scrape(subreddit, searchLimit, scriptDir):
    reddit = praw.Reddit(
        client_id = details['CLIENT_ID'],
        client_secret = details['CLIENT_SECRET'],
        user_agent = details['CLIENT_UA'],
        username = details['CLIENT_USERNAME'],
        password = details['CLIENT_PASSWORD']
    )

    subreddit = reddit.subreddit(subreddit)
    
    top_posts = subreddit.top(limit=searchLimit)

    folderUuid = str(uuid.uuid1())
    folderLocation = os.path.join(scriptDir, 'posts', folderUuid,)

    os.mkdir(folderLocation)

    detailsArray = []

    for post in top_posts:
        sanitizedPost = contentsanitizer.Sanitize(post.title, post.selftext)
        fileName = sanitizedPost['title'].replace(' ', '_')[:20] + '.txt'
        #fileLocation = folderLocation + '\\' + fileTitle
        fileLocation = os.path.join(folderLocation, fileName)
        
        with open(fileLocation, 'w') as postFile:
            postFile.writelines([sanitizedPost['title'], '\n', sanitizedPost['innerText']])
            postFile.close()

        fileDetails = {
            'folderLocation': folderLocation,
            'textFilePath': fileLocation,
        }

        detailsArray.append(fileDetails)

    print(detailsArray)
    return detailsArray