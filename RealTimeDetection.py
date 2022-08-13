import cv2
import numpy as np
from PIL import Image
from keras import models

from mtcnn.mtcnn import MTCNN
detector = MTCNN()

#Load the saved model
model = models.load_model('model.h5')
video = cv2.VideoCapture(1)

while True:
        _, frame = video.read()

        # Used MTCNN to extract face(s) from frames
        bboxes = []
        # detect faces in the image
        faces = detector.detect_faces(frame)
        for face in faces: 
            if face['confidence']>0.99:
                bboxes.append(face['box'])
        
        # print(bboxes);
        
        # Iteratating over all the faces
        for (x, y, w, h) in bboxes:
            img_cropped = frame;
            # Resizing into 128x128 because we trained the model with this image size.
            img_cropped = img_cropped[y:y+h,x:x+w]
            img_cropped = cv2.resize(img_cropped, (128,128))
            img_cropped = np.array(img_cropped)/255
            
            #Our keras model used a 4D tensor, (images x height x width x channel)
            #So changing dimension 128x128x3 into 1x128x128x3 
            img_cropped = np.expand_dims(img_cropped, axis=0)
        
            #Calling the predict method on model to predict current face on the image
            prediction = int(model.predict(img_cropped)[0][0])
            #if prediction is 0, which means I am missing on the image, then show the red color, else show green color rectangle.
            if prediction == 0:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(10)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()
