# Youtube-Scrapper
Python and bash framework to scrape youtube

## Introduction
Youtube has become incredible source of information, where both entertainment as well as vlog/documentary content is added everyday.
These videos and comments sections have data like no other, but information can be hard to obtain from it.   
That said, information scraped or accessed through youtube api can be used to do various datascience projects.
There is also one big challenge in this process. Most of the information in youtube is in the form of video format 
(except video description, comments and statistics). Information from videos can be obtained either using available subtitles 
or auto-generated subtitles to the video. These subtitles can be in SRT/VTT format, and need to be pre-processed to get
sentence based information. Once the subtitles are downloaded and cleaned, they can be fed to NLP/text-mining pipeline to get more 
information from it. This project just does that!

## Procedure
I use youtube API to search for specific keyword and download top 50 videos with maximum number of views.
Following that, the video ID and title are used to generate youtube URLs
These URLs and then used as input to already available 'youtube-dl' tool to download the subtitles. 
Subtitles are then pre-processed to remove time stamps and CSS tags
and following that are fed to NLP pipeline that uses beautiful soup to analyze the data

# Future changes:
Make the program more interactive:
A) Arguments
1. Users developer key
2. Channel
3. Number of videos
4. Key word to search
5. Statistics to download from videos
6. Number of likes
7. Number of Views
8. Number of Comments
9. Advanced NLP features
10. Statistical analysis

Lastly, build a web based flask application for the whole framework.


