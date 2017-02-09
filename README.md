# Hallucination

## First author

(C) 2012- by Adam Tauber, <asciimoo@gmail.com>

## Requirements

## 

get the right data

```unix
mkdir data
cd data
```

download

http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-16.mat

```unix
wget http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-16.mat
```

http://www.vlfeat.org/matconvnet/models/imagenet-vgg-verydeep-19.mat

New dataset coming

Really important to also get cuDNN for Lasagne


### Cuda

Really important to have well install:

https://developer.nvidia.com/cuda-downloads

http://www.r-tutor.com/gpu-computing/cuda-installation/cuda7.5-ubuntu



### Pylearn2 

#### Installation

There is no PyPI download yet, so Pylearn2 cannot be installed using e.g. pip. You must check out the bleeding-edge/development version from GitHub using:
```unix
git clone git://github.com/lisa-lab/pylearn2.git
```

To make Pylearn2 available in your Python installation, run the following command in the top-level pylearn2 directory (which should have been created by the previous command):

```unix
python setup.py develop
```
You may need to use sudo to invoke this command with administrator privileges. If you do not have such access (or would rather not add Pylearn2 to the global site-packages for whatever reason), you can install the relevant links inside the user site-packages directory by issuing the command:
```unix
python setup.py develop --user
```
This command will also compile the Cython extensions required for e.g. pylearn2.train_extensions.window_flip.
Alternatively, you can make Pylearn2 available by adding the installation directory to your PYTHONPATH environment variable, but note that changing
your PYTHONPATH alone won’t compile the Cython extensions (you will need to make sure the extension .so files are built and accessible within the source t
ree, e.g. with python setup.py build_ext --inplace).

#### Path adding

For some tutorials and tests you will also need to set your PYLEARN2_DATA_PATH variable. On Linux, the best way to do this is to add a line to your ~/.bashrc file:
```unix
export PYLEARN2_DATA_PATH=/data/lisa/data
```
Note that this is only an example, and if you are not in the LISA lab, you will need to choose a directory path that is valid on your filesystem. Simply choose a path where it will be convenient for you to store datasets for use with Pylearn2.


### Caffe (for mac OsX)

###### General dependencies

```python
brew install -vd snappy leveldb gflags glog szip lmdb
# need the homebrew science source for OpenCV and hdf5
brew tap homebrew/science
brew install homebrew/science/hdf5 #to be sure..
brew install hdf5 opencv
```
If using Anaconda Python, a modification to the OpenCV formula might be needed Do brew edit opencv and change the lines that look like the two lines below to exactly the two lines below.

```python
-DPYTHON_LIBRARY=#{py_prefix}/lib/libpython2.7.dylib
-DPYTHON_INCLUDE_DIR=#{py_prefix}/include/python2.7
```

If using Anaconda Python, HDF5 is bundled and the hdf5 formula can be skipped.


##### Remaining dependencies, with / without Python

```unix
# with Python pycaffe needs dependencies built from source
brew install --build-from-source --with-python -vd protobuf
brew install --build-from-source -vd boost boost-python
# without Python the usual installation suffices
brew install protobuf boost
```

........ TO FINISH

# Polish the database

Once you've downloaded the vgg-verydeep-16 and 19, you will need to create the normalization batch

# Train
first create the database
```unix
python matn2py.py
```
then simply train

```unix
THEANO_FLAGS=device=gpu python train.py`

```
