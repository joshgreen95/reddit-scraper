import os
import random

from moviepy.editor import VideoFileClip, AudioFileClip

from .generatesubtitles import GenerateSubtitles

def Edit(details, videoPath, format):
    
    def CutAndAddAudio(audioPath, videoPath):
        #Load video and audio clips
        videoClip = VideoFileClip(videoPath)
        audioClip = AudioFileClip(audioPath)

        #Get duration of audio and video
        videoDuration = videoClip.duration
        audioDuration = audioClip.duration

        #If Audio clip is longer than video clip throw error
        if audioDuration > videoDuration:
            raise ValueError('Audio clip is longer than video clip!')

        #Generate random start time from video
        startTime = random.uniform(0, videoDuration - audioDuration)

        #Cut the video to length of audio clip
        cutVideo = videoClip.subclip(startTime, startTime + audioDuration)

        #Set Audio
        cutVideo = cutVideo.set_audio(audioClip)
        
        print(cutVideo)
        return cutVideo

    cutVideo = CutAndAddAudio(details['audioPath'], videoPath)
    cutVideo = GenerateSubtitles(details, cutVideo)
    #Write to File
    outputPath = details['textFilePath'] + format
    cutVideo.write_videofile(outputPath, codec="libx264", audio_codec="aac")