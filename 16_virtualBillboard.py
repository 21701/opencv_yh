import cv2
import numpy as np

from utils import get_four_points

image =  cv2.imread('data/imgaes/first-image.jpg')

cv2.imshow('original', image)

# 1. 이 이미지를 변환하기 위한 점 4개 구하기



image_dst = cv2.imread('data/images/times-square.jpg')

cv2.imshow('dst',image_dst)


# 2. 타임 스퀘어의 이미지에 매칭할 점의 좌표를 구합니다.


# 3. 위의 두개 이미지간의 매칭할 두 점들을 모두 찾았으니,
#     변환 행렬을 얻어 옵니다.


# 4. image를 변환시킵니다.




cv2.waitKey(0)
cv2.destroyAllWindows()