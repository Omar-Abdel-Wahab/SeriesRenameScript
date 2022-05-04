import os
import sys

END_PROGRAM = ['q', 'Q']


def rename_files(path, name, season):
    change_directory(path)
    files = get_files()
    _, extension = os.path.splitext(files[0])
    new_files = []

    for episode_number, file in enumerate(files, start=1):
        # File name format = "Series_Name - Season_Number - Episode_Number.extension"
        new_file = f'{name} - S{int(season):02} - E{episode_number:02}{extension}'
        os.rename(file, new_file)
        new_files.append(new_file)

    return new_files


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


def ask_for_name_and_season():
    name = input("Enter the series name you would like for the files: ")
    season = input("And the season: ")

    return name, season


def ask_for_path_or_exit():
    answer = input("Enter a folder path or 'q' to exit: ")
    return answer


if __name__ == "__main__":

    while True:
        folder_path = ask_for_path_or_exit()
        if folder_path in END_PROGRAM:
            break
        else:
            basename, season_number = ask_for_name_and_season()
            print("Working on it..")
            rename_files(folder_path, basename, season_number)
            print("Done, Enjoy the series!")
