#!C:\Users\benja\AppData\Local\Programs\Python\Python310\python.exe

#Goal - simple a youtube transcript sumarizer

#Tools - Use a Natural language processing to allow computer to understand trasncript, and the youtube-transcript-api to get trnscript

#install and import tools needed - command
#FOR NLTK (Natural langauge tool kit)
#pip install nltk

#For the youtube-transcript-api
#pip install youtube-transcript-api
import nltk
import string
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
#print(parse_video_id)
#lets get transcript
'''
try:
    transcript = Y_API.YouTubeTranscriptApi.get_transcript(parse_video_id)
    print(transcript)
except Y_API.youtube_transcript_api._errors.TranscriptsDisabled:
    print("Subtitles Disabled. Try another URL")
'''
transcript = []
transcript = Y_API.YouTubeTranscriptApi.get_transcript(parse_video_id)
#print(transcript)

#download stopwords
#Check to see if resource is already installed
#nltk.download("stopwords")


#Data returned is a list
#Also want to remove any unimportant words to make life easier
stop_w = nltk.corpus.stopwords.words('english') #Gte stop words
#print(f"\n{stop_w}")
#next get puncturations out
punc = string.punctuation
#print(punc)

'''remeber that this gets transcript, so by defualt, we will have some
numbers, well lets remove those numbers'''

#Create new list
cleanUp = []

for i in range(len(transcript)):
    cleanUp.append(transcript[i].get("text"))

#print("First step\n",cleanUp, "\n\n")

'''next lets delete some words in the list and  it will create a new
list for use'''
print(cleanUp,"\n\n")
cleanUpData = []
for i in cleanUp:
    local_store = i.split(" ")
    for j in local_store:
        if(j in stop_w or j in punc or j.upper() in stop_w or j.lower() in stop_w): #remeber to check for lower and uppercase just to be sure
            #cleanUp.remove(j)
            #print("Remove:",j)
            #cleanUpData.append(j)
            pass
            #local_store.remove(j)
        #removed.append()
            #cleanUp.remove(j)
        else:
            cleanUpData.append(j)

print(cleanUpData)
#Next lets create a word frequency list according to the general concept
frequency = {}
for word in cleanUpData:
    for count in range(len(cleanUpData)):
        if(word == cleanUpData[count]):
            #update 
            pass