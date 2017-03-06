# coding:utf-8
import random
import math
import numpy as np


class NetWork(object):
    input_num = 0  # 输出层神经元个数
    hiden_num = 0  # 隐藏层神经元个数
    output_num = 0  # 输出层神经元个数
    input_layer = None  # 输入层,为input_num维向量
    hiden_layer = None  # 隐藏层,为hiden_num维向量
    output_layer = None  # 输出层向量,为output_num维向量
    expect_result = None  # 期望输出向量,为output_num维向量
    hiden_delta = None  # 隐藏层的误差斜率
    output_delta = None  # 输出层的误差斜率
    hiden_weight = None  # 隐藏层权重，为input_num*hiden_num 维矩阵
    output_weight = None  # 输出层权重，为hiden_num*output_num 维矩阵
    hiden_theta = None  # 隐藏层阈值，为hiden_num维向量
    output_theta = None  # 输出层阈值,为ouput_num维向量
    hiden_theta_delta = None  # 隐藏层阈值的调整
    output_theta_delta = None  # 输出层阈值的调整
    error_squared = 1.0     # 误差的平方和
    alpha = 0.1  # 学习率

    # 构造函数，需要传入 输入层个数，隐藏层个数，输出层个数 ，学习率
    def __init__(self, input_num, hiden_num, output_num, alpha):
        self.input_num = input_num
        self.hiden_num = hiden_num
        self.output_num = output_num
        self.alpha = alpha
        self.init_parameter()

    # 激活函数
    def sigmoid(self, x):
        y = 1 / (1 + np.exp(-x * 1.0))
        return y

    # 初始化参数
    def init_parameter(self):
        i = self.input_num
        j = self.hiden_num
        k = self.output_num
        self.hiden_weight = np.random.rand(i * j) - 0.5
        self.hiden_weight = np.reshape(self.hiden_weight, (i, j))
        self.output_weight = np.random.rand(j * k) - 0.5
        self.output_weight = np.reshape(self.output_weight, (j, k))
        self.hiden_theta = np.random.rand(j) - 0.5
        self.output_theta = np.random.rand(k) - 0.5

        # print self.hiden_weight
        # print self.hiden_weight.shape
        # print self.output_weight
        # print self.output_weight.shape
        # print self.hiden_theta
        # print self.hiden_theta.shape
        # print self.output_theta
        # print self.output_theta.shape
        # a = np.random.random(5)
        # print a.shape
        # b = self.hiden_weight
        # print b.shape
        # print np.dot(a,b)

    # 计算输出
    def calculate_result(self):
        sigmoid = np.frompyfunc(self.sigmoid, 1, 1)
        a = self.input_layer
        # a = np.random.rand(self.input_num)
        b = self.hiden_weight
        result = np.dot(a, b) - self.hiden_theta
        self.hiden_layer = sigmoid(result)
        # print self.hiden_layer

        c = self.hiden_layer
        d = self.output_weight
        result = np.dot(c, d) - self.output_theta
        self.output_layer = sigmoid(result)

        # print self.output_layer

    # 计算误差和权重的校正
    def calculate_expect(self):
        expect_func = np.frompyfunc(lambda x: x * (1 - x), 1, 1)

        # 输出层
        # self.expect_result = np.random.rand(4)
        delta = self.expect_result - self.output_layer
        self.error_squared = (delta * delta).sum()
        r = expect_func(self.output_layer)
        a = np.ones((self.hiden_num, self.output_num))
        b = self.hiden_layer
        delta_k = r * delta
        self.output_delta = (a.T * b).T * delta_k * self.alpha
        self.output_theta_delta = delta_k * self.alpha
        # print self.output_delta
        # print (self.output_weight+self.output_delta)

        # 隐藏层
        r = expect_func(self.hiden_layer)
        p = delta_k
        q = self.output_weight
        delta_j = np.dot(p, q.T)
        # print delta_j
        # self.input_layer = np.random.rand(5)
        a = np.ones((self.input_num, self.hiden_num))
        b = self.input_layer
        self.hiden_delta = (a.T * b).T * delta_j * self.alpha
        self.hiden_theta_delta = delta_j * self.alpha
        # print a.shape
        # print self.input_layer.shape
        # print delta_j.shape
        # print self.hiden_delta

    # 权重调整
    def adjust_weight(self):
        self.output_weight = self.output_weight + self.output_delta
        self.hiden_weight = self.hiden_weight + self.hiden_delta
        # self.output_theta = self.output_theta + self.output_theta_delta
        # self.hiden_theta = self.hiden_theta + self.hiden_theta_delta
        # print self.hiden_weight
        # print self.output_weight

    # 完成一次学习
    def tranning(self, input_list, expect_list):
        self.input_layer = input_list
        self.expect_result = expect_list
        self.calculate_result()
        self.calculate_expect()
        self.adjust_weight()

    # 获取结果
    def get_output_result(self, input_list):
        self.input_layer = input_list
        self.calculate_result()
        return self.output_layer


if __name__ == '__main__':
    nw = NetWork(5, 3, 4)
    nw.calculate_result()
    nw.calculate_expect()
    nw.adjust_weight()
