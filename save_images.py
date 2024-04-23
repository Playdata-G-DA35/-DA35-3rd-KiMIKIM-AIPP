import cv2
import pickle

def save_images(img, name, path):
    #전처리한 이미지 저장
    cv2.imwrite(path+name+'jpg', img)
    #평균이 0인 매트릭스로 만들기
    img_mean, img_std = cv2.meanStdDev(img)
    zero_mean = (img-img_mean)/img_std
    #Min-Max가 0-1인 데이터로 정규화
    norm_img = cv2.normalize(img, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    #저장 경로
    zero_mean_path = path+ 'zero_mean/'+ name + '.pickle'
    norm_img_path = path + 'norm_img/'+ name + '.pickle'
    #저장
    with open(zero_mean_path, "wb") as fw:
        pickle.dump(zero_mean, fw)
    with open(norm_img_path, "wb") as fw2:
        pickle.dump(norm_img, fw2)
    



