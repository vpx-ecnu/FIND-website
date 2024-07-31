import cv2
import os
import glob
import imageio

vs = glob.glob("/sdc/ccg/workspace/ClothPPO-website/static/find_imgs/*.mp4")

for p in vs:
    video_path = p
    gif_path = p.replace("find_imgs", "find_videos").replace("mp4", "gif")

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    frames = []  # 存储帧的列表

    # 检查视频是否打开成功
    if not cap.isOpened():
        print("Error opening video file")
    else:
        # 逐帧读取视频
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # 将BGR格式转换为RGB格式（imageio保存GIF需要RGB格式）
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(rgb_frame)

        # 释放视频捕获对象
        cap.release()

        # 使用imageio保存帧为GIF
        imageio.mimsave(gif_path, frames, fps=8, loop=0)  # fps是每秒帧数，根据需要调整
    # cv2.destroyAllWindows()
