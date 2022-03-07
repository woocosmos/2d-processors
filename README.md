## Easy 2D Processors
Hi, my name is Yunsoo Woo. I made this repository to make it easy to handle gifs.

지원하는 기능
* 움짤에서 프레임 추출
    * 투명 움짤일 경우 흰 배경으로 채움
* 프레임에서 움짤 생성
* DeepSIM 훈련을 위한 데이터 세팅
* EbSynth 프로그램 실행을 위한 데이터 세팅

## History
### v1.0
* 기본 기능


## ```gif_processor.py```

### extracting frames from gif
```
python3 gif_processor.py --gif_path test.gif --save_path result
```
This extracts frames from ```--gif_path``` and save them in ```--save_path``` directory.

### making gif from frames
```
python3 gif_processor.py --dir_path frames --save_path result --deepsim True
```
This makes a gif file from the frames which are stored in ```--dir_path``` directory and save it in ```--save_path``` directory (If ```--save_path``` is not specified, the result gif file will be saved in the working directory). 
* If ```--deepsim``` flag is on, it produces a gif file from DeepSIM output.

## ```prepare_data.py```
### preparing data for DeepSIM

```
python3 prepare_data.py --model deepsim --key_path drawn1.jpg drawn2.jpg --frame_num 7 33
```

This creates three directories: ```train_B```, ```train_reals```, ```test_reals```. It detects a sole gif file and extracts frames to save them in ```test_reals``` directory (If frames alreay exist, this step will be skipped). 

* ```--key_path``` specifies the key frame images that will be moved ```train_B``` directory, while the corresponding label images are copied to ```train_reals```.
* ```--frame_num``` specifies the frame number of the given image files. Note that the order of the given key image paths should match that of the given frame numbers. 
    
### preparing data for EbSynth

```
python3 prepare_data.py --model ebsynth --key_path drawn1.jpg drawn2.jpg --frame_num 7 33
```

This creates three directories: ```keys```, ```out```, ```video```. It detects a sole gif file and extracts frames to save them in ```video``` directory (If frames alreay exist, this step will be skipped). 

* ```--key_path``` specifies the key frame images that will be moved ```keys``` directory.
* ```--frame_num``` specifies the frame number of the given image files. Note that the order of the given key image paths should match that of the given frame numbers. 
