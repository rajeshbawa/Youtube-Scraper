import os
import argparse
import random
import subprocess
#import webvtt
#import youtube_dl
import googleapiclient
import oauth2client
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from bs4 import BeautifulSoup

os.chdir("/Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool")
DEVELOPER_KEY = 'AIzaSyCcD51hH8s5Dc4Rqt-uD3PDWDtRZi1MXpc'
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)
ids = 'EH8R5eB8ioo'
#viewCount = 1000000000
#ids = '9bZkp7q19f0,eHvccEXfacM'
print("\033[1m")
keyword = str(input("Please input the words you want to search for:\n"))
print(keyword)
print("\033[0m")
search = youtube.search().list(q=keyword, type = "video", 
part="id,snippet", maxResults=50).execute()
results = youtube.videos().list(id=ids, part='snippet').execute()
captions = youtube.captions().list(part="snippet",videoId=ids).execute()
#captions_download = youtube.captions().download(id = "p1RlVpkbLVxp6OM_6EWQCIeaOCEdTtrR", tfmt=tfmt).execute()
videos = {}
for search_result in search.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        #videos.append("%s" % (search_result["id"]["videoId"]))
        videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]


#print("Videos:\n", "\n".join(videos), "\n")
#s = ','.join(videos.keys())
#print(s)


print("\033[1m")
print("The titles of videos being downloaded are")
print('\033[92m')
for i in videos:
    print(videos[i])  


print("\033[0m")

urls = []
for i in videos:
    urls.append("https://www.youtube.com/watch?v=" + i)
    

#urls
os.chdir("/Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/youtube-dl/bin")
thefile = open('urls.txt', 'w')

for i in urls:
    thefile.write("%s\n" %i)


thefile.close()
print("\033[1m" + "The transcripts of videos are being downloaded" + "\033[0m")
subprocess.call("/Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/download_subtitles.sh", shell=True)

print("\033[0m" + "Job is done! \n Please check the folder for results" + "\033[0m")
'''
calling youtube-dl program from bash 
and then calling that bash program in python
to download the subtitles or captions (autocaptions)
###
cat urls.txt | while read line
do
youtube-dl --write-sub \
--write-auto-sub \
--skip-download \
$line
done
###
'''
##getting data from the transcripts of the youtube
#os.chdir("/Users/rajesh13/Documents/health_datascience/Youtube_scrapping_tool/youtube-dl/bin/subtitles")
#cap1 = webvtt.WebVTT().read("Open Concept Modern Tiny House with Elevator Bed-lHjJd4tkvSU.en.vtt")
'''
regex for replacing the effed up webvtt file so that its just normal text
to do in bash
sed -e 's/[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9].*%//g' \
-e 's/<*>//g' \
-e "s/<c.colorE5E5E5//g" \
-e "s/<c.colorCCCCCC//g" \
-e "s/<\/c<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g" \
-e "s/<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g" \
-e "s/<\/c//g" file
'''
'''
to automate the above regex to get actual transcript/
for f in *.vtt; do cat "$f" | \
sed -e 's/[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9].*%//g' \
-e 's/<*>//g' \
-e 's/<c.colorE5E5E5//g' \
-e 's/<c.colorCCCCCC//g' \
-e 's/<\/c<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g' \
-e 's/<[0-9][0-9]:[0-9][0-9]:[0-9][0-9].[0-9][0-9][0-9]<c//g' -e 's/<\/c//g' \
| grep -ve "[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" \
> transcript/"`basename "$f" .en.vtt`.txt"; continue; done
'''
'''
Things to do:
1. Search for keyword in youtube using API
2. Select the top 10 videos
3. Download the transcript of the video
4. text-mine those videos
####benchmark
1. Use list, np.array, trees and dictionary etc and benchmark
2. Interactive
3. Unit testing
'''

'''    
for result in results.get('items', []):
    print(result['id'])
    print(result['snippet']['description'])
    print('-----')

'''
###textmining using beautiful soup
###using 10 video transcripts
