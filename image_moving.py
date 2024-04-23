#이미지 변환

import cv2

def moving(img):
    """
    img (numpy.ndarray): 원본 이미지
    flip_1 (numpy.ndarray): 좌우 반전된 이미지
    angle_images (list): 회전된 이미지 리스트 (5도, 10도, 15도)
    """
    # 좌우 반전 이미지 생성
    flip_1 = cv2.flip(img, 1)
    # 회전된 이미지 리스트 생성
    angle_images = [
        cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 5, 1), (img.shape[1], img.shape[0])),
        cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 10, 1), (img.shape[1], img.shape[0])),
        cv2.warpAffine(img, cv2.getRotationMatrix2D((img.shape[1]//2, img.shape[0]//2), 15, 1), (img.shape[1], img.shape[0]))
    ]

    return img, flip_1, *angle_images