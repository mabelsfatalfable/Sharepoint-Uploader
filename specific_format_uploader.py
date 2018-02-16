
#Author: Arif Armagan Gozutok 
#Contact: agozutok@turksat.com.tr

import requests
import os
import sys
import glob
import re
from pathlib import Path
from requests_ntlm import HttpNtlmAuth

path = r'Directory path of the folder where files are being stored' #CHANGE THIS

temp_list = []
    
files = next(os.walk(path))[2]
#print "File array:"
#print files
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

print 'Files with .pdf extension:'
for file_pdf in os.listdir(path):
    if file_pdf.endswith(".pdf"):
        print(os.path.join(path, file_pdf))
print '\n'

print 'Files with .docx extension:' 
for file_docx in os.listdir(path):
    if file_docx.endswith(".docx"):
        print(os.path.join(path, file_docx))
print '\n'
		
print 'Files with .xlsx extension:' 
for file_xlsx in os.listdir(path):
    if file_xlsx.endswith(".xlsx"):
        print(os.path.join(path, file_xlsx))
print '\n'
		
print 'Files with .ppt extension:' 
for file_ppt in os.listdir(path):
    if file_ppt.endswith(".ppt"):
        print(os.path.join(path, file_ppt))
print '\n'
		
regex = re.compile(r'\.pdf')
pdf_files = filter(regex.search, files)
print(pdf_files)	
regex = re.compile(r'\.docx')
docx_files = filter(regex.search, files)
print(docx_files)	
regex = re.compile(r'\.xlsx')
xlsx_files = filter(regex.search, files)
print(xlsx_files)	
regex = re.compile(r'\.ppt')
ppt_files = filter(regex.search, files)
print(ppt_files)	

files = pdf_files + docx_files + xlsx_files +ppt_files

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
		
		print 'Script will start uploading... \n'
		
		print 'Check if status codes are 200 (200 OK - The request has succeeded) ' 
		print 'or 201 (201 CREATED - The request has been fulfilled and has resulted'
		print 'in one or more new resources being created). If not, try again. \n'
		
		for i in range(0, len(files)):

			filename = files[i]

			session = requests.Session()
		
			session.auth = HttpNtlmAuth('SharepointDomain\\username','password', session)

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

