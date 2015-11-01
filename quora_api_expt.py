from quora import User
user_name=raw_input("Enter fullname(case Sensitive)(Enter '-'in place of space)")
user=User(user_name)
print user.stats
try:
    print "No of people followed:"+str(user.stats['following'])
    print "No of followers"+str(user.stats['followers'])    
except:
    print "Exception occured."
