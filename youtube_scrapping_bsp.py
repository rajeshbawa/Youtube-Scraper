import requests
import json 
import pandas  

key = 'AIzaSyCcD51hH8s5Dc4Rqt-uD3PDWDtRZi1MXpc'
url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=50&order=viewCount&q=tiny+house&type=video&videoDefinition=high&key="+key
content = json.loads(requests.get(url).text)

def get_youtoube_content(content):
    id = []
    kind=[]
    description = []
    title = []
    time =[]
    for i in content["items"]:
        a=i["id"]
        b=i["snippet"]
        id.append(a["videoId"])
        kind.append(a["kind"])
        description.append(b["description"])
        title.append(b["title"])
        time.append(b["publishedAt"])
    data = pandas.DataFrame({"id":id, "type":kind,"description":description ,"title":title,"time":time })
    return(data)

x = 10
data=get_youtoube_content(content)