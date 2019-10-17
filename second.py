import cv2
import numpy as np
import math
#from PIL import image
im = cv2.imread('gray_image.png',cv2.IMREAD_GRAYSCALE)
tiles = [im[x:x+10,y:y+10] for x in range(0,im.shape[0],10) for y in range(0,im.shape[1],10)]
size = len(tiles)
print(math.sqrt(size))
#var1 = list(im.getdata())
print(im.shape)
print(im)
for x in range(10000):
    globals()['string%s' % x] = tiles[x]
avg = []
for x in range(0,10000,1):
 sum = 0
 for i in range(10):
  for j in range(10):
   #print (" ",globals()['string%s' % x][i,j])
   sum=sum+globals()['string%s' % x][i,j]
 avg3=sum/10
 avg.append(avg3)
 if x == 9999 :
  print(" ",avg)
def to_matrix(avg):
	return [avg[i:i+100] for i in range(0, len(avg), 100)]
print(to_matrix(avg))
#newavg = np.reshape(avg, (-1, 100))
#print(np.matrix(newavg))
#for p in range(100):
    #for q in range(100):
        #print '{:4}'.format(newavg[p][q]),
    #print
matqq = avg.copy()
matqq = np.reshape(matqq,(25,20,20))
print("\narray reshaped: \n", matqq)
#print(matqq.shape)
#matq = [avg[i * 20:(i + 1) * 20] for i in range((len(avg) + 19) // 20 )]  
#print (matq)
tensorc=np.concatenate((matqq,matqq))
#tensorc = np.array(matq)
print(tensorc.shape)
print(len(avg))
print(math.sqrt(size))
#for x in range(10000):
 #cv2.imshow("image", tiles[x])
#print(im[1,2,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
