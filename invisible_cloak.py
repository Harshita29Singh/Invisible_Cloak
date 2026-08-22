import cv2
import numpy as np
import time

# Open webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

print("Camera opened:", cap.isOpened())

if not cap.isOpened():
    print("Camera not found!")
    exit()

print("Stay away from camera...")
print("Capturing background in 3 seconds...")
time.sleep(3)

# Warm up camera
for i in range(30):
    cap.read()

# Capture background
ret, background = cap.read()

print("Background capture:", ret)

if not ret:
    print("Failed to capture background!")
    cap.release()
    exit()

background = cv2.flip(background, 1)

print("Background captured successfully!")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Frame not received")
        break

    frame = cv2.flip(frame, 1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red color detection
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    mask = mask1 + mask2

    # Noise removal
    kernel = np.ones((3, 3), np.uint8)

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel,
        iterations=2
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    mask_inv = cv2.bitwise_not(mask)

    # Current frame without red cloth
    visible_part = cv2.bitwise_and(
        frame,
        frame,
        mask=mask_inv
    )

    # Background where red cloth exists
    invisible_part = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )

    # Final output
    final = cv2.addWeighted(
        visible_part,
        1,
        invisible_part,
        1,
        0
    )

    cv2.imshow("Mask", mask)
    cv2.imshow("Invisible Cloak", final)

    key = cv2.waitKey(1) & 0xFF

    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()