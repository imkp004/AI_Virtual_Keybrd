import cv2 as cv
import mediapipe as mp
from pynput.keyboard import Key, Controller
import math
from time import sleep

"""
I want this Artificial Intellengence Virtual Keybaord for the enhancement of the normal
keybaord. To do this I used the OpenCV and mediapipe libraries from google libraries.
To begin with the algrothim, a sinmple python code to start the camera and read the video.
"""

cap = cv.VideoCapture(0)
cap.set(3, 1250)
cap.set(4, 640)


    """
    An empty array to store the clicked key.
    """
arr = []
keyLayout = [["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "<"],
 ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
 ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
 ["Z", "X", "C", "V", "B", "N", "M"],
 [" "]]

    """
    An array that holds the keys of the keybaord
    """

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
Hands = mpHands.Hands()
keyboard = Controller()
mpDraw = mp.solutions.drawing_utils

    """
    Function: To read and run the hands through the camera.
    drawing the landmarks of the hands.
    reading the hands.
    connecting the hand tracking with the virtual keybaord.
    Drawing and editing the keyboard.
    """

class settings():
    def __init__(self, pos, size, text):
        self.pos = pos
        self.size = size
        self.text = text
      
    """
    Class: To set the location of the keys for everytime the hands
    goes near it it will click.
    """

def keyboardEdit(img, storedVar):
    for button in storedVar:
        x, y = button.pos
        w, h = button.size

        cv.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), 5)
        cv.putText(img, button.text, (x + 15, y + 35), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)

    return img
   
    """
    Function: To make and to click the keys on the keyboard which is also
    connected with the array and the loaction of the keys.
    """

for i in range(len(keyLayout)):
    for j, key in enumerate(keyLayout[i]):
        arr.append(settings([60 * j + 10, 60 * i + 10], [50, 50], key))
    
    """
    loop: To give its own loaction on the camera.
    """

    """
    main code
    """
while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = Hands.process(imgRGB)

    printer = []

    if results.multi_hand_landmarks:
        for hand_in_frame in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand_in_frame, mpHands.HAND_CONNECTIONS)

        for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            printer.append([cx, cy])

        if printer:
            for button in arr:
                x, y = button.pos
                w, h = button.size

                if x < printer[8][0] < x + w and y < printer[8][1] < y + h:
                    cv.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), cv.FILLED)
                    x1, y1 = printer[8][0], printer[8][1]
                    x2, y2 = printer[12][0], printer[12][1]
                    clicked = math.hypot(x2 - x1 - 30, y2 - y1 - 30)
                    print(clicked)
                    if button.text == "<":
                        keyboard.press(Key.backspace)
                        keyboard.release(Key.backspace)

                    if not clicked > 63:
                        keyboard.press(button.text)
                        cv.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), cv.FILLED)
                        sleep(0.15)

        img = keyboardEdit(img, arr)


    cv.imshow("Camera", img)
    cv.waitKey(1)
 
