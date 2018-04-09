import urllib2
import json
import sys

rooturl = sys.argv[1]

itemsurl = "%s/api/items" % rooturl
itemresponse = urllib2.urlopen(itemsurl).read()
itemjson = json.loads(itemresponse)
alltranscriptions = []
total = 0
for i in itemjson:
	colltranscripts = []	
	filesurl = i["files"]["url"]
	filesresponse = urllib2.urlopen(filesurl).read()
	filesjson = json.loads(filesresponse)
	itemid = str(i["id"])
	collectionurl = rooturl + "/items/show/" + itemid
	iet = i["element_texts"]
	collectiontitle = "[No collection title available]"	
	for ie in iet:
		if ie["element"]["name"] == "Title":
			collectiontitle = ie["text"]	
	for f in filesjson:
		fileid = str(f["id"])
		dlink = rooturl + "/scripto/transcribe/"+itemid+"/"+fileid
		element_texts = f["element_texts"]
		text = ""
		for et in element_texts:
			element = et["element"]
			if element["name"] == "Transcription":
				text = et["text"]				
				colltranscripts.append({"url":dlink,"text":text})
				total += 1
	objects = {"transcriptions": colltranscripts, "item_url":collectionurl, "item":collectiontitle}
	alltranscriptions.append(objects)
print "Successfully exported "+str(total)+" transcriptions"
with open("./alltranscripts.json", 'w') as f:
   json.dump(alltranscriptions, f,indent=4, sort_keys=True)
				
				