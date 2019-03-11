# jt-neural :rocket:

This repository is a sandbox for experimenting with neural style transfer networks (and a fun thing to play around with)! Use neural networks to stylize your videos or webcam with your own style images. Credits to https://github.com/pytorch/examples/tree/master/fast_neural_style and https://github.com/jsigee87/real-time-style-transfer repositories which serve as the base to this one.

# Things to know:
* Training set should be saved to jt-neural/fast-neural-style/train (images must be in a directory *within* this directory): http://cocodataset.org/#download (We are using 2014 Train Images [13GB])
* Input style images should be saved to jt-neural/images
* Input images should be saved to input/images/
* Input videos should be saved to input/videos/
* Models are be saved to fast-neural-style/models
* Images are saved to output/images/
* Videos are to output/videos/
* We currently save models in fast-neural-style/models

# To train a network on a new style image:
* `cd fast-neural-style`
* `python neural_style/neural_style.py train --dataset train --style-image ../input/images/<style-image-name>.jpg --save-model-dir ../models/ --epochs 2 --cuda 1` (Example: `python neural_style/neural_style.py train --dataset train--style-image images/space.jpg --save-model-dir models --epochs 3 --cuda 1`)

# To stylize a video, change the name of the variable `weights_fname` in `stylize_video.py` to the style model you would like to use and run the following:
* `python stylize_video.py <name-of-video>.mp4` (Note: The argument is the name of the video without its path. Make sure it is in videos/input prior to execution.)

# To run the webcam app, change the name of the variable `weights_fname` in `webcam-app\webcam_app.py` to the style model you would like to use and run the following:
* `cd webcam-app`
* `python webcam_app.py`