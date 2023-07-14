import os

from pytube import YouTube

while True:
    user_input = input('What do you want to do?:\n'
                       '1. Download from YT (input link)\n'
                       '2. Change download default location (default where .exe is.)\n'
                       '3. Exit\n'
                       '')
    if user_input == '1':
        link = input('Input YT link: ')
        yt = YouTube(link).streams.filter(only_audio=True).first()
        try:
            try:
                downloaded_file = yt.download(location)
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)
                print("\nDone\n")
            except NameError:
                downloaded_file = yt.download()
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)
                print("\nDone\n")
        except FileExistsError:
            print("\nFile already exists\n")

    elif user_input == '2':
        location = input('where do you wanna output file (example "D:/test/" or blank)?')

    elif user_input == '3':
        break
    else:
        print('Wrong input. It only can be 1, 2 or 3')