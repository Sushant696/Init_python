import pickle 
a = ['ram','hari']
f = open('abc.txt','wb')
pickle.dump(a,f)
f.close()
