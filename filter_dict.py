with open('tagalog_dict.txt', 'r') as dic:
     words = dic.read().split('\n') 
     
nodup = set()
nodup_add = nodup.add
nodup = [w.lower() for w in words if not (w.lower() in nodup or nodup_add(w.lower()))]

with open('tagalog_dict.txt', 'w') as dic:
	for n in nodup:
		print(n, file=dic)
  
