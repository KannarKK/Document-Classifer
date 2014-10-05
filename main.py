import glob
import math
import nltk
#nltk.download()
from nltk.corpus import stopwords
from stemming.porter2 import stem

#from docx import *

# Open the .docx file
#document = opendocx('A document.docx')

def cleanupDoc(s):
    stopset = set(stopwords.words('english'))
    token=set()
    #for tok in s:
   #	if tok.lower() not in stopset and len(tok)>2:
#	  token.add(tok.lower())
    cleanup =[]
    for tok in s:
	if(tok.lower() not in stopset and len(tok)>2):
		cleanup.append(tok.lower())	     
    #cleanup= [tok.lower() for tok in s not in stopset and len(tok)>2]
    for i in s:
	 if i not in stopset:
		token.add(i)
    return cleanup

def clean(s):
  stopset  = set(stopwords.words('english'))
  cleaned = set()
  for term in s:
	if(len(term)>2):
	   cleaned.add(term.lower())
  cleaned = s.difference(stopset)
  return cleaned

line=''
s=set()
flist=glob.glob(r'*.txt') #get all the files from the d`#open each file >> tokenize the content >> and store it in a set
for fname in flist:         
    #print flist
    tfile=open(fname,"r")
    line=tfile.read() # read the content of file and store in "line"
    tfile.close() # close the file
    s=s.union(set(line.split(None))) # union of common words
 
#s=sorted(s) # sorts the content alphabetically
#s = cleanupDoc(s) 
s = clean(s)
s= sorted(s) 

i=0
ct=0
tf_line=''          
doc_counts=[]  #number of documents in which each word is found
for term in s: #takes each term in the set 
    doc_counts.append(0)
    
    for fdoc in flist: # counts the no of times "term" is encountered in each doc
        
        doc=open(fdoc)
        line=doc.read()
        doc.close()
        ct=line.count(str(term)) #counts the no. of times "term" is present in the file
        tf_line+=str(ct)+',' #prints the count in each doc seperated by comma
        if (ct>0):              #counts no of docs in which 
            doc_counts[i]+=1    #this "term" is found
    i+=1
    tf_line=tf_line.strip()+'\n'    
 
idf=[]  #inverse document frequency      
weights=[]      #weight
total_docs=len(flist)   #total number of documents
print i
i=0
cnt= []
y = set(stopwords.words('english'))
for term in y:
	print y,'\t'
#for term in s:
#     for fdoc in flist:
for doc_count in doc_counts:    #takes the 1st doc count
    #print(str(total_docs)+" "+str(doc_count))
    if(doc_count==0):
	idf.append(0)
    else:
    	idf.append(math.log(total_docs/doc_count)) #calculates idf for each "term"
    #print(idf[i])
    weights.append(idf[i]*doc_count) #calculate weight of the term
    i+=1
 
 
 
final_line='TERM'+','       
i=1
for f in flist:
    final_line+='D'+str(i)+'  '+','
    i+=1
final_line+=','+'IDF'+','+'TF-IDF\n'
 
 
tf_arr=tf_line.split('\n')
 
 
 
i=0
for term in s:
    final_line+=term+','+tf_arr[i]+','+str(round(idf[i],2))+','+' '+str(round(weights[i],2))+','+'\n'
    i+=1
 
fdoc="tftable.csv"
outfile=open(fdoc,"w")
outfile.write(final_line)
outfile.close()
 
print "DONE"
