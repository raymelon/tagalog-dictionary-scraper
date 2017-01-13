with open('tagalog_dict.txt', 'r') as dic:
     words = dic.read().split('\n')
     
nodup = set()
nodup_add = nodup.add
nodup = [w for w in words if not (w in nodup or nodup_add(w))]

#with open('tagalog_dict.txt', 'w') as dic:
     
