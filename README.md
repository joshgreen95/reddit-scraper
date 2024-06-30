# Reddit Video Creator

## Overview

Reddit Video Creator is a Python-based application that automates the creation of engaging video content from top Reddit stories. This tool utilizes various APIs and technologies to generate text-to-speech narration, transcribe audio, create subtitles, and synchronize these elements with pre-recorded gameplay footage. The final output is a video ready for upload to platforms like TikTok, complete with a generated description.

## Features

- **Reddit Integration**: Fetches top stories from Reddit using the Reddit API.
- **Text-to-Speech**: Converts story text to speech using the ElevenLabs API.
- **Audio Transcription**: Uses Whisper to transcribe audio and generate word-level subtitles.
- **Video Editing**: Randomly selects segments from pre-recorded gameplay videos to match the length of the narration.
- **Description Generation**: Utilizes the ChatGPT API to create engaging descriptions for videos.
- **Output**: Produces a fully edited video with subtitles and descriptions for easy upload.

## Technologies Used

- **Python**: Core programming language for the project.
- **Reddit API**: To extract top stories from Reddit.
- **ElevenLabs API**: For generating text-to-speech audio.
- **Whisper**: To transcribe speech into text and generate subtitles.
- **FFMPEG**: For video processing and editing.
- **OpenAI API**: To generate video descriptions.
