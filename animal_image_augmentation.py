#이미지 변환

import cv2

def animal_images(img, flip_1, angle_images):
    """
    여러 개의 이미지를 창에 표시하는 함수
    
    Args:
        img (numpy.ndarray): 원본 이미지
        flip_1 (numpy.ndarray): 좌우 반전된 이미지
        angle_images (list): 회전된 이미지 리스트 (5도, 10도, 15도)
    """
    # 원본 이미지 표시
    cv2.imshow("Original Image", img)
    
    # 좌우 반전 이미지 표시
    cv2.imshow("Flipped Image", flip_1)
    
    # 회전된 이미지 표시
    cv2.imshow("Rotated 5 Degrees", angle_images[0])
    cv2.imshow("Rotated 10 Degrees", angle_images[1])
    cv2.imshow("Rotated 15 Degrees", angle_images[2])
    
    # 키 입력 대기 및 창 닫기
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 원본 이미지 읽기
img = cv2.imread(r"C:\Users\USER\Desktop\JH\05_numpy_opencv\images\Bear.jpg")

# 좌우 반전 이미지 생성
flip_1 = cv2.flip(img, 1)

# 회전된 이미지 리스트 생성
angle_images = [
    cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 5, 1), (img.shape[1], img.shape[0])),
    cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 10, 1), (img.shape[1], img.shape[0])),
    cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 15, 1), (img.shape[1], img.shape[0]))
]


# 이미지 표시 함수 호출
animal_images(img, flip_1, angle_images)