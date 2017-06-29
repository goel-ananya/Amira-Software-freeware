import cv2
import numpy as np

mouseX=mouseY=[]
xco= []
yco=[]
fi=[]
def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        #cv2.circle(img,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y
        xco.append(x)
        xco.append(y)
        yco.append(xco)
        
        

img = cv2.imread('imgres.bmp',1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        
        for a in range(0,len(yco[0]),2):
            d=[]
            d.append(yco[0][a])
            d.append(yco[0][a+1])
            fi.append(d)
        fi = np.array(fi, np.int32)   
        fi= fi.reshape((-1,1,2))
        cv2.polylines(img,[fi],True,(0,255,255))
        for a in range(len(yco[0])):
            print yco[0][a]
cv2.waitKey(0)
cv2.destroyAllWindows()
