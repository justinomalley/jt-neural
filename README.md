# jt-neural :rocket:

This repository uses a bunch of shit to make art! Credits to https://github.com/pytorch/examples/tree/master/fast_neural_style and https://github.com/jsigee87/real-time-style-transfer repositories.

Things to know:
* Training set should be saved to jt-neural/fast-neural-style/train (images must be in a directory *within* this directory): http://cocodataset.org/#download (We are using 2014 Train Images [13GB])
* Input images should be saved to jt-neural/input/images/
* Input videos should be saved to jt-neural/input/videos/
* Models should be saved to jt-neural/models
* Images should be saved to jt-neural/output/images/
* Videos should be saved to jt-neural/output/videos/
* Video frames should be saved to jt-neural/output/videos/temp/

To train a network on a new style image, run the following:
* `cd fast-neural-style`
* `python neural_style/neural_style.py train --dataset train --style-image ../input/images/<style-image-name>.jpg --save-model-dir ../models/ --epochs 2 --cuda 1`

To cut a video into frames, put your video into ./input/videos (make sure it is the only video in that directory and the temp folder is empty) and run this:
`python cut_video.py`

To stylize the frames, run this:
`python real-time.py`

