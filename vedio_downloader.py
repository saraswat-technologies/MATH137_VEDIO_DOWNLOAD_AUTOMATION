import PyPDF2 # pip3 install pikepdf
import urllib.request
import time
# pip install PyPDF2
# pip install requests
# pip install urllib
# Acknoledgement StackOverflow PyhtonBitz.com Automate Boring Stuff .com
print(" Script compiled By Shiv Saraswat")
time.sleep(1)

PDFFile = input("Enter Your pdf file for weekly schedule eg C://Users//XYZ//Desktop//Week6.pdf")
Save_folder=input("Enter your folder directory for vedio download ex. C://Users//XYZ//Week6_Downloaded_vedios note that you should not put file name or mp4 here only folder directory")


PDF = PyPDF2.PdfFileReader(PDFFile)
pages = PDF.getNumPages()
key = '/Annots'
uri = '/URI'
ank = '/A'
link=[]
for page in range(pages):
    print("Current Page: {}".format(page))
    pageSliced = PDF.getPage(page)
    pageObject = pageSliced.getObject()
    if key in pageObject.keys():
        ann = pageObject[key]
        for a in ann:
            u = a.getObject()
            if uri in u[ank].keys():
                link.append(u[ank][uri])
t=0
print(link)
for i in link:
	if i.endswith(".mp4"):
		urllib.request.urlretrieve(i,Save_folder+"//Vedio"+str(t)+".mp4")
		t=t+1
