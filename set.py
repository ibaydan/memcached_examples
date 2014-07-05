#!/bin/python

#import library
import memcache

#Create object and make connection to the memcached server
mc = memcache.Client(['127.0.0.1:11211'], debug=0)



#set values with keys
mc.set("ismail", "baydan")

#and get the value
value = mc.get("ismail")

#print the value
print(value)




#set another value
mc.set("another_key", 3)

#and delete it
mc.delete("another_key")

#get value withh key which previously used for store
obj = mc.get("some_key")

#print the value
print(obj)
