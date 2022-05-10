# _*_coding:utf-8_*_
# Author： Zachary


# executable = "../../x64/Release/FeatureExtraction.exe"
# in_dir = 'E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff'
# output_dir = 'E:\※学习资料※\postgraduate\210721疼痛识别小系统\01获取AU43\02_get_ear_multi\dataset\result'
# command = sprintf('%s -fdir "%s" -out_dir "%s" -verbose', executable, in_dir, output_dir);

import os

# 要执行的exe的路径
execute_path = r"E:\New_OpenFace\OpenFace-master_new\OpenFace-master\x64\Release\FeatureExtraction.exe"
# 要处理的图片/视频路径
in_dir = r"E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff"
# csv输出路径
out_dir = r"E:\※学习资料※\postgraduate\210721疼痛识别小系统\01获取AU43\02_get_ear_multi\dataset\result"

# 要执行的参数
execute_parameter = rf'-fdir {in_dir} -out_dir {out_dir} -verbose'
# execute_parameter = rf'-fdir {in_dir} -out_dir {out_dir}'  # 不会看见过程

# 要执行的命令
execute_line = os.system(execute_path+' '+execute_parameter)
print(execute_line)