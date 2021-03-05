# Gibson+Sparse-Depth-Completion

This repo first create a virtual robotics environment using [Gibson](https://github.com/StanfordVL/iGibson). RGB and spare LiDAR data are generated in the Gibson. Then I use the trained model of Sparse-Depth-Completion (https://github.com/wvangansbeke/Sparse-Depth-Completion) to perform guided up sampling and generate a dense depth image. The training runs on [HIPERGATOR 3.0](https://www.rc.ufl.edu/services/hipergator/).

![demo](https://github.com/dingkwang/Gibson_Spares_Depth_Completion/blob/main/result/GUSampling1.gif)
![demo](https://github.com/dingkwang/Gibson_Spares_Depth_Completion/blob/main/result/GUSampling2.gif)
## Run the project

1. Install Gibson. There are several options. You can download the Gibson](https://github.com/StanfordVL/iGibson), or follow  http://svl.stanford.edu/igibson/docs/installation.html.

2. Run iGibson/demo5.py to generate RGB images and LiDAR depth images.

3. Train the model, python dkmain.py. Refer to the [Sparse-Depth-Completion] (https://github.com/wvangansbeke/Sparse-Depth-Completion) for the training data. 

4. Run Test/test.py to generate the dense depth image. 

5. Use creatVideo.py to generate videos. 



