import os
import cv2

path = "Images/"
images=[]
for file in path:
    os.listdir(path)
    os.splitext(file)
    if ext in ['.gif','.jpg','.png', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append()
        count= len(images)
        frame = cv2.imread(images[0])
        frame.shape(width,height,channel)
        size=(width,height)
        
print(size)
out=cv2.VideoWriter('Project', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
    out.write()
print("Done")