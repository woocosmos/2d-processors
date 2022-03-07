import argparse
import os
import glob
from PIL import Image
import sys
import shutil
from gif_processor import gif2frame

# input  : place original gif, key frame images in the same directory
# output : (deepsim) train_B with key images, train_reals with label images, test_reals with frames
#        : (ebsynth) keys with key images, video with frames, out


path_dict = {'deepsim':['train_B', 'test_reals', 'train_reals'], 
             'ebsynth':['keys', 'video', 'out']}


def set_dir(model):
    for d in path_dict[model]:
        os.mkdir(d)


def save_frames(gif_path, model):
    save_path = path_dict[model][1]        
    if len(os.listdir(save_path)) == 0:         # only when empty
        gif2frame(gif_path, save_path)


def rename_keys(key_path, frame_num, model):
    assert len(key_path) == len(frame_num), 'the number of key frames and frame numbers must be same'
    save_path = path_dict[model][0]
    
    # match key images with label images
    if model == 'deepsim':
        for k in range(len(key_path)):
            src = 'test_reals/frame_%03d.jpg' % int(frame_num[k])
            dst = 'train_reals/frame_%03d.jpg' % int(frame_num[k])
            shutil.copyfile(src, dst)
    
    for j in range(len(key_path)):
        os.rename(key_path[j], save_path + '/frame_%03d.jpg' % int(frame_num[j]))


# python3 preprocessor.py --model deepsim --key_path drawn1.jpg drawn2.jpg --frame_num 7 33
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)                                 # choose between deepsim and ebsynth
    parser.add_argument("--key_path", nargs="*", type=str, required=True)                   # specify key image files path in the order of frame numbers
    parser.add_argument("--frame_num", nargs="*", type=int, required=True, default=[0])     # specify key frame numbers
    args = parser.parse_args()
    
    assert args.model in ['deepsim', 'ebsynth'], 'specify the model - deepsim or ebsynth?'
    print(f"Preprocessing for {args.model} !")
    set_dir(args.model)

    gif_path = glob.glob('*.gif')[0]
    assert len(gif_path) == 1, "place only one gif file"
    print(f'Nice, I found the gif file to cook ! - {gif_path}')
    
    save_frames(gif_path, args.model)
    rename_keys(args.key_path, args.frame_num, args.model)
    print('finished.')