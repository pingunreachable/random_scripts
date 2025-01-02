#!python3

import zipfile, os

#open existing zip file that was already created
folderbkup = zipfile.ZipFile("D:\\Archive.zip",'a')

#Walk directory of the actual folder itself
for folderName, subfolders, filenames in os.walk("D:\\DocoFolder"):
	print('The current folder is ' + folderName)
	folderbkup.write(folderName, compress_type=zipfile.ZIP_DEFLATED)
	
	for subfolder in subfolders:
		print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
		#folderbkup.write(os.path.join(folderName, subfolder))
	
	for filename in filenames:
		print('FILE INSIDE ' + folderName + ': '+ filename)
		folderbkup.write(os.path.join(folderName, filename))
		print('')

folderbkup.close()
