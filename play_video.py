import base64 
import subprocess 

# 從 string 轉換為 mp4
def base64_to_mp4(base64_string):
    try:
        mp4_binary_data = base64.b64decode(base64_string)
         
        video_path = "/home/lynn/makeVideo/text-to-video-ms-1.7b/damo-vilab/test_gen.mp4"
        with open(video_path, 'wb') as mp4_file:
            mp4_file.write(mp4_binary_data)
        
        print(f" video_path{video_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"video_path={video_path}")
    return  video_path


# 播放影片 
def play_video(base64_string):
    # 使用subprocess運行mpv命令
    try:
        video_path=base64_to_mp4(base64_string)
        subprocess.run(["mpv", video_path])
        print("success play!")

    except Exception as e:
        print(f"Error: {e}")  
