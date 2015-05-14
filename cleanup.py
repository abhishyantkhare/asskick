import json

names = []
i = 0
with open('/run/media/abhishyant/Storage/Music/torrent_files/albumlist.txt') as albumlist:
	with open('/run/media/abhishyant/Storage/Python/music_torrent_scripts/asskick/listtwo.txt','a') as writelist:
		for line in albumlist:
			if line is not '':
				while(line.find(')') > -1):
					start = line.find('(')
					end = line.find(')')+1
					sub = line[start:end]
					line = line.replace(sub,'')
					line = line.replace('(','')
					line = line.replace(')','')
				while(line.find('[') > -1):
					start = line.find('[')
					end = line.find(']')+1
					sub = line[start:end]
					line = line.replace(sub,'')
					line = line.replace('[','')
					line = line.replace(']','')	
				line = line.replace('&', 'and')
				line = line.replace('!','')
				line = line.replace('.','')
				line = line.replace(',','')
				line = line.replace('?','')
				line = line.replace('/','')
				line = line.replace('deluxe','')
				line = line.replace('-','')
				line = line.replace('Deluxe','')
				line = line.replace('remaster','')
				line = line.replace('Remaster','')
				line = line.replace('Remastered','')
				line = line.replace('remastered','')
				line  = line +'\n'
				writelist.write(line)



