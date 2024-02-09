import ColorRecognition
import cv2

def showCanny(path):
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 30, 500)
    cv2.imshow(canny)

if __name__ == '__main__':
    image = cv2.imread('src/assets/sus.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 30, 500)
    while True:
        cv2.imshow(canny)
    #print(ColorRecognition.getImageMeanRGB('/Users/sgupte/Documents/GitHub/LegoSorter/src/assets/sus.png'))
    


