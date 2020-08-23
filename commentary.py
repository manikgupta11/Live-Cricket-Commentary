import requests
import bs4
import time
import os
i=0

res=requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
soup=bs4.BeautifulSoup(res.text,'lxml')
matchid=soup.find("div",{"cb-lv-scrs-col text-black"})
#results=soup.findAll("div",{'class':"cscore_score "})
url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
r=requests.get(url).json()
r1=r.get('matches')

for match in r1:
	print( match['match_id'],end=": ")
	print( match['series_name'])
print("\nEnter match id")
mid = input()
while True:
	#res=requests.get('https://www.cricbuzz.com/live-cricket-scores/23446/')
	
	#url = "http://mapps.cricbuzz.com/cbzios/match/22574" 
	url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
	r = requests.get(url).json()
	prevscore=0; prevwkt=0
	currscore=0; currwkt=0
	
	r1=r.get('matches')
	list2=[]

	for match in r1:
		if match['match_id'] == mid:
			list1=match.get('bat_team')
			#list1=match['bat_team']
			list2=list1.get('innings')
			#print(list2)
	for inng in list2:
		prevscore=inng['score']
		prevwkt=inng['wkts']
		print("Score after "+str(i)+" seconds: "+prevscore+"/"+prevwkt)

	time.sleep(10)
	i+=10

	url = "http://mapps.cricbuzz.com/cbzios/match/livematches"
	r = requests.get(url).json()

	r1=r.get('matches')
	list2=[]

	for match in r1:
		if match['match_id'] == mid:
			list1=match.get('bat_team')
			list2=list1.get('innings')
			#print(list2)
	for inng in list2:
		currscore=inng['score']
		currwkt=inng['wkts']

		if( int(currscore) - int(prevscore) ==4 ):
			os.system("xdg-open commentary_four.mp3")
		elif( int(currscore) - int(prevscore) ==6 ):
			os.system("xdg-open commentary_six.mp3")
		elif( int(currwkt) - int(prevwkt) ==1 ):
			os.system("xdg-open commentary_out.mp3")
