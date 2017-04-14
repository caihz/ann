# coding: utf-8
import network
from PIL import Image
import numpy as np
import struct
import file_tools
import json

def main():
    input_num = 28*28
    hidden_num = 30
    output_num = 10
    alpha = 0.2
    nw = network.NetWork(input_num, hidden_num, output_num, alpha)
    process = 0
    tran_num = 1000 # 训练数

    # error_list = []
    # best_list = []
    for i in xrange(tran_num):
        # index = int(np.random.random()*59999)
        img_list = file_tools.read_image('train-images.idx3-ubyte',i)
        expect_list = file_tools.read_label('train-labels.idx1-ubyte',i) 
        nw.training(img_list,expect_list)
        # error_list.append(nw.error_squared)
        # if nw.error_squared < best_square:
        #     best_square = nw.error_squared
            # best_hidden = nw.hidden_weight
            # best_output = nw.output_weight
        # best_list.append(best_square)         
        print str(i)+' error_squared = '+str(nw.error_squared)

    # best_data = {
    # 'input_num': input_num,
    # 'hidden_num': hidden_num,
    # 'output_num':output_num,
    # 'hidden':best_hidden.tolist(),
    # 'output':best_output.tolist(),
    # 'hidden_theta':nw.hidden_theta.tolist(),
    # 'output_theta':nw.output_theta.tolist(),
    # }

    data = {
    'input_num': input_num,
    'hidden_num': hidden_num,
    'output_num':output_num,
    'hidden':nw.hidden_weight.tolist(),
    'output':nw.output_weight.tolist(),
    'hidden_theta':nw.hidden_theta.tolist(),
    'output_theta':nw.output_theta.tolist(),
    }

    # error_data = {
    # 'error_list': error_list,
    # 'best_list' : best_list,
    # }

    with open('data.json','w') as f:
        json.dump(data,f)

    # with open('error_data.json','w') as f:
    #     json.dump(error_data,f)

if __name__ == '__main__':
    main()