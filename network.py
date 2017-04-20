# coding:utf-8
import random
import math
import numpy as np


class NetWork(object):
    input_num = 0  # 输入层神经元个数
    hidden_num = 0  # 隐藏层神经元个数
    output_num = 0  # 输出层神经元个数
    input_layer = None  # 输入层,为input_num维向量
    hidden_layer = None  # 隐藏层,为hidden_num维向量
    output_layer = None  # 输出层向量,为output_num维向量
    expect_result = None  # 期望输出向量,为output_num维向量
    hidden_delta = None  # 隐藏层的误差斜率
    output_delta = None  # 输出层的误差斜率
    hidden_weight = None  # 隐藏层权重，为input_num*hidden_num 维矩阵
    output_weight = None  # 输出层权重，为hidden_num*output_num 维矩阵
    hidden_theta = None  # 隐藏层阈值，为hidden_num维向量
    output_theta = None  # 输出层阈值,为ouput_num维向量
    hidden_theta_delta = None  # 隐藏层阈值的调整
    output_theta_delta = None  # 输出层阈值的调整
    error_squared = 0.0     # 误差
    alpha = 0.3  # 学习率

    # 构造函数，需要传入 输入层个数，隐藏层个数，输出层个数 ，学习率
    def __init__(self, input_num, hidden_num, output_num, alpha):
        self.input_num = input_num
        self.hidden_num = hidden_num
        self.output_num = output_num
        self.alpha = alpha
        self.init_parameter()

    # 激活函数
    def sigmoid(self, x):
        y = 1 / (1 + np.exp(-x * 1.0))
        return y


    # 初始化参数
    def init_parameter(self):
    	'''
    	网络类各个参数的初始化。包括：
    	隐藏层权重的初始化，初始化为一个input_num*hidden_num的矩阵，值的范围在(-0.5~0.5)
    	输出层权重的初始化，初始化为一个hidden_num*output_num的矩阵，值的范围在(-0.5~0.5)
    	隐藏层阈值的初始化，初始化为一个hidden_num维向量，值的范围在(-0.5~0.5)
    	输出层阈值的初始化，初始化为一个output_num维向量，值得范围在(-0.5~0.5)
    	'''

        i = self.input_num
        j = self.hidden_num
        k = self.output_num
        self.hidden_weight = np.random.randn(j,i) - 0.5
        self.output_weight = np.random.randn(k,j) - 0.5
        self.hidden_theta = np.random.randn(j) - 0.5
        self.output_theta = np.random.randn(k) - 0.5

        # print self.hidden_weight
        # print self.hidden_weight.shape
        # print self.output_weight
        # print self.output_weight.shape
        # print self.hidden_theta
        # print self.hidden_theta.shape
        # print self.output_theta
        # print self.output_theta.shape
        # a = np.random.random(5)
        # print a.shape
        # b = self.hidden_weight
        # print b.shape
        # print np.dot(a,b)

    # 计算输出
    def calculate_result(self):
    	'''
    	计算出隐藏层与输出层的结果，并通过激活函数激活
    	避免使用for循环语句，直接使用矩阵的相关运算提高可阅读性
    	'''

        sigmoid = np.frompyfunc(self.sigmoid, 1, 1)
        a = self.input_layer
        # a = np.random.rand(self.input_num)
        b = self.hidden_weight
        result = np.dot(b, a) - self.hidden_theta
        self.hidden_layer = sigmoid(result)
        # print self.hidden_layer

        c = self.hidden_layer
        d = self.output_weight
        result = np.dot(d, c) - self.output_theta
        self.output_layer = sigmoid(result)

        # print self.output_layer

    # 计算误差和权重的校正
    def calculate_expect(self):
    	"""
    	计算出输出层结果与期望结果的差值，即误差
    	并根据误差，计算出输出层与隐藏层权重的校正(反向传播算法)
    	"""

        # 输出层
        e = self.expect_result - self.output_layer
        self.error_squared = np.dot(e,e)*0.5
        a = np.ones((self.hidden_num,self.output_num))
        b = self.hidden_layer
        delta_k = self.output_layer*(1-self.output_layer) * e
        self.output_delta = (a * delta_k).T * b * self.alpha
        self.output_theta_delta = delta_k*self.alpha

        # 隐藏层
        delta_j = np.dot(delta_k, self.output_weight)* (1-self.hidden_layer)*self.hidden_layer
        a = np.ones((self.input_num, self.hidden_num))
        b = self.input_layer
        self.hidden_delta = (a* delta_j).T * b * self.alpha
        self.hidden_theta_delta = delta_j * self.alpha

    # 权重调整
    def adjust_weight(self):
        self.output_weight = self.output_weight + self.output_delta
        self.hidden_weight = self.hidden_weight + self.hidden_delta
        # self.output_theta = self.output_theta + self.output_theta_delta
        # self.hidden_theta = self.hidden_theta + self.hidden_theta_delta
        # print self.hidden_weight
        # print self.output_weight

    # 完成一次学习
    def training(self, input_list, expect_list):
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
    nw = NetWork(3, 4, 5,0.3)
    nw.input_layer = np.random.randn(3)
    weight = np.random.randn(3,5)
    print weight
    out = np.random.randn(5)
    print weight*out
    # weight = np.random.randn(4,3)
    # print weight
    # input_layer = np.random.randn(3)
    # print input_layer

    # print np.dot(weight,input_layer)
    
