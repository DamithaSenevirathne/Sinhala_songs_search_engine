# Sinhala_songs_search_engine

## Description

A simple search engine for Sinhala songs whcih supports both English & Sinhala queries. Search engine was built based on ElasticSearch and thi engine supports both simple and advance querie such as ranged queris faceting.

## Requirements

1. Python 3.8.3
2. AWS ElasticSearch
2. elasticsearch 7.8.0

## Describing the data

Dataset was extracted from http://geepadura.blogspot.com/ and extracted data contains following fields

```
{
   "lyric_id": 158,
   "title": "විරාග රාගය - අමරසිරි පීරිස්, අමල් පෙරේරා  |  Viraga ragaya - Amarasiri Peiris, Amal Perera - sinhala lyrics",
   "title_sinhala": "විරාග රාගය - අමරසිරි පීරිස්, අමල් පෙරේරා",
   "title_english": "Viraga ragaya - Amarasiri Peiris, Amal Perera - sinhala lyrics",
   "artist": "අමරසිරි පීරිස්, අමල් පෙරේරා",
   "music": "සුරේෂ් මාලියද්ද",
   "melody": "",
   "lyrics_author": "බන්දුල නානායක්කාරවසම්",
   "lyrics": "විරාග රාගය අතරේ තනි වූ ආලය ...",
   "upload_year": 2018,
   "upload_month": 2
 },
 
```

## How to Setup and RUN

1. Install ElasticSearch on the local machine.
2. create python 3.8.3 virtual environment.
3. Add elasticsearch to python using pip<br />
      ```pip install elasticsearch```
4. Start ElasticSearch service by executing command<br />
      ```sudo /etc/init.d/elasticsearch start```
5. Navigate to the project diractory & type <br />```python app.py```


## Supported Features

1. Supports both sinhala & English queries
2. Can search by title, title_sinhala, title_english, artist, music, melody, lyrics_author, lyrics, upload_year
3. Range queries supported
   example - can search artist's songs between a time period
