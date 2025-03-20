import cv2
import pickle
import os

WIDTH, HEIGHT = 105, 43

DATA_PATH = 'data/parking_position'
IMAGE_PATH = 'data/parking.png'

if os.path.exists(DATA_PATH):
    with open(DATA_PATH, 'rb') as file:
        pos_list = pickle.load(file)
else:
    pos_list = []

def save_positions():
    with open(DATA_PATH, 'wb') as file:
        pickle.dump(pos_list, file)

def mouse_click(event, x, y, flags, params):
    global pos_list
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pos_list.append((x, y))
    elif event == cv2.EVENT_RBUTTONDOWN:
        pos_list = [pos for pos in pos_list if not (pos[0] < x < pos[0] + WIDTH and pos[1] < y < pos[1] + HEIGHT)]
    
    save_positions()

def main():
    while True:
        img = cv2.imread(IMAGE_PATH)
        if img is None:
            print("Error: Image not found.")
            break
        
        for pos in pos_list:
            cv2.rectangle(img, pos, (pos[0] + WIDTH, pos[1] + HEIGHT), (255, 0, 255), 1)
        
        cv2.imshow("Parking Spot Selector", img)
        cv2.setMouseCallback("Parking Spot Selector", mouse_click)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
