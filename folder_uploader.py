import requests
import os
import sys
from requests_ntlm import HttpNtlmAuth
import glob

path = 'C:\Python27' #CHANGE THIS

    
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

#print 'Do you want to continue to upload? (Y)es or (N)o'

#print 'Press (Y) to continue...'

status = []

play = True

while play:
	
    answer = raw_input('Do you want to continue to upload corresponding files? (Y)es or (N)o: \n').lower()
	
    while True:
        if answer == 'y':
		
		for i in range(0, len(files)):

			filename = files[i]

			session = requests.Session()
		
			session.auth = HttpNtlmAuth('SharepointDomain\\username','password', session) #CHANGE THIS

			file = open(path + "\\" + filename, 'rb')
    
			bytes = bytearray(file.read())
    
			resp = requests.put('Full directory path including hostname where the files will be uploaded' + filename, data=bytes, auth=session.auth)
            
			print "Status response for file #",i+1, "is", resp.status_code
			
			status = 'ok'
			
		break
		
        elif answer == 'n':
            play = False
            break
        else:
            answer = raw_input('Incorrect input. Press \"Y" to continue or \"N" to leave": ').lower()



print 'Program will exit.'


