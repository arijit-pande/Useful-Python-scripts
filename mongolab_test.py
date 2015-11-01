#Just a script to test if mongolab connection is up or not

import pymongo
import sys
MONGO_URI="ENTER YOUR MONGOLAB URI HERE"
def main():
    f_log=open("log.txt","w")
    try:
        conn=pymongo.MongoClient(MONGO_URI)
    db=conn.dummydb
    f_log.write("connection opened with:" +MONGO_URI+" Connection address:"+conn"\n")   
    except:
        print sys.exc_info()
    
if __name__=='__main__':
    main()
