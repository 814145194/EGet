import os
import shutil
from moviepy.editor import AudioFileClip
video_path=os.listdir('video')
print("读入视频文件")
print(video_path)
for i in range(len(video_path)):
    my_audio_clip = AudioFileClip('video/'+video_path[i])
    (filename, extension) = os.path.splitext(video_path[i])
    try:
        my_audio_clip.write_audiofile('music/' + filename + '.mp3')
    except:
        shutil.copyfile('video/'+video_path[i], 'music/'+video_path[i])

print("转换完成！")
input()

