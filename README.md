# jt-neural :rocket:

This repository uses a bunch of shit to make art! Credits to https://github.com/pytorch/examples/tree/master/fast_neural_style and https://github.com/jsigee87/real-time-style-transfer repositories.

To train a network on a new style image, run the following:
* `cd fast-neural-style`
* `python neural_style/neural_style.py train --dataset <path-to-train-dataset> --style-image <path-to-style-image> --save-model-dir ../model/ --epochs 2 --cuda 1`

To cut a video into frames, put your video into ./input/videos (make sure it is the only video in that directory and the temp folder is empty) and run this:
`python cut_video.py`

To stylize the frames, run this:
`python real-time.py`
