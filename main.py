#!C:\Users\benja\AppData\Local\Programs\Python\Python310\python.exe

#Goal - simple a youtube transcript sumarizer

#Tools - Use a Natural language processing to allow computer to understand trasncript, and the youtube-transcript-api to get trnscript

#install and import tools needed - command
#FOR NLTK (Natural langauge tool kit)
#pip install nltk

#For the youtube-transcript-api
#pip install youtube-transcript-api
import nltk
import youtube_transcript_api as Y_API

## we will implment a GUI once we have the logic in place. Never use TKINTER again, use eel.


#allow user to Enter URL
user = input("Enter youtube URL: ")

#Next lets cut out the important part fromthe URL, which is the v part:

#So a typical youtube URL look slike - https://www.youtube.com/watch?v=liJVSwOiiwg
#The important part for us is the list of characters after the 'v='
#First find the index
indx = user.find("v=")
#print(indx+1)
#Next lets take only that section
parse_video_id = user[indx+2:]
print(parse_video_id)
#First lets get transcript
#transcript = Y_API.YouTubeTranscriptApi()