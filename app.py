from elasticsearch import Elasticsearch
from elasticsearch import helpers
import json
from queries import multiMatchAggreagation
from queries import rangeQuaries

es = Elasticsearch(HOST="http://localhost",PORT=9200)

def createIndex(index):
    return es.indices.create(index=index,ignore=400)

def getData():
    with open('text_data_updated.json','r') as f:
        data = json.loads(f.read())
        return data


def cleanOutput(string):

    out = ''

    for i in string:

        if i!='\n':

            out += i

    return out

def boostedSearch(search_query):
    
    artist_keywors = ['Artist','Singer','ගායනය']
    melody_keywords = ['melody','melody','තනු']
    music_keywors = ['Music','music','composer','සංගීතය']
    
    
    # add  length

    boost = {
        "title_sinhala":1,
        "title_english":1,
        "artist":1,
        "music":1,
        "melody":1,
        "lyrics_author":1,
        "lyrics":1
        }

    if (len(search_query) > 3):

        boost["title_sinhala"] += 1
        boost["melody"] += 1
        boost["lyrics_author"] += 1
        boost["lyrics"] += 10

        for key in artist_keywors:
            if(key in search_query):
                boost["artist"] += 1

        for key in music_keywors:
            if(key in search_query):
                boost["music"] += 1

        for key in melody_keywords:
            if(key in search_query):
                boost["melody"] += 1

              
    field_1 ="title_sinhala^{}".format(boost["title_sinhala"])
    field_2 ="title_english^{}".format(boost["title_english"])
    field_3 ="artist^{}".format(boost["artist"])
    field_4 ="music^{}".format(boost["music"])
    field_5 ="melody^{}".format(boost["melody"])
    field_6 ="lyrics_author^{}".format(boost["lyrics_author"])
    field_8 ="lyrics^{}".format(boost["lyrics"])

        
    boostedFields = [field_1,field_2,field_3,field_4,field_5,field_6,field_8]
    res = es.search(index="index",body=multiMatchAggreagation(search_query,boostedFields))
    return res




def extractData(dataArray,indexName):
    for lyricData in dataArray:

        lyric_id = lyricData.get("lyric_id",None)
        title = lyricData.get("title",None)
        title_sinhala = lyricData.get("title_sinhala",None)
        title_english = lyricData.get("title_english",None)
        artist = lyricData.get("artist",None)
        music = lyricData.get("music",None)
        melody = lyricData.get("melody",None)
        lyrics_author = lyricData.get("lyrics_author",None)
        lyrics = lyricData.get("lyrics",None)
        upload_year = lyricData.get("upload_year",None)



        yield {
            "_index": indexName,
            "_source": {
                "lyric_id": lyric_id,
                "title_sinhala": title_sinhala,
                "title_english": title_english,
                "artist": artist,
                "music": music,
                "melody": melody,
                "lyrics_author": lyrics_author,
                "lyrics": lyrics,
                "upload_year":upload_year
            },
        }


def initIndex():
    createIndex(index="index")  

initIndex()

helpers.bulk(es,extractData(getData(),"index"))

#print (rangeQuaries("ආත්මා ලියනගේ",2014,2019))

print ("##---Started--##")

while (True):
    
    initIndex()
    helpers.bulk(es,extractData(getData(),"index"))

    input_ = input("Enter queries : " )

    if input_ == "search-by-artist":

        artist_ = input("Enter Name : "  )
        res = es.search(index="index",body={"from":0,'size':10,"query":{"match":{"artist":artist_}}})
        query = res['hits']['hits']
        # i['_source']["lyric_id"]
        for i in query:
            print (cleanOutput(i['_source']["title_sinhala"]))

    elif input_ == 'boosting':

        x = []

        res = boostedSearch("title_sinhala melody ආත්මා ලියනගේ")
        query = res['hits']['hits']
        # i['_source']["lyric_id"]
        for i in query:

            if i['_source']["lyric_id"] in x:

                return_ = 1
            
            else:

                print ((i['_source']["title_sinhala"],i['_source']["artist"],i['_source']["melody"]))
                x.append(i['_source']["lyric_id"])


    elif input_ == 'latest-by-artist':

        artist_ = input("Enter Name : "  )
        res = es.search(index="index",body={"from":0,'size':10,"query":{"match":{"artist":artist_}}})
        query = res['hits']['hits']
        # i['_source']["lyric_id"]
        for i in query:
            print (i['_source']["title_sinhala"])

    
    elif input_ == 'cust':


        field_ = input("Enter field : "  )
        search = input("Enter search : "  )
        res = es.search(index="index",body={"from":0,'size':10,"query":{"match":{str(field_) :search}}})
        query = res['hits']['hits']

        for i in query:
            print (i['_source']["title_sinhala"])
