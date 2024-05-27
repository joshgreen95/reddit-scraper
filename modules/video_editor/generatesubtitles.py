import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip


import pickle

def GenerateSubtitles(details, videoClip):
    def ReadTextFile(details):
        with open(details['textFilePath'], 'r') as file:
            lines = file.readlines()

        transcript = ' '.join([line.strip() for line in lines if line.strip()])
        transcript = transcript.split()
        
        return transcript
    
    def CalculateDurationPerWord(words, videoClip):
        word_factor = 0.2
        video_factor = 0.8
        videoDuration = videoClip.duration

        totalWords = len(words)
        wordDurations = []

        for word in words:
            duration = (len(word) * word_factor + videoDuration * video_factor) / totalWords
            wordDurations.append(duration)

        return wordDurations
    
    def CreateWordClips(words, wordDurations, videoClip):
        wordClips = []
        currentTime = 0

        fontSize = 64
        color = 'white'
        font = 'Arial'

        for word, duration in zip(words, wordDurations):
            textClip = TextClip(word, fontsize=fontSize, color=color, font=font)
            textClip = textClip.set_position(('center'))
            textClip = textClip.set_duration(duration)
            textClip = textClip.set_start(currentTime)

            wordClips.append(textClip)
            currentTime += duration
        
        return wordClips
    
    def TranscribeAudio(audioFile):
        recognizer = sr.Recognizer()
        audio = AudioSegment.from_file(audioFile)

        segments = split_on_silence(audio, min_silence_len=500, silence_thresh=-40)
        transcript = []

        for segment in segments:
            with sr.AudioFile(segment) as source:
                audioData = recognizer.record(source)
                text = recognizer.recognize_google(audioData)
                transcript.append(text)

        return ' '.join(transcript).split()

    audioTranscript = TranscribeAudio(details['audioPath'])
    
    transcript = ReadTextFile(details)
    durations = CalculateDurationPerWord(audioTranscript, videoClip)
    wordClips = CreateWordClips(audioTranscript, durations, videoClip)
    
    videoWithSubtitles = CompositeVideoClip([videoClip] + wordClips)

    return videoWithSubtitles;