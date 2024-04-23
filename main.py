import cv2
#import numpy
import os
import glob
import import_ipynb
import image_moving
import pp_method_ino

if __name__ == '__main__':
    path = "animal_data"
    image_list = glob.glob(path +"/**/*")
    save_path = "preprocessed/" #저장 경로 설정, 생성
    os.makedirs(save_path, exist_ok=True)
    
	#이미지 이동 : 원본, 좌우반전, 5도, 10도, 15도 회전
    moves = ["origin_", "flip_", "rotation5_", "rotation10_", "rotation15_"]
    
	#전처리 : 노이즈제거, 이진화, 열림, 엣지검출 라플라시안, 엣지검출 캐니
    pps = ["gaussian_", "binary_", "opening_", "laplacian_", "canny_"]

    for il in image_list:
        img = cv2.imread(il)
        img_name = il.split("\\")[-1] #파일 이름
        #이동된 이미지 생성
        img_moves = image_moving.moving(img)
        #이동 방식 + 전처리 방식 + 원본 파일 이름으로 이미지 저장
        for m, im in enumerate(img_moves):
            cv2.imwrite(save_path+moves[m]+pps[0]+img_name, pp_method_ino.del_noise(im)) 
            cv2.imwrite(save_path+moves[m]+pps[1]+img_name, pp_method_ino.make_gray_and_binary(im)) 
            cv2.imwrite(save_path+moves[m]+pps[2]+img_name, pp_method_ino.morphologing(im)) 
            cv2.imwrite(save_path+moves[m]+pps[3]+img_name, pp_method_ino.detect_edge(im, 0)) 
            cv2.imwrite(save_path+moves[m]+pps[4]+img_name, pp_method_ino.detect_edge(im, 1)) 
