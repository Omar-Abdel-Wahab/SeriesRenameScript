import os
import sys

END_PROGRAM = ['q', 'Q']


def rename_files(files, new_name):
    series_name, season = new_name[0], new_name[1]
    _, extension = os.path.splitext(files[0])
    new_files = []

    for episode_number, file in enumerate(files, start=1):
        new_file = f'{series_name} - S{int(season):02} - E{episode_number:02}{extension}'
        os.rename(file, new_file)
        new_files.append(new_file)

    return new_files


def get_files(path):
    change_directory(path)
    files = os.listdir()

    for file in files:
        if os.path.isdir(file):
            files.remove(file)

    return files


def change_directory(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Please check that the entered folder exists or use an absolute path")
        sys.exit()


def ask_for_path_or_exit():
    answer = input("Enter a folder path or 'q' to exit: ")
    return answer


def ask_for_name_and_season():
    name = input("Enter the series name you would like for the files: ")
    season = input("And the season: ")

    return name, season


if __name__ == "__main__":

    while True:
        folder_path = ask_for_path_or_exit()
        if folder_path in END_PROGRAM:
            break
        else:
            new_file_name = ask_for_name_and_season()
            returned_files = get_files(folder_path)
            rename_files(returned_files, new_file_name)
            print("Done, Enjoy the series!")
