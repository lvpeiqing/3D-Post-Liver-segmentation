# -----------------------路径相关参数---------------------------------------

raw_liver_data_path = '......./origin_data/'  # 原始数据集路径(包括CT和标签)

fix_liver_data_path = '........../fixed_data/'  # 经过预处理后数据的路径(包括CT和标签)

test_liver_ct_path = '..../ct/'  # 原始测试集CT数据路径

test_liver_seg_path = '....../seg/'  # 原始测试集标注数据路径

pred_liver_path = './data/output_test_data/liver'  # 网络预测结果保存路径

crf_liver_path = './data/output_test_data/crf_liver'  # CRF优化结果保存路径

liver_module_path = '/checkpoints/.....'

# -----------------------路径相关参数---------------    ------------------------


# ---------------------训练数据获取相关参数-----------------------------------

size = 16  # 使用48张连续切片作为网络的输入

stride_1 = 3  # 每隔3个切片，生成一个数据块

block_size = 16

down_scale = 0.5  # 横断面降采样因子

expand_slice = 20  # 仅使用包含肝脏以及肝脏上下20张切片作为训练样本

slice_thickness = 1  # 将所有数据在z轴的spacing归一化到1mm

upper, lower = 200, -200  # CT数据灰度截断窗口

# ---------------------训练数据获取相关参数-----------------------------------


# -----------------------网络结构相关参数------------------------------------

drop_rate = 0.3  # dropout随机丢弃概率

# -----------------------网络结构相关参数------------------------------------


# ---------------------网络训练相关参数--------------------------------------
import torch

device = torch.device('cuda:0,1,2')  # 使用的显卡序号

gpu = '0,1,2'

max_epochs = 800

learning_rate = 1e-4

weight_decay = 5e-4

learning_rate_decay = [400, 650]

alpha = 1  # 深度监督衰减系数

dataset_liver_path = './data/fixed_data/'

batch_size = 1

num_workers = 3

pin_memory = True

cudnn_benchmark = True

# ---------------------网络训练相关参数--------------------------------------


# ----------------------模型测试相关参数-------------------------------------

threshold = 0.5  # 阈值度阈值

stride = 12  # 滑动取样步长

maximum_hole = 5e4  # 最大的空洞面积

# ----------------------模型测试相关参数-------------------------------------


# ---------------------CRF后处理优化相关参数----------------------------------

z_expand, x_expand, y_expand = 10, 30, 30  # 根据预测结果在三个方向上的扩展数量

max_iter = 20  # CRF迭代次数

s1, s2, s3 = 1, 10, 10  # CRF高斯核参数

# ---------------------CRF后处理优化相关参数----------------------------------