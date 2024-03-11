import ColorRecognition
import cv2

def showCanny(path):
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 50, 150)
    cv2.imshow(canny)

if __name__ == '__main__':
    print(ColorRecognition.getImageMeanRGB('/Users/sgupte/Documents/GitHub/LegoSorter/src/assets/leaf.png'))
    test = ColorRecognition.sobelDetectEdges(cv2.imread('src/assets/leaf.png'))
    canny = ColorRecognition.cannyDetectEdges(test)
    cv2.imshow('thing', test)
    cv2.imshow('cannt', canny)

    cv2.waitKey(0)

