import cv2
import numpy as np
import os
from os.path import isfile, join
# pathIn= './best/results/' #NN out
# pathIn = './../GibData/depth_selection/image/val/'


def create(pathIn, pathOut):
    fps = 60
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    #for sorting the file names properly
    files.sort(key = lambda x: x[5:-4])
    files.sort()
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    #for sorting the file names properly
    files.sort(key = lambda x: x[5:-4])
    for i in range(len(files)):
        filename=pathIn + files[i]
        # print("filename", filename)
        #reading each files
        img = cv2.imread(filename)
        
        height, width, layers = img.shape

        size = (width,height)
        
        #inserting the frames into an image array
        frame_array.append(img)
    # out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size) 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'MPEG'), fps, size)
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()

def depth_read(img, sparse_val):
    # loads depth map D from png file
    # and returns it as a numpy array,
    # for details see readme.txt
    depth_png = np.array(img, dtype=int)
    y = depth_png
    depth_png = (65535*((y - y.min())/y.ptp())).astype(np.uint16)
    depth_png = np.expand_dims(depth_png, axis=2)
    # make sure we have a proper 16bit depth map here.. not 8bit!
    assert(np.max(depth_png) > 255)
    depth = depth_png.astype(np.float) / 256.
    depth[depth_png == 0] = sparse_val
    return depth


pathIn, pathOut  = 'Gib4/depth_selection/image/val/', 'Gib3/v_image.mp4'
create(pathIn, pathOut)


pathIn, pathOut  = 'Gib4/depth_selection/groundtruth_depth/val/', 'Gib3/v_groundtruth_depth.mp4'
create(pathIn, pathOut)

pathIn, pathOut  = 'Gib4/depth_selection/velodyne_raw_depth/val/', 'Gib3/v_velodyne_raw_depth.mp4'
create(pathIn, pathOut)

# pathIn, pathOut  = 'Saved/best_sj/gib3_results/', 'Gib3/v_gib_results_sj.mp4'
# create(pathIn, pathOut)

