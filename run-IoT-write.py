from write import *
#from MongoUpload import *

personlocx  = raw_input("Please input user\'s two digit x location: ")
personlocy  = raw_input("Please input user\'s two digit y location: ")
print 'Scan tag please:'
writeinput(str(personlocx),str(personlocy),"null","null")
print finduid()
print 'Written successfully to tag'

