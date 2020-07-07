import os

answer = input("Please enter a folder path or 'q' to exit: ")


def rename_files(ans):
    try:
        # Change the working directory to the path provided by the user
        os.chdir(ans)
    except OSError as e:
        print(e)
    # Get all files and folders in this directory
    files = os.listdir(ans)
    name = input("Please enter the series name you would like for the files: ")
    season = input("And the season: ")
    print("Working on it..")
    exts = []
    for file in files:
        file_path = os.path.join(os.getcwd(), file)
        # Check if there is a sub-folder in the current folder. If so, remove it
        if os.path.isdir(file_path):
            files.remove(file)
        else:
            _, file_ext = os.path.splitext(file_path)
            exts.append(file_ext)
    for episode_number, file in enumerate(files):
        # Rename each file to this format "Series Name - Season - Episode. Associated extension"
        os.rename(file, f'{name} - S{int(season):02} - E{episode_number + 1}{exts[episode_number]}')
    print("Done, Enjoy the series!")


while answer != 'q':
    rename_files(answer)
    answer = input("Please enter a folder path or 'q' to exit: ")


