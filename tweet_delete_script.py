import twython
import time
app_key = "XXXXXX"
app_secret = "XXXXXX"
oauth_token = "XXXXXX"
oauth_token_secret = "XXXXXX"
count=0
profile_name=raw_input()
twitter = twython.Twython(app_key, app_secret, oauth_token, oauth_token_secret)
while 1:
    user_timeline = twitter.get_user_timeline(screen_name=profile_name, count=10)
    count = len(user_timeline)
    if count==0:
        print "No more tweets to delete"
        break
    for tweets in user_timeline:
        print tweets['text'] 
        twitter.destroy_status(id=tweets['id'])
    count=count+10
    print str(count)+ " tweets deleted..sleeping"
    time.sleep(10)
    
