import numpy as np
import cv2


def cannyDetectEdges(img) -> cv2.Mat:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blurred, 30, 200)
    return canny

#Test the efficacy of this method vs canny edge detection
def sobelDetectEdges(img) -> cv2.Mat:
    grad_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    grad_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    grad = np.sqrt(grad_x**2 + grad_y**2)
    grad_norm = (grad * 255 / grad.max()).astype(np.uint8)
    return grad_norm


def getImageMeanRGB(path) -> list:
    frame = cv2.imread(path)
    sobel = sobelDetectEdges(frame)
    canny = cannyDetectEdges(sobel)
    return getMatrixMeanColor(canny, frame)

def getMatrixMeanColor(mask_matrix, image_matrix) -> list:
    total = [0, 0, 0]
    denominator = 0
    for i, row in  enumerate(mask_matrix):
        temp_rgb = getRowMeanColor(row, image_matrix, i)
        if temp_rgb is None:
            continue
        total[0] += temp_rgb[0]
        total[1] += temp_rgb[1]
        total[2] += temp_rgb[2]
        denominator += 1
    total = list(map(lambda x : x / denominator, total))
    return total

# Add check for adjacency to another edge pixel
def getRowMeanColor(input_row, color_matrix, row_number) -> list:
    red = 0
    blue = 0
    green = 0
    denominator = 0
    count = 0
    target = sum(input_row)
    if target % 2 == 1 or target == 0:
        return None
    for i, j in enumerate(input_row):
        if j != 0:
            count += 1
        if count % 2 == 1:
            denominator += 1
            blue += color_matrix[row_number][i][0]
            green += color_matrix[row_number][i][1]
            red += color_matrix[row_number][i][2]

    return list(map(lambda x : x / denominator, [blue, green, red]))




