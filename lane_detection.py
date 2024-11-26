
import cv2
import numpy as np
kernel = np.ones((5,5),np.uint8)

def mousePoints(event, x,y,flags,params):
   if event == cv2.EVENT_LBUTTONDOWN:
      print(x,y)

def drawlines(img,lines):
   img = np.copy(img)
   bimg = np.zeros((img.shape[0],img.shape[1],3),np.uint8)

   for line in lines:
      for x1,y1,x2,y2 in line:
         cv2.line(bimg,(x1,y1),(x2,y2),(0,0,255),1)

   img1 = cv2.addWeighted(img,0.8,bimg,1,0.0)
   return img1

cap = cv2.VideoCapture("Resources/dsp.mp4")

while True:
 flag = 0
 suc,img = cap.read()
 img = img[0:img.shape[0]-50,0:img.shape[1]]
 img = cv2.resize(img,(832,432))
 hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
 l = np.array([0,0,230])
 u = np.array([255,255,255])
 mask = cv2.inRange(hsv,l,u)
 imgresult = cv2.bitwise_and(img,img,mask=mask)
 imggray = cv2.cvtColor(imgresult,cv2.COLOR_BGR2GRAY)
 imgblur = cv2.GaussianBlur(imggray,(5,5),0)
 imgcan = cv2.Canny(imgblur,80,150)
 imgdil = cv2.dilate(imgcan,kernel,iterations = 1)
 imgdil = cv2.erode(imgdil,kernel,iterations = 1)
 imgerode = imgdil.copy()
 imgline = cv2.line(imgdil,(360,333),(218,432),255,2)
 imgline = cv2.line(imgline,(480,333),(635,432),255,2)


 sample = np.zeros((imgline.shape[0],imgline.shape[1]),np.uint8)
 sample[0:imgline.shape[0],0:int(imgline.shape[1]/2)] = 255

 mk1 = cv2.bitwise_not(np.zeros_like(imgline))
 polygon1 = np.array([[218,432],[360,333],[480,333],[635,432]])
 cv2.fillPoly(mk1,[polygon1],0)
 mi1 = cv2.bitwise_and(imgerode,mk1)
 out_left = cv2.bitwise_and(mi1,sample)
 out_right = cv2.bitwise_and(mi1,cv2.bitwise_not(sample))

 mk2 = np.zeros_like(imgline)
 polygon2 = np.array([[218,432],[360,333],[480,333],[635,432]])
 cv2.fillPoly(mk2,[polygon2],255)
 inc = cv2.bitwise_and(imgerode,mk2)

 imgref = np.zeros((imgline.shape[0],img.shape[1],3),np.uint8)
 imgref = cv2.line(imgref,(360,333),(218,432),255,2)
 imgref = cv2.line(imgref,(480,333),(635,432),255,2)
 imgout = imgref

 #LANES PLOTTING
 lines = cv2.HoughLinesP(inc,1,np.pi/180,45,np.array([]),0,35)

 if lines is not None:
  imgout = drawlines(imgref,lines)
  cv2.putText(imgout,"LANE SWITCHING",(300,130),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
  flag=1

 lines = cv2.HoughLinesP(out_left,1,np.pi/180,45,np.array([]),0,35)
 if lines is not None:
     imgout = drawlines(imgout, lines)

 lines = cv2.HoughLinesP(out_right, 1, np.pi / 180, 45, np.array([]), 0, 35)
 if lines is not None:
         imgout = drawlines(imgout, lines)

 if(not flag):
     cv2.putText(imgout, "IN-LANE", (350, 130), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

 #WARP PERSPECTIVE
 width, height = 832, 432

 pts1 = np.float32([[0, 300], [832, 300], [832, 432], [0, 432]])
 pts2 = np.float32([[0, 0], [832, 0], [832, 432], [0, 432]])
 matrix = cv2.getPerspectiveTransform(pts1, pts2)
 output = cv2.warpPerspective(img, matrix, (width, height))

 #YELLOW DETECTION
 hsv_out = cv2.cvtColor(output,cv2.COLOR_BGR2HSV)
 l = np.array([20, 20, 230])
 u = np.array([30, 255, 255])
 mask_outy = cv2.inRange(hsv_out, l, u)
 imgresult_outy = cv2.bitwise_and(output, output, mask=mask_outy)
 imggray_outy = cv2.cvtColor(imgresult_outy, cv2.COLOR_BGR2GRAY)
 imgblur_outy = cv2.GaussianBlur(imggray_outy, (5, 5), 0)
 imgdil_outy = cv2.dilate(imgblur_outy, kernel, iterations=1)
 imgdil_outy = cv2.erode(imgdil_outy, kernel, iterations=1)
 lines = cv2.HoughLinesP(imgdil_outy, 1, np.pi / 180, 45, np.array([]), 0, 35)

 if lines is not None:
  cv2.putText(imgout, "YELLOW LANE!", (650, 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 1)
  cv2.putText(imgout, "STICK TO REGULATIONS!", (600, 100), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 255), 1)

 cv2.imshow("out",imgout)
 cv2.waitKey(1)
