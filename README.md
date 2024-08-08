# Reddit Video Creator

## Overview

Reddit Video Creator is a Python-based application that automates the creation of AI Generated videos and descriptions which are uploadable to TikTok. 

## Workflow

- **Reddit Scraper**: Scrapes from Reddit using the PRAW Reddit Wrapper, allows user input for Subreddit and number of videos to compile.
- **Text-to-Speech**: Converts story text to speech using the ElevenLabs API.
- **Audio Transcription**: Uses Whisper to transcribe audio and generate word-by-word subtitle tracks.
- **Video Editing**: Randomly selects segments from user video (think minecraft parkour) to match the length of the narration and overlays subtitles.
- **Description Generation**: Uses ChatGPT API to create description and hashtags for videos.
- **Output**: Produces an edited video with subtitles and descriptions for easy upload.

## Technologies Used

- **Python**: ...Obviously.
- **Praw**: To extract Reddit posts.
- **ElevenLabs API**: For generating text-to-speech audio.
- **OpenAI's Whisper**: To generate subtitles.
- **PyMovie**: For video processing and editing.
- **ChatGPT**: To generate video descriptions.

## Prerequisites
This project needs FFMPEG and ImageMagik

## Getting Started
1. Clone the Repo
   ```sh
   git clone https://github.com/joshgreen95/reddit-scraper.git
   ```
1.5. Collect API Keys, ready for prompt. If you dont have any of these, make the accounts
```Needed Keys
   Reddit API Client ID
   Reddit API Secret Key
   Your Reddit Username and Password ...Obviously
   Elevenlabs XI Api Key
   ChatGPT Api Key
```
2. Install PiP Dependencies
``` sh
Praw
Moviepy
Whisper
openai
```
3. Place Videos into Videos folder ===Try to use videos over 10 minutes and in the correct aspect ratio.==
4. Run the Main.py Script and follow prompts.

