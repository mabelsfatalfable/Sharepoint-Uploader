import requests
import os
import sys
from requests_ntlm import HttpNtlmAuth
import glob

path = 'path to directory including files or documents to upload'

    
files = next(os.walk(path))[2]
print "File array:"
print files
print "\n"
print 'Total number of files in', path, 'is', len(files)
print "\n"
print "Files listed in directory:"
print "\n"
i = 0
for i in range(0,len(files)):
    print(path+"\\."+files[i])
    i += 1
print "\n"
   

#temp_list = glob.glob('single_file_sharepoint.py')

#temp_list = glob.glob("C:\Python27\Scripts\*")

#print(glob.glob("C:\Python27\Scripts\*"))

#print("\n")
#print(temp_list)
#print("\n")
#print(len(temp_list))
#print("\n")

for i in range(0, len(files)):

    filename = files[i]

    session = requests.Session()
    
    session.auth = HttpNtlmAuth('SharepointDomain\\username','password', session)

    file = open(path + "\\" + filename, 'rb')
    
    bytes = bytearray(file.read())
    
    resp = requests.put('Full directory path including hostname where the files will be uploaded' + filename, data=bytes, auth=session.auth)
            
    print "Status response for file #",i+1, "is", resp.status_code



    
