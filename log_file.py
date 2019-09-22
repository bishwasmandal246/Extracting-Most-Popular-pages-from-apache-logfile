import collections
log_file = open('put_your_log_file.log', 'r')
clean_log=[]
for i in log_file:
    try:
        clean_log.append(i[i.index('GET')+4:i.index('HTTP')])
    except:
        pass
count = collections.Counter(clean_log)
for c in counter.most_common(10):
    print(str(c[1]) + '	 ' + str(c[0]))
log_file.close()
