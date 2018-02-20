
#Author: Arif Armagan Gozutok 
#Contact: agozutok@turksat.com.tr

import requests
import os
import sys
import glob
import re
from pathlib import Path
from requests_ntlm import HttpNtlmAuth

path = r'path to directory where files are being stored'

temp_list = []
    
files = next(os.walk(path))[2]

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
		
			session.auth = HttpNtlmAuth('TURKSAT\\username','password', session)

			file = open(path + "\\" + filename, 'rb')
    
			bytes = bytearray(file.read())
    
			resp = requests.put('https web page with full path to directory where files are to be stored on sharepoint server' + filename, data=bytes, auth=session.auth)
            
			print "Status response for file #",i+1, "is", resp.status_code
			
			status = 'ok'
			
		break
		
		print '\n'
		
        elif answer == 'n':
            play = False
            break
        else:
            answer = raw_input('Incorrect input. Press \"Y" to continue or \"N" to leave": ').lower()

print '\n'

print 'Program will exit.'

