import cv2
import numpy as np
import math
#from PIL import image
def hashfinder(gray_img):
 #im = cv2.imread('gray_image.png',cv2.IMREAD_GRAYSCALE)
 im = gray_img
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
 from tensorly.decomposition import tucker
 tensorcpy=tensorc.copy()
 core, factors = tucker(tensorcpy, ranks=[50, 20, 20])
 print(core.shape)
 #tucker(tensorcpy, rank=None, ranks=None, n_iter_max=100, init='svd', svd='numpy_svd', tol=0.0001, random_state=None, verbose=False)
 len(factors)
 print(factors[0].shape)
 print(factors[1].shape)
 print(factors[2].shape)
 A = factors[0]
 B = factors[1]
 C = factors[2]
 print(A,B,C)
 #mean of the A,B,C
 mean_A = A.mean(axis=0)
 mean_B = B.mean(axis=0)
 mean_C = C.mean(axis=0)
 
 mean_of_ma = mean_A.mean(axis=0)
 mean_of_mb = mean_B.mean(axis=0)
 mean_of_mc = mean_C.mean(axis=0)
 
 def compare_a(number):
     if number < mean_of_ma:
         return 0
     else:
         return 1
 
 mean_compare_bin_a = list(map(compare_a , mean_A))
 
 len(mean_compare_bin_a)
 print(mean_compare_bin_a)
 
 def compare_b(number):
     if number < mean_of_mb:
         return 0
     else:
         return 1
 mean_compare_bin_b = list(map(compare_b , mean_B))
 
 def compare_c(number):
     if number < mean_of_mc:
         return 0
     else:
         return 1
 mean_compare_bin_c = list(map(compare_c , mean_C))
 
 print(mean_compare_bin_b)
 print(mean_compare_bin_c)
 
 final_hash_bin = mean_compare_bin_a + mean_compare_bin_b + mean_compare_bin_c
 
 print(final_hash_bin)
 print(len(final_hash_bin))
 return final_hash_bin

img1 = cv2.imread('gray_image1.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('gray_image2.png',cv2.IMREAD_GRAYSCALE)
#img1 = open ('gray_image.png')
#img2 = open ()

hashval1 = hashfinder(img1)
hashval2 = hashfinder(img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
