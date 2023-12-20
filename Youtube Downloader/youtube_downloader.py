from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video():
    video_url = url_entry.get()
    save_path = open_file_dialog()

    if save_path:
        try:
            yt = YouTube(video_url)
            streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highest_res = streams.get_highest_resolution()
            
            # Disable the button during download
            download_button.config(text="Downloading", state=tk.DISABLED)
            
            highest_res.download(output_path=save_path)

            result_label.config(text="Video downloaded successfully.")
        
        except Exception as e:
            result_label.config(text=f"Error: {e}")
        
        finally:
            # Re-enable the button after download completes
            download_button.config(text="Download", state=tk.NORMAL)

    else:
        result_label.config(text="Invalid save location.")

def open_file_dialog():
    folder = filedialog.askdirectory()

    if folder:
        print(f"Selected folder: {folder}")

    return folder

# GUI setup
root = tk.Tk()
root.title("YouTube Video Downloader")

# Entry for YouTube URL
url_label = tk.Label(root, text="Enter YouTube video link:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=10)

# Button to trigger download
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=10)

# Label to display download result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
