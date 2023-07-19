import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

folderPath = "fingers"  # name of the folder, where there are images of fingers
fingerList = os.listdir(folderPath)  # list of image titles in 'fingers' folder
overlayList = []
for imgPath in fingerList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    overlayList.append(image)

pTime = 0

detector = htm.handDetector(detectionCon=0.75)
totalFingers = 0

while True:
    sucess, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if lmList:
        fingersUp = detector.fingersUp()
        totalFingers = fingersUp.count(1)
        if fingersUp[1] == 1 and fingersUp[2] != 1 and fingersUp[0] != 1 and fingersUp[3] != 1 and \
                fingersUp[4] != 1:
            pyautogui.press('right')
        if fingersUp[1] != 1 and fingersUp[2] != 1 and fingersUp[0] != 1 and fingersUp[3] != 1 and \
                fingersUp[4] == 1:
            pyautogui.press('left')
        if fingersUp[1] == 1 and fingersUp[2] == 1 and fingersUp[0] != 1 and fingersUp[3] != 1 and \
                fingersUp[4] != 1:
            pyautogui.press('space')
        if fingersUp[1] == 1 and fingersUp[2] == 1 and fingersUp[0] == 1 and fingersUp[3] != 1 and \
                fingersUp[4] != 1:
            pyautogui.press('f')
            print('1')
    # elif totalFingers[1] == 1 and totalFingers[2] == 1 and totalFingers[0] != 1 and totalFingers[3] != 1 and \
    #         totalFingers[4] != 1:
    #     pyautogui.press('right')
