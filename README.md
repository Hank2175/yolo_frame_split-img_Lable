We can use "frame_generator.py" to split video.  
e.g in this repository:  
        python frame_generator.py --dataset_folder MJ --locations second_round  
        (It is necessary to place video user folder "MJ/second_round/video/")  
        (Processed png images would place in "MJ/second_round/frame/")  
  
After we got the PNGs file, like "MJ/second_round/frame/_VIDEO_NAME_".  
Please copy it into "MJ/second_round/frame/original".  
After that, use "MJ/second_round/frame/auto_label.py" to mark automatic.  
e.g:  
        python auto_label.py --YOLO_MODULE '_WHERE_YOUR_TRAINED_MODEL_/runs/detect/train2/weights/best.pt'  
