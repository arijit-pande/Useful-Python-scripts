#playing around with reddit api :)

import requests
import json
user_name=raw_input("Enter username:")
url='http://www.reddit.com/user/%s/comments/.json'%user_name
hdr= { 'User-Agent' : 'this is a sample request' }
r=requests.get(url,headers=hdr) #header because http://stackoverflow.com/questions/13213048/urllib2-http-error-429
data_fetch=json.loads(r.text)
total_comments=(len(data_fetch[u'data'][u'children']))
print "Total comments:"+str(total_comments)
max_karma_comment_score=0
for i in range(0,total_comments):
    max_karma_comment_score=max(max_karma_comment_score,data_fetch[u'data'][u'children'][0][u'data'][u'score'])
print "Maximum karma on a comment by %s:"%user_name+str(max_karma_comment_score)
