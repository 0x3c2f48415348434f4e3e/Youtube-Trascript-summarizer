#!C:\Users\benja\AppData\Local\Programs\Python\Python310\python.exe

import nltk
import string
import heapq
import youtube_transcript_api as Y_API
import tkinter #Will use to display final output

#URL must be valid
user = input("Enter youtube URL: ")

#Next lets cut out the important part fromthe URL, which is the v part:

#So a typical youtube URL look slike - https://www.youtube.com/watch?v=liJVSwOiiwg
#The important part for us is the list of characters after the 'v='
#First find the index
indx = user.find("v=")
#Next lets take only that section
parse_video_id = user[indx+2:]
#lets get transcript

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
            pass
        else:
            cleanUpData.append(j)

#print(cleanUpData)
#Next lets create a word frequency list according to the general concept
frequency = {}
for word in cleanUpData:
    count = 0 #set coutner
    for count in range(len(cleanUpData)):
        if(word == cleanUpData[count]):
            #update 
            #update counter
            count+=1
            frequency.update({word:count})
print("\n")
#print(frequency)

#Next lets get the maximum within our frequency object
def _max(obj): #lets pass in our object
    return max(obj.values())

maxStore = _max(frequency)

#division
div = {}
#update object
for i,j in frequency.items():
    j/=maxStore
    div.update({i:j})

#print(div)


#Tokenize into sentences
sen = nltk.sent_tokenize(str(cleanUp))

#set up an empty dictorinary
#Lets use the dict constructor
scores = {}
#Lets find the weighted frequencies
#print("Test\n",sen)

for n in cleanUp: #remove sen and test cleanup
    sen_wordCount = len(nltk.word_tokenize(n))
    sen_wordcount_without_stopwords = 0
    for weight in div:
        if(weight in n.lower()):
            sen_wordcount_without_stopwords +=1
            if(n in scores):
                scores[n] += div[weight]
            else:
                scores[n] = div[weight]
    #scores[n] = scores[n]

print(scores)

#summary
length = float(len(scores)*0.3)
print(length)

summary = heapq.nlargest(int(length),scores, key=scores.get)
res = ''
for word in summary:
    res+= (f" {word}")
summary = ''.join(res)
print("Final summary:", summary)