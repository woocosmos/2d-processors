import argparse
from PIL import Image
import imageio
import glob

def gif2frame(gif_path, save_path):
    im = Image.open(gif_path)
    x, y = im.size
    try:
        while True:
            num = im.tell()+1
            im.seek(im.tell()+1)
            background = Image.new("RGBA", (x, y), "WHITE")
            filled = Image.alpha_composite(background, im.convert('RGBA'))
            filled.convert('RGB').save(save_path + '/frame_%03d.jpg' % num)
    except EOFError:
        pass
    
    
def frame2gif(dir_path, save_path, deepsim=False):
    images = []
    filenames = glob.glob(dir_path + '/*.jpg')
    filenames.sort()
    
    if deepsim:    
        filenames = [f for f in filenames if "synthesized" in f]

    for filename in filenames:
        images.append(imageio.imread(filename))
        
    imageio.mimsave(save_path + '/result.gif', images)


if __name__ == "__main__":
    # python3 --gif_path test.gif --save_path result
    # python3 --dir_path frames --deepsim True
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--gif_path", type=str)                   # make gif from frames
    parser.add_argument("--dir_path", type=str)                   # extract frames from gif
    parser.add_argument("--save_path", type=str, default='.')     # save the result(s) in this path
    parser.add_argument("--deepsim", type=bool, default=False)    # deepsim
    args = parser.parse_args()

    if args.gif_path:
        gif2frame(args.gif_path, args.save_path)
        
    if args.dir_path:
        frame2gif(args.dir_path, args.save_path, args.deepsim)