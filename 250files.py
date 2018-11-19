import numpy as np
import soundfile as sf
new_data = np.empty([25000,]) #creating an empty array for new file to be generated from original file
y1 = np.empty([25000,])
for j in range(1,3):
	b= "hello"+str(j)+".wav"
	data, samplerate = sf.read(b)
	print len(data), samplerate
	x= len(data)
	p = 25000-x
	for y in range(1 ,p):
		for i in range(0,y-1):
			new_data[i] =y1[i]
		for i in range(y,25000-x+y-1):
			new_data[i] =data[i-y]
		for i in range(25000-y , 24999):
			new_data[i] = y1[i]	
		a = "hello__"+str(j) +"_"+str(y)+".wav"
		sf.write(a, new_data, samplerate)
		print len(new_data)
 
