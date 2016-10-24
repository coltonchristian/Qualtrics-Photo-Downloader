import urllib.request #to fetch URLs
import time #to create a delay so that the server you're downloading from doesn't get overloaded
import os #to create path names to save the files to
fh=open('filename.txt') #where filename.txt is a text file containing the link to a single photo on each line
fhlines=fh.readlines() #read in the URLs
count=0 #set count to 0
for line in fhlines:
    filename = 'image%d'%(count) #filename with a digit that is specified by count attached
    resource = urllib.request.urlopen(line) #open a connection
    output = open(os.path.join('folder', filename  + '.' + 'jpg'),"wb") #where folder is the path to the folder where the files should be saved. This line concatenates the path with the filename created above and then opens a jpg under that name
    output.write(resource.read()) #download the file from the open connection
    output.close() #close the file
    resource.close() #close the connection
    count=count+1 #add one to the counter so that the next file is named sequentially
    time.sleep(5) #wait 5 seconds before downloading the next file