from moviepy.video.io.VideoFileClip import VideoFileClip
import tkinter as tk
from tkinter import filedialog
import os

def convert_to_whatsapp_compatible(input_file, output_file):
    try:
        # Load the video file
        clip = VideoFileClip(input_file)
        
        # Define WhatsApp-compatible parameters
        target_resolution = (640, 360)  # Width x Height
        target_bitrate = "488k"         # Total bitrate limit
        target_audio_bitrate = "128k"   # Audio bitrate limit
        
        # Resize video to target resolution
        resized_clip = clip.resize(height=target_resolution[1])  # Maintain aspect ratio
        
        # Export with WhatsApp-compatible settings
        resized_clip.write_videofile(
            output_file,
            codec="libx264",             # WhatsApp prefers H.264 codec
            audio_codec="aac",           # WhatsApp-compatible audio codec
            bitrate=target_bitrate,      # Adjust video bitrate
            audio_bitrate=target_audio_bitrate
        )
        
        # Close the clips to free resources
        clip.close()
        resized_clip.close()
        print(f"Conversion completed! File saved as: {output_file}")
        
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")

def select_and_convert_files():
    # Create root window but hide it
    root = tk.Tk()
    root.withdraw()
    
    # Let user select multiple MP4 files
    file_paths = filedialog.askopenfilenames(
        title="Select MP4 files to convert",
        filetypes=[("MP4 files", "*.mp4")]
    )
    
    if not file_paths:
        print("No files selected. Exiting...")
        return
    
    # Process each selected file
    for input_file in file_paths:
        # Create output filename by adding "_whatsapp" before the extension
        file_dir = os.path.dirname(input_file)
        file_name = os.path.basename(input_file)
        name_without_ext = os.path.splitext(file_name)[0]
        output_file = os.path.join(file_dir, f"{name_without_ext}_whatsapp.mp4")
        
        print(f"\nProcessing: {file_name}")
        convert_to_whatsapp_compatible(input_file, output_file)

if __name__ == "__main__":
    print("WhatsApp Video Converter")
    print("------------------------")
    print("Select the MP4 files you want to convert...")
    select_and_convert_files()
    input("\nPress Enter to exit...")