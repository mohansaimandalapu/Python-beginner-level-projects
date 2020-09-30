from pytube import YouTube
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("link",type=str,help='give URL of vedio to br download')
parser.add_argument("resolution",type=str,nargs='?',help="Resolution of vedio to be download ('High','Medium','Low')",default="High")
parser.add_argument("file_path",type=str,nargs='?',help="file path to save vedio",default= './')

args = parser.parse_args()

def youtube_vedio_download(link,resolution,file_path):
    yt = YouTube(link)
    if resolution == "High":
        stream = yt.streams.all()[1]
    elif resolution == "Medium":
        stream = yt.streams.all()[5]
    else:
        stream = yt.streams.all()[-6]    
   
    print(f"Downloading video from YouTube to {str(file_path)} at {resolution} resolution ")
    stream.download(file_path)

if __name__ == "__main__":
   youtube_vedio_download(link=args.link,resolution = args.resolution,file_path = args.file_path) 