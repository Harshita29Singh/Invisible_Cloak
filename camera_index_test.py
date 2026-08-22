import cv2

for i in range(5):

    cap = cv2.VideoCapture(i)

    ret, frame = cap.read()

    print("Camera", i, "=>", ret)

    cap.release()