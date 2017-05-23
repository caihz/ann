# ann
BP Artificial Neural Network with three layer.
Using this network to recognize  MNIST handwritten digits.

## Require Library
1. python2.7
2. numpy
```
pip install numpy
```
3. pillow
```
pip install pillow
```

4. GUI need PyQt4

https://www.riverbankcomputing.com/software/pyqt/download

5. Mnist Database

http://yann.lecun.com/exdb/mnist/
## include
- train-labels-idx1-ubyte
- train-images-idx3-ubyte
- t10k-labels-idx1-ubyte
- t10k-images-idx3-ubyte

## fast using
1. copy data.json from best dictionary to root dictionary(with file_tools.py same dictionary).
2. copy t10k-images.idx3-ubyte file to img dictionary and run img.py(ensure PIL installed) to get MNIST images.
3. run gui.pyw (ensure PyQt4 installed),you can drag MNIST image to GUI program.
4. enjoy and happy coding.

## screenshot
![screenshot](https://raw.githubusercontent.com/kulaice/ann/master/screenshot/screenshot.png)