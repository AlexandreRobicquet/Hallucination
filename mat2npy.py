import numpy as np
import scipy.io


data = scipy.io.loadmat("data/imagenet-vgg-verydeep-16.mat")

print data.keys()

idxs = [0,2,5,7,10,12,14,17,19,21,24,26,28,31,33,35]

params = []
for i in idxs:
    W = data['layers'][0][i][0][0][2][0][0]
    W = np.transpose(W, (3,2,0,1))
    b = data['layers'][0][i][0][0][2][0][1]
    W = W[:,:,::-1,::-1]
    print W.shape, b.shape, data['layers'][0][i][0][0][0][0]
    params.extend([W,b])

np.save("data/vgg16.npy",params)
np.save("data/mean.npy",data['meta']['normalization'][0][0][0][0][2])
np.save("data/classes.npy",data['meta']['classes'][0][0].tolist()[0][0])


data = scipy.io.loadmat("data/imagenet-vgg-verydeep-19.mat")

print data.keys()

idxs = [0,2,5,7,10,12,14,16,19,21,23,25,28,30,32,34,37,39,41]

params = []
for i in idxs:
    W = data['layers'][0][i][0][0][2][0][0]
    W = np.transpose(W, (3,2,0,1))
    b = data['layers'][0][i][0][0][2][0][1]
    #W = W[:,:,::-1,::-1]
    print W.shape, b.shape, data['layers'][0][i][0][0][0][0]
    params.extend([W,b])

np.save("data/vgg19.npy",params)
np.save("data/mean.npy",data['meta']['normalization'][0][0][0][0][2])
np.save("data/classes.npy",data['meta']['classes'][0][0].tolist()[0][0])
