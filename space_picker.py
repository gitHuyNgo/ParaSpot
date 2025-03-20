import cv2
import pickle

width, height = 105, 43
    
try:
    with open('data/parking_position', 'rb') as f:
        pos_list = pickle.load(f)
except:
    pos_list = []

def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for index, pos in enumerate(pos_list):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                pos_list.pop(index)
    
    with open('data/parking_position', 'wb') as f:
        pickle.dump(pos_list, f)

while True:
    img = cv2.imread('data/parking.png')
    for pos in pos_list:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 1)
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', mouse_click)
    cv2.waitKey(1)
    