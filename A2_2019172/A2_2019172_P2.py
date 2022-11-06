# Insert import statements below
from math import *
import numpy as np
import cv2
import matplotlib.pyplot as plt

def imageEqualization(image):
    
    inp=cv2.imread(image,0)
    cv2.imshow("input",inp)

    M=len(inp)
    N=len(inp[0])
    h=[]
    for i in range(256):
        sum=0
        for j in range(M):
            for k in range(N):
                if (i==inp[j][k]):
                    sum=sum+1
        
        h.append(sum/(N*M))
    

    equalized_image=np.ones((M,N),dtype='uint8')*-1
    for x in range(M):
        for y in range(N):
            v=inp[x][y]
            s=0
            for j in range(v):
                s=255*(h[j])+s
            equalized_image[x][y]=round(s)

    equalized_image=equalized_image.astype(np.uint8)

    g=[]
    for i in range(256):
        sum=0
        for j in range(M):
            for k in range(N):
                if (i==equalized_image[j][k]):
                    sum=sum+1
        
        g.append(sum/(N*M))

    return equalized_image
    
    
if __name__ == "__main__":
    
    image = './input_image.jpg'
    equalized_image = imageEqualization(image)
    
    # write the code to save the image below by the given name
    cv2.imshow("ouput",equalized_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    final_image_path = './output.jpg'
    status = cv2.imwrite(final_image_path,equalized_image)
    print("Image was successfully saved :",status)