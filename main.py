from moviepy.editor import VideoFileClip

def convert_mp4_to_mp3(mp4_file, mp3_file):
    video = VideoFileClip(mp4_file)
    audio = video.audio
    audio.write_audiofile(mp3_file)
    
# Example usage
mp4_file_path = input("Enter video file location: ")
mp3_file_path = input("Enter music file save location: ")

convert_mp4_to_mp3(mp4_file_path, mp3_file_path)