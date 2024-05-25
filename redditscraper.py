import os
import uuid

import contentsanitizer
import praw

def Scrape():
    CLIENT_ID = '5cf_TVSV3HJkB9EXkqye7Q'
    CLIENT_SECRET = 'lkmVB-k71REExiLqsY-Qmnot1UTTYQ'
    CLIENT_USERNAME = 'ProfessionalMug'
    
    with open('pw.env', 'r') as f:
        CLIENT_PASSWORD = f.read().strip()
    
    CLIENT_UA = 'Scraper/0.0.1'
    
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = CLIENT_UA,
        username = CLIENT_USERNAME,
        password = CLIENT_PASSWORD
    )

    subreddit = reddit.subreddit('AITAH')
    
    top_posts = subreddit.top(limit=3)

    folderUuid = str(uuid.uuid1())
    folderLocation = './posts/' + folderUuid + '/'
    os.mkdir(folderLocation)

    for post in top_posts:
        sanitizedPost = contentsanitizer.Sanitize(post.title, post.selftext)
        print(sanitizedPost['title'])
        fileLocation = folderLocation + sanitizedPost['title'] + '.txt'
        
        with open(fileLocation, 'w') as postFile:
            postFile.writelines([post.title, '\n', sanitizedPost['innerText']])
            postFile.close()

    return folderLocation

