import cv2
import numpy
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
	moves = ["_origin",
			"_flip",
			"_rotation5",
			"_rotation10",
			"_rotation15"]

	#전처리 : 노이즈제거, 이진화, 열림, 엣지검출 라플라시안, 엣지검출 캐니
	pps = [ "_del_noise",
			"_make_gray_and_binary",
			"_morphologing",
			"_detect_edge_0",
			"_detect_edge_1"]

	for il in image_list:
        img = cv2.imread(il)
        img_name = il.split("\\")[-1] #파일 이름

        #이동된 이미지 생성
        img_moves = image_moving.moving(img)

        #이동 방식 + 전처리 방식 + 원본 이름으로 이미지 저장
        for m, im in enumerate(img_moves):
            cv2.imwrite(pp_method_ino.del_noise(im), save_path+moves[m]+pps[0]+img_name) 
            cv2.imwrite(pp_method_ino.make_gray_and_binary(im), save_path+moves[m]+pps[1]+img_name) 
            cv2.imwrite(pp_method_ino.morphologing(im), save_path+moves[m]+pps[2]+img_name) 
            cv2.imwrite(pp_method_ino.detect_edge(im, 0), save_path+moves[m]+pps[3]+img_name) 
            cv2.imwrite(pp_method_ino.detect_edge(im, 1), save_path+moves[m]+pps[4]+img_name) 
        
