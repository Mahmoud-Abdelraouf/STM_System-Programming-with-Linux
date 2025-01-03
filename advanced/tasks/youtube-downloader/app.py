import os
from yt_dlp import YoutubeDL

def list_videos_in_playlist(url):
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Extract metadata without downloading
        'force_generic_extractor': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        return info_dict

def download_youtube_video(url, selected_format, selected_videos=None):
    ydl_opts = {
        'format': selected_format,
        'outtmpl': os.path.expanduser('~/Downloads/%(title)s.%(ext)s'),
    }

    with YoutubeDL(ydl_opts) as ydl:
        if selected_videos is None:
            # Download the entire video or all videos in the playlist
            ydl.download([url])
        else:
            # Download only the selected videos from the playlist
            for video in selected_videos:
                ydl.download([video['url']])

def download_single_video(url, selected_format):
    """Function to handle downloading a single video."""
    download_youtube_video(url, selected_format)

def download_playlist(url, selected_format, selected_videos=None):
    """Function to handle downloading a playlist."""
    download_youtube_video(url, selected_format, selected_videos)

if __name__ == "__main__":
    print("\n" + "-" * 50)
    print(" YOUTUBE VIDEO/PLAYLIST DOWNLOADER ".center(50))
    print("-" * 50 + "\n")

    # Prompt the user to choose between downloading a video or a playlist
    print("Please choose what you want to download:")
    print("1. Single Video")
    print("2. Playlist")
    print("-" * 50)
    choice = input("Enter the number corresponding to your choice (1 or 2): ").strip()

    if choice == '1':
        # User chose to download a single video
        video_url = input("\nEnter the URL of the YouTube video: ")

        print("\n" + "-" * 50)
        print(" SELECT VIDEO QUALITY ".center(50))
        print("-" * 50)
        print("1. Best")
        print("2. High (1080p)")
        print("3. Medium (720p)")
        print("4. Low (480p)")
        print("-" * 50)
        quality_choice = input("Enter the number corresponding to the desired quality: ")

        # Map the user's choice to a format string
        quality_map = {
            '1': 'bestvideo+bestaudio/best',
            '2': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '3': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '4': 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        }

        # Select the format based on user input
        selected_format = quality_map.get(quality_choice, 'best')

        print("\n" + "-" * 50)
        print(" DOWNLOADING VIDEO ".center(50))
        print("-" * 50 + "\n")

        # Download the single video
        download_single_video(video_url, selected_format)

        print("\n" + "-" * 50)
        print(" DOWNLOAD COMPLETED ".center(50))
        print("-" * 50 + "\n")

    elif choice == '2':
        # User chose to download a playlist
        playlist_url = input("\nEnter the URL of the YouTube playlist: ")

        # Add message to tell the user to wait while checking the URL
        print("\nChecking the playlist... Please wait.\n")

        # Check if the URL is a playlist
        info_dict = list_videos_in_playlist(playlist_url)
        if 'entries' in info_dict:
            print("\n" + "-" * 50)
            print(" PLAYLIST DETECTED ".center(50))
            print("-" * 50 + "\n")

            # Ask if the user wants to download the entire playlist or just specific videos
            download_choice = input("Do you want to download the entire playlist? (y/n): ").strip().lower()

            if download_choice == 'y':
                selected_videos = None  # This means all videos in the playlist will be downloaded
            else:
                # List videos in the playlist and allow user to choose
                print("\nAvailable videos in the playlist:")
                print("-" * 50)
                for i, entry in enumerate(info_dict['entries']):
                    print(f"{i + 1}. {entry.get('title', 'No Title')}")
                print("-" * 50)

                video_indices = input("\nEnter the numbers of the videos you want to download (e.g., 1,3,5): ")
                try:
                    selected_indices = [int(x.strip()) - 1 for x in video_indices.split(',')]
                    # Validate indices
                    selected_indices = [i for i in selected_indices if 0 <= i < len(info_dict['entries'])]
                    selected_videos = [info_dict['entries'][i] for i in selected_indices]
                except ValueError:
                    print("Invalid input. No videos will be downloaded.")
                    selected_videos = []

        else:
            print("The provided URL does not appear to be a playlist. Exiting.")
            exit(1)

        # Ask the user for the desired quality
        print("\n" + "-" * 50)
        print(" SELECT VIDEO QUALITY ".center(50))
        print("-" * 50)
        print("1. Best")
        print("2. High (1080p)")
        print("3. Medium (720p)")
        print("4. Low (480p)")
        print("-" * 50)
        quality_choice = input("Enter the number corresponding to the desired quality: ")

        # Map the user's choice to a format string
        quality_map = {
            '1': 'bestvideo+bestaudio/best',
            '2': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
            '3': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            '4': 'bestvideo[height<=480]+bestaudio/best[height<=480]'
        }

        # Select the format based on user input
        selected_format = quality_map.get(quality_choice, 'best')

        print("\n" + "-" * 50)
        print(" DOWNLOADING PLAYLIST ".center(50))
        print("-" * 50 + "\n")

        # Download the selected video(s) or the entire playlist
        download_playlist(playlist_url, selected_format, selected_videos)

        print("\n" + "-" * 50)
        print(" DOWNLOAD COMPLETED ".center(50))
        print("-" * 50 + "\n")

    else:
        print("Invalid choice. Please run the program again and select either 1 or 2.")
