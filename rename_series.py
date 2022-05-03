import os
import sys

END_PROGRAM = ['q', 'Q']


def rename_files(path, name, season):
    change_directory(path)
    files = get_files()
    _, extension = os.path.splitext(files[0])

    for episode_number, file in enumerate(files, start=1):
        # File name format = "Series_Name - Season_Number - Episode_Number.extension"
        os.rename(file, f'{name} - S{int(season):02} - E{episode_number:02}{extension}')


def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Please check that the entered folder exists or use an absolute path")
        sys.exit()


def get_files():
    files = os.listdir()

    for file in files:
        if os.path.isdir(file):
            files.remove(file)

    return files


def ask_for_input_or_exit():
    answer = input("Enter a folder path or 'q' to exit: ")
    if answer in END_PROGRAM:
        return answer, None, None

    name = input("Enter the series name you would like for the files: ")
    season = input("And the season: ")

    return answer, name, season


if __name__ == "__main__":

    while True:
        folder_path, basename, season_number = ask_for_input_or_exit()
        if folder_path in END_PROGRAM:
            break
        else:
            print("Working on it..")
            rename_files(folder_path, basename, season_number)
            print("Done, Enjoy the series!")
