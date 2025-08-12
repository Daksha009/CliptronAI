# this file looks for new folders inside user upload and converts them to a reel if  they are alredy converted.
import os

def text_to_audio(folder):
    print("TTA -", folder)

def create_reel(folder):
    print("CR -", folder)

if __name__ == "__main__":
  with  open("done.txt", "r") as f:
     done_folders = f.readlines()
  
  folders = os.listdir("user_uploads")
  print(folders,done_folders)
  for folder in folders:
     if(folder not in done_folders):
         text_to_audio(folder) #generate the audio.mp3 from desc.txt
         create_reel(folder) # convert the images and audio.mp3 inside the folder to a reel
         with open("done.txt", "a") as f:
            f.write(folder + "\n") # mark this folder as done
