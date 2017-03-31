# coding: utf-8
import network
from PIL import Image
import numpy as np
import struct
import file_tools
import json


def main():
    input_num = 28 * 28
    hiden_num = 70
    output_num = 10
    alpha = 0.3
    count = 0
    nw = network.NetWork(input_num, hiden_num, output_num, alpha)

    with open('last_data.json', 'r') as f:
        data = json.load(f)

    input_num = data['input_num']
    hiden_num = data['hiden_num']
    output_num = data['output_num']
    nw.hiden_weight = np.asarray(data['hiden'])
    nw.output_weight = np.asarray(data['output'])
    nw.hiden_theta = np.asarray(data['hiden_theta'])
    nw.output_theta = np.asarray(data['output_theta'])
    test_num = 10000  # 测试样本数
    for i in xrange(test_num):
        # index = int(np.random.random()*9999)
        img_list = file_tools.read_image('t10k-images.idx3-ubyte', i)
        expect_list = file_tools.read_label('t10k-labels.idx1-ubyte', i)
        result = nw.get_output_result(img_list)

        print expect_list, '\t', np.float32(result).round(), i
        if (expect_list - np.float32(result).round()).sum() == 0:
            print 'success'
            count += 1
        else:
            print 'fail'
    print 'success count=' + str(count)

if __name__ == '__main__':
    main()
