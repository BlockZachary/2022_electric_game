# _*_coding:utf-8_*_
# Author： Zachary
import math
import os, cv2, shutil
import csv
import time

import pandas as pd
from scipy.spatial import distance as dist
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination


# Pain Level Bayesian Network Modeling and Training
def train_BN(train_file):
    """
    该方法用于构建疼痛等级评估贝叶斯网络模型并使用训练数据集进行训练
    :return: 贝叶斯网络结构、参数
    """
    # 首先读取训练数据
    train_list = []
    with open(train_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            train_list.append(row)

    data = pd.DataFrame(train_list[1:], columns=train_list[0])

    # 其次构建贝叶斯网络结构
    model = BayesianModel([('Pain_Level', 'AU4'), ('Pain_Level', 'AU6'), ('Pain_Level', 'AU7'), ('Pain_Level', 'AU9'),
                           ('Pain_Level', 'AU10'), ('Pain_Level', 'AU43')])

    # 进行参数学习
    mle = MaximumLikelihoodEstimator(model, data)
    mle.get_parameters()
    model.fit(data, estimator=MaximumLikelihoodEstimator)
    print(model.get_cpds('Pain_Level'))
    return model


# Predict pain level according to AUs evidence
def predict(model, filename):
    """
    用于完成疼痛等级的预测，使用先前创建的贝叶斯网络模型进行推理
    :param model: 贝叶斯网络模型，包含了Bayesian的结构以及参数，是通过数据预训练的
    :param filename: 这个是用于输入的证据，用于推理疼痛等级
    :return: 返回值为res，所有疼痛等级的预测结果——>dict格式
    """

    # 接下来是推理
    # ev = [2,3,2,2,0,1]
    # model_infer = VariableElimination(model)
    # res = model_infer.query(variables=['Pain_Level'],evidence={'AU4':ev[0],'AU6':ev[1],'AU7':ev[2],'AU9':ev[3],'AU10':ev[4],'AU43':ev[5]})
    # # print(model.get_cpds('Pain_Level'))
    # print(res)
    most_flag = ''
    test_list = []
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            test_list.append(row)

    res = {}
    test = pd.DataFrame(test_list[1:], columns=test_list[0])
    print(len(test))
    predict_data = test.drop(columns=['Pain_Level'], axis=1)
    test_res = model.predict(predict_data)
    for item in test_res['Pain_Level']:
        print(item)

        if item not in res:
            res[item] = 1
        else:
            res[item] += 1
    print(f"测试集测试结果准确率为{(test_res['Pain_Level'] == test['Pain_Level']).sum() / len(test) * 100:.2f}%")  # 有标签的话可以加这个

    get_key = res.keys()
    if 'Severe' in get_key:
        most_flag = 'Severe'
    elif 'Moderate' in get_key:
        most_flag = 'Moderate'
    elif 'Weak' in get_key:
        most_flag = 'Weak'
    else:
        most_flag = 'No'

    for index,item in enumerate(test_res['Pain_Level']):
        if item == most_flag:
            most_flag_index = index

    return res,most_flag_index,most_flag,(test_res['Pain_Level'] == test['Pain_Level']).sum() / len(test) * 100


# Read picture then execute the exe to extract the landmarks from pic, next save result
def execute_pic(in_dir, out_dir):
    """
    该方法用于将in_dir的照片作为输入，执行exe，识别出特征点以及AU信息保存为csv
    :param in_dir: 输入的照片路径
    :param out_dir: 输出的csv路径
    :return: None
    """
    # 要执行的exe的路径
    execute_path = r"E:\New_OpenFace\OpenFace-master_new\OpenFace-master\x64\Release\FeatureExtraction.exe"

    # 要执行的参数
    execute_parameter = rf'-fdir {in_dir} -out_dir {out_dir} -verbose'
    # execute_parameter = rf'-fdir {in_dir} -out_dir {out_dir}'  # 不会看见过程

    # 要执行的命令
    execute_line = os.system(execute_path + ' ' + execute_parameter)
    print(execute_line)


def eye_aspect_ratio(eye_point):
    '''
    使用眼部六个特征点计算眼睛睁开比
    :param eye_point: 六个特征点列表
    :return: ear眼睛睁开比
    '''
    p1_5 = dist.euclidean(eye_point[1], eye_point[5])
    p2_4 = dist.euclidean(eye_point[2], eye_point[4])
    p0_3 = dist.euclidean(eye_point[0], eye_point[3])
    ear = (p1_5 + p2_4) / (2.0 * p0_3)
    return ear


def cal_ear(left, right):
    '''
    用于计算左右眼平均的EAR值
    :param left: 六个左眼的特征点坐标列表
    :param right: 六个右眼的特征点坐标列表
    :return: 返回平均EAR值
    '''
    left_ear = eye_aspect_ratio(left)
    right_ear = eye_aspect_ratio(right)
    ear = (left_ear + right_ear) / 2.0
    return ear


def cal_pain_intensity(AU_list):
    '''
    根据AU4、6、7、9、10、43求解疼痛强度
    :param AU_list: AU列表
    :return: 输出疼痛强度值以及疼痛等级
    '''
    au_intensity = 0
    AU_4, AU_6, AU_7, AU_9, AU_10, AU_43 = AU_list
    au_intensity = au_intensity + AU_4 + AU_43
    if AU_6 > AU_7:
        au_intensity += AU_6
    else:
        au_intensity += AU_7

    if AU_9 > AU_10:
        au_intensity += AU_9
    else:
        au_intensity += AU_10

    if au_intensity == 0:
        print(f"\tAU强度为{au_intensity},疼痛等级为：No Pain")
        return 'No'
    elif 1 <= au_intensity <= 2:
        print(f"\tAU强度为{au_intensity},疼痛等级为：Weak Pain")
        return 'Weak'
    elif 3 <= au_intensity <= 4:
        print(f"\tAU强度为{au_intensity},疼痛等级为：Moderate Pain")
        return 'Moderate'
    else:
        print(f"\tAU强度为{au_intensity},疼痛等级为：Severe Pain")
        return 'Severe'


def read_csv_output_result(filepath):
    '''
    根据读取的csv文件获取左右眼的特征点坐标及AU数据，并将EAR值作为AU43，并调用疼痛强度计算方法获得疼痛等级并输出结果
    :param filepath: csv文件的路径
    :return: 输出EAR值、AU43状态、AU状态、AU强度值、疼痛等级,并返回所有EAR值，保存至test_au.csv中
    '''
    x_start = 335
    x_end = 346
    y_start = 403
    y_end = 414
    AU_start = 681
    frame = 0
    ear_data = []
    save_use = []

    print(filepath)

    with open(filepath) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # print(header_row[x_start:x_end+1],header_row[y_start:y_end+1])
        # print(header_row[AU_start])
        while True:
            try:
                frame += 1
                next_row = next(reader)
                right = []
                left = []
                AU = []
                for i in range(6):
                    right.append((float(next_row[x_start + i]), float(next_row[y_start + i])))
                    left.append((float(next_row[x_start + i + 6]), float(next_row[y_start + i + 6])))
                    AU.append(float(next_row[AU_start + i]))
                # print(first_row[x_start:x_end+1],first_row[y_start:y_end+1])
                AU.pop(1)
                print(f"===============第{frame}帧===============")
                ear_res = cal_ear(left, right)
                print(f"\tEAR值为：{ear_res}")
                ear_data.append(ear_res)

                if ear_res < 0.26:
                    print("\tAU43 = 1，闭眼状态")
                    AU43 = 1
                else:
                    print("\tAU43 = 0，睁眼状态")
                    AU43 = 0
                AU.append(AU43)

                AU_use = []
                for item in AU:
                    # AU_use.append(int(math.ceil(item))) # 向下取整
                    AU_use.append(int(math.floor(item)))
                print(f"\t所获取到的AU值：{AU_use}")

                temp_au = AU_use

                # 添加标签，标签是AU计算的
                pain_lable = cal_pain_intensity(AU_use)
                # temp_au.insert(0, None)
                temp_au.insert(0, pain_lable)
                save_use.append(temp_au)
            except:
                print("到底了")
                with open("test_au.csv", "w", newline='') as csvfile:
                    w = csv.writer(csvfile)
                    w.writerow(["Pain_Level", "AU4", "AU6", "AU7", "AU9", "AU10", "AU43"])
                    w.writerows(save_use)
                break


def capmethod():
    try:
        os.mkdir('./data_set')
    except:
        shutil.rmtree('./data_set')
        os.mkdir('./data_set')
    flag = 0
    cam = cv2.VideoCapture(0)
    cam.set(3, 800)  # set video width
    cam.set(4, 600)  # set video height
    framerate = 4  # set frame
    count_frame = 1
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # 水平翻转
        cv2.imshow("pic", img)
        if count_frame % framerate == 0:
            cv2.imwrite(f'./data_set/{flag}_pic.png', img)
            flag += 1
        # time.sleep(0.05)
        count_frame += 1
        # flag += 1
        key = cv2.waitKey(10)  # 原来是10
        if key & 0xFF == 27:  # 27表示ASCII码，代表ESC按键
            break


if __name__ == '__main__':
    # 第负一步，使用摄像头获得数据
    capmethod()

    # 第零步，初始化Bayesian network，并训练出网络模型
    BN = train_BN('traindata.csv')
    print("[info]BN建模完成")

    # 第一步，读取in_dir并执行exe，将结果输出到out_dir-->csv
    # 要处理的图片/视频路径
    # in_dir = r"E:\New_OpenFace\Datasets\UNBC\Images\064-ak064\ak064t1afaff"  # 这个路径是你的待识别图像的路径，路径必须完整
    # in_dir = r"E:\※学习资料※\postgraduate\210721疼痛识别小系统\03用python执行exe\data_set"
    in_dir = os.path.abspath("./data_set")
    # csv输出路径
    # out_dir = r"E:\※学习资料※\postgraduate\210721疼痛识别小系统\03用python执行exe\result"  # 这个是在当前项目文件夹下的result文件夹，路径必须完整
    out_dir = os.path.abspath("./result")
    execute_pic(in_dir, out_dir)
    print("[info]特征点获取完成")

    # 第二步，获取csv中需要的AU4,6,7,9,10，并根据特征点计算EAR值，判断AU43
    # 第三步，将所获取的证据生成单独的csv文件
    read_csv_output_result(f"{out_dir}/{os.path.basename(in_dir)}.csv")
    print("[info]完成AU的计算并保存")

    # 第四步，把证据csv送到Bayesian network中进行推理，并输出结果
    res = predict(BN, "test_au.csv")
    print(f"[info]输出了预测结果{res}")
