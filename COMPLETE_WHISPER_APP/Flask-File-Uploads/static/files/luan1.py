""""
import whisper

#Importing Pytube library
import pytube
# Reading the above Taken movie Youtube link
video = 'https://www.youtube.com/watch?v=-LIIf7E-qFI'
data = pytube.YouTube(video)
# Converting and downloading as 'MP4' file
audio = data.streams.get_audio_only()
audio.download()

model = whisper.load_model("base")
text = model.transcribe("I will find YouI will Kill You Taken Movie best scene ever liam neeson.mp4", fp16=False)
    #printing the transcribe
print(text['text'])
"""