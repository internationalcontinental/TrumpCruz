import tweepy
from tweepy import OAuthHandler
import sys
#import json
from pymongo import MongoClient

atoken = "719527275834818561-5hY4KfOhczFYeXA73fn6rDQ0yqSSb6k"
asecret = "37Nd9vWGumY0RukEOaid6H7eAwpHJsWPy86m4G0MS3AGI"
ckey = "bWbdkXRfCtn61tWKgAJPzXMJu"
csecret = "w3bJirguKsOtAmoOzjnySvucLSzerTo1zMTXDkExOU7HqpDfsD"

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)

### keywords for the public stream
keyword = "cruz", "trump", "sanders", "clinton"
### initialize blank list to contain tweets
### file name that you want to open is the second argument

class CustomStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        super(tweepy.StreamListener, self).__init__()

        
 
        
 
        # Decode JSON
        

    def on_status(self, status):
        if status.coordinates is not None:
            print status.text , "\n"

            data ={}
            data['text'] = status.text
        #data['user']=status.user
            data['created_at'] = status.created_at
            data['geo'] = status.geo
            data['coordinates']=status.coordinates
            data['source'] = status.source
        #datajson = json.loads(status)
        # Use cooldb database
            client = MongoClient('localhost', 27017)
            db = client.indb
            db.inprimtweets.insert(data)

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener(api))
sapi.filter(track=["cruz", "trump"])
#sapi.filter(locations=[-87.451171875,37.8054439493,-84.4189453125,41.7602577209])
