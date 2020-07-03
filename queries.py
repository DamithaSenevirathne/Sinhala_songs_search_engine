import json

def multiMatchAggreagation(query, fields=['title','lyrics'], operator ='or'):
    
	res = {
		"size": 10,
		"explain": True,
		"query": {
			"multi_match": {
				"query": query,
				"fields": fields,
				"operator": operator,
				"type": "best_fields"
			}
		},
		"aggs": {
			"Artist Filter": {
				"terms": {
					"field": "artist.keyword",
					"size": 10
				}
			},
                "Music Filter": {
				"terms": {
					"field": "music.keyword",
					"size": 10
				}
			},
                 "Melody Filter": {
				"terms": {
					"field": "melody.keyword",
					"size": 10
				}
			},
                "Lyrics Author Filter": {
				"terms": {
					"field": "lyrics_author.keyword",
					"size": 10
				}
			}
		}
	}
	return json.dumps(res)

def rangeQuaries(query,start,end):

    res ={
    "query": {
			"multi_match": {
				"query": query,

			}
		},
        "bool": {
        "filter": [
            {
            "range": {
                "upload_year": {
                "lte": start
                }
            }
            },
            {
            "range": {
                "upload_year": {
                    "gte": end
                            }
                    }
            }
        ]
        }
    }
    


    return json.dumps(res)


