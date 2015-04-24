import os

os.chdir(os.path.expanduser("~/testing/")) #Changing dir to your unix users home directory
sdra = file('output.txt', 'r') #Loads ~/output.txt as read only
sdrb = file('fixed.txt', 'w+') #Creates ~/fixed.txt if file does not already exist then loads as write only
oread = sdra.read()
stage1 = oread.translate(None, '[]').split()
for line in stage1:
        if not "-" in line: #if file does not contain '-'
                sdrb.write(line+"\n")#Writes modified output to fixed.txt line by line as well as adding \n to each line

sdrb.close() #closes fixed.txt
sdra.close() #closes output.txt



                
