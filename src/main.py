import ColorRecognition
import cv2

if __name__ == '__main__':
    print(ColorRecognition.getImageMeanRGB('/Users/sgupte/Documents/GitHub/LegoSorter/src/assets/lavender.png'))
    test = ColorRecognition.sobelDetectEdges(cv2.imread('src/assets/lavender.png'))
    canny = ColorRecognition.cannyDetectEdges(test)
    cv2.imshow('thing', test)
    cv2.imshow('cannt', canny)
    cv2.waitKey(0)

