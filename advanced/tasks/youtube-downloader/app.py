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

def download_youtube_video(url, selected_format, download_dir, selected_videos=None):
    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    ydl_opts = {
        'format': selected_format,
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': False,  # Set to True to suppress output
        'noprogress': False,  # Show progress bar
    }

    with YoutubeDL(ydl_opts) as ydl:
        if selected_videos is None:
            # Download the entire video or all videos in the playlist
            ydl.download([url])
        else:
            # Download only the selected videos from the playlist
            for video in selected_videos:
                ydl.download([video['url']])

def download_single_video(url, selected_format, download_dir):
    """Function to handle downloading a single video."""
    download_youtube_video(url, selected_format, download_dir)

def download_playlist(url, selected_format, download_dir, selected_videos=None):
    """Function to handle downloading a playlist."""
    download_youtube_video(url, selected_format, download_dir, selected_videos)

def get_download_directory():
    """Prompt the user for a download directory with a default option."""
    default_dir = os.path.expanduser('~/Downloads')
    prompt = f"Enter the download directory [default: {default_dir}]: "
    user_input = input(prompt).strip()
    if user_input:
        # Expand user (~) and environment variables
        download_dir = os.path.expanduser(os.path.expandvars(user_input))
    else:
        download_dir = default_dir
    return download_dir

def get_user_choice(prompt, options, default):
    """
    Generic function to get user input with a default value.

    :param prompt: The input prompt to display.
    :param options: A list of valid options as strings.
    :param default: The default value to return if user presses Enter.
    :return: The user's choice, defaulting if necessary.
    """
    while True:
        choice = input(prompt).strip()
        if not choice:
            return default
        if choice in options:
            return choice
        else:
            print(f"Invalid input. Please enter one of the following options: {', '.join(options)}")

def main():
    print("\n" + "-" * 50)
    print(" YOUTUBE VIDEO/PLAYLIST DOWNLOADER ".center(50))
    print("-" * 50 + "\n")

    # Prompt the user to choose between downloading a video or a playlist with default
    print("Please choose what you want to download:")
    print("1. Single Video")
    print("2. Playlist")
    print("-" * 50)
    choice_prompt = "Enter the number corresponding to your choice (1 or 2) [default: 1]: "
    choice = get_user_choice(choice_prompt, ['1', '2'], '1')

    # Get the download directory from the user
    download_dir = get_download_directory()
    print(f"\nDownload directory set to: {download_dir}\n")

    if choice == '1':
        # User chose to download a single video
        video_url = input("Enter the URL of the YouTube video [required]: ").strip()
        while not video_url:
            print("Video URL cannot be empty.")
            video_url = input("Enter the URL of the YouTube video [required]: ").strip()

        print("\n" + "-" * 50)
        print(" SELECT VIDEO QUALITY ".center(50))
        print("-" * 50)
        print("1. Best")
        print("2. High (1080p)")
        print("3. Medium (720p)")
        print("4. Low (480p)")
        print("-" * 50)
        quality_prompt = "Enter the number corresponding to the desired quality [default: 1]: "
        quality_choice = get_user_choice(quality_prompt, ['1', '2', '3', '4'], '1')

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
        download_single_video(video_url, selected_format, download_dir)

        print("\n" + "-" * 50)
        print(" DOWNLOAD COMPLETED ".center(50))
        print("-" * 50 + "\n")

    elif choice == '2':
        # User chose to download a playlist
        playlist_url = input("Enter the URL of the YouTube playlist [required]: ").strip()
        while not playlist_url:
            print("Playlist URL cannot be empty.")
            playlist_url = input("Enter the URL of the YouTube playlist [required]: ").strip()

        # Add message to tell the user to wait while checking the URL
        print("\nChecking the playlist... Please wait.\n")

        # Check if the URL is a playlist
        info_dict = list_videos_in_playlist(playlist_url)
        if 'entries' in info_dict:
            print("\n" + "-" * 50)
            print(" PLAYLIST DETECTED ".center(50))
            print("-" * 50 + "\n")

            # Ask if the user wants to download the entire playlist or just specific videos with default
            download_choice_prompt = "Do you want to download the entire playlist? (y/n) [default: y]: "
            download_choice = input(download_choice_prompt).strip().lower()
            if not download_choice:
                download_choice = 'y'
            elif download_choice not in ['y', 'n']:
                print("Invalid input. Defaulting to downloading the entire playlist.")
                download_choice = 'y'

            if download_choice == 'y':
                selected_videos = None  # This means all videos in the playlist will be downloaded
            else:
                # List videos in the playlist and allow user to choose
                print("\nAvailable videos in the playlist:")
                print("-" * 50)
                for i, entry in enumerate(info_dict['entries']):
                    title = entry.get('title', 'No Title')
                    print(f"{i + 1}. {title}")
                print("-" * 50)

                video_indices = input("Enter the numbers of the videos you want to download (e.g., 1,3,5) [default: all]: ").strip()
                if not video_indices:
                    # If user presses Enter without input, default to all videos
                    selected_videos = None
                else:
                    try:
                        # Split the input by commas and convert to zero-based indices
                        selected_indices = [int(x.strip()) - 1 for x in video_indices.split(',') if x.strip().isdigit()]
                        # Validate indices
                        selected_indices = [i for i in selected_indices if 0 <= i < len(info_dict['entries'])]
                        selected_videos = [info_dict['entries'][i] for i in selected_indices]
                        if not selected_videos:
                            print("No valid videos selected. Exiting.")
                            exit(1)
                    except ValueError:
                        print("Invalid input. No videos will be downloaded.")
                        selected_videos = []

        else:
            print("The provided URL does not appear to be a playlist. Exiting.")
            exit(1)

        # Ask the user for the desired quality with default
        print("\n" + "-" * 50)
        print(" SELECT VIDEO QUALITY ".center(50))
        print("-" * 50)
        print("1. Best")
        print("2. High (1080p)")
        print("3. Medium (720p)")
        print("4. Low (480p)")
        print("-" * 50)
        quality_prompt = "Enter the number corresponding to the desired quality [default: 1]: "
        quality_choice = get_user_choice(quality_prompt, ['1', '2', '3', '4'], '1')

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
        download_playlist(playlist_url, selected_format, download_dir, selected_videos)

        print("\n" + "-" * 50)
        print(" DOWNLOAD COMPLETED ".center(50))
        print("-" * 50 + "\n")

    else:
        print("Invalid choice. Please run the program again and select either 1 or 2.")

if __name__ == "__main__":
    main()
