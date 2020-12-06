import cv2
import os
import numpy as np



FOLDER = input('path: ')
SALT_FRAMES = int(input('how many salt frames: '))

PATH_FRAMES = './frames'
if not os.path.exists(PATH_FRAMES):
    os.makedirs(PATH_FRAMES)

os.chdir(PATH_FRAMES)

ACTUAL = os.getcwd()

for root, dirs, files in os.walk(FOLDER):
    for file in files:
        if '.mp4' in file:
            
            print(f'actual file: {file}')

            cap = cv2.VideoCapture(os.path.join(root, file))

            if (cap.isOpened() == False): 
                print("Error opening video stream or file")

            count = 0
            controller = 0

            while(cap.isOpened()):
                if not os.path.exists(os.path.join(ACTUAL, file.replace('.mp4', ''))):
                    os.makedirs(os.path.join(ACTUAL, file.replace('.mp4', '')))
                if os.getcwd() != os.path.join(ACTUAL, file.replace('.mp4', '')):
                    os.chdir(os.path.join(ACTUAL, file.replace('.mp4', '')))

                ret, frame = cap.read()
                if ret == True:
                    
                    if count % SALT_FRAMES == 0:
                        cv2.imwrite("frame%d.jpg" % controller, frame)
                        controller += 1

                    cv2.imshow(f'{file}',frame)

                    if cv2.waitKey(25) & 0xFF == ord('q'):
                        break
                    count += 1
                else: 
                    break
                
            cap.release()

            cv2.destroyAllWindows()






