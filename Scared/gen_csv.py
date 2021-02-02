import os
import pandas as pd

def gen_csv(data_dir, output_dir):
    left_rgb_list = sorted(os.listdir(data_dir + '/image_2'))
    right_rgb_list = sorted(os.listdir(data_dir + '/image_3'))
    disp_list = sorted(os.listdir(data_dir + '/disp_occ_0'))
    df_list = []
    for left_rgb, right_rgb, disp in zip(left_rgb_list, right_rgb_list, disp_list):
        left_rgb_file = os.path.join(data_dir, 'image_2', left_rgb)
        right_rgb_file = os.path.join(data_dir, 'image_3', right_rgb)
        disp_file = os.path.join(data_dir, 'disp_occ_0', disp)
        df_list.append({"path_to_left_rgb": left_rgb_file, "right_rgb_list": right_rgb_file, "path_to_groundtruth": disp_file})
    df = pd.DataFrame(df_list)
    df.to_csv(os.path.join(output_dir, 'scared.csv'), index=False, header=False)
        
def main():
    data_dir = "/mnt/Private/ywt/datasets/SCARED_PSMNet/training/"
    output_dir = "/home/ywt/Documents/project_lab/depth_estimation/scared-related/Real-time-self-adaptive-deep-stereo/"
    gen_csv(data_dir, output_dir)

if __name__=="__main__":
    main()