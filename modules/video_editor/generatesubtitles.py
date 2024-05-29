import os

from pydub import AudioSegment
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

import whisper

def GenerateSubtitles(details, videoClip):
    font = 'arial'
    fontSize = 42
    color = 'white'
    backgroundColor = None
    subtitlePosition = ('center')

    def Transcribe(path):
        model = whisper.load_model("base")
        results = model.transcribe(path, word_timestamps=True)
        return results

    def ExtractTimings(results):
        wordTimings = []

        for segment in results['segments']:
            words = segment.get('words', None)
            if words:
                for wordInfo in words:
                    startTime = wordInfo['start']
                    endTime = wordInfo['end']
                    word = wordInfo['word']

                    wordTimings.append((startTime, endTime, word))
        return wordTimings

    def GenerateTextClips(wordTImings):
        textClips = []

        for startTime, endTime, word in wordTImings:
            duration = endTime - startTime
            textClip = TextClip(word, 
                                font=font,
                                fontsize=fontSize,
                                color=color,
                                )
            textClip = textClip.set_position(subtitlePosition)
            textClip = textClip.set_start(startTime)
            textClip = textClip.set_duration(duration)

            textClips.append(textClip)
        return textClips 

    audio = AudioSegment.from_mp3(details['audioPath'])
    audio.export('temp.wav', format='wav')
    transcription = Transcribe('temp.wav')
    wordTimings = ExtractTimings(transcription)
    textClips = GenerateTextClips(wordTimings)

    finalVideo = CompositeVideoClip([videoClip] + textClips)
    return finalVideo


