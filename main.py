import os

answer = input("Please enter a folder path or 'q' to exit: ")

while answer != 'q':
    try:
        # Change the working directory to the path provided by the user
        os.chdir(answer)
    except OSError as e:
        print(e)
    # Get all files and folders in this directory
    files = os.listdir(answer)
    name = input("Please enter the series name you would like for the files: ")
    season = input("And the season: ")
    print("Working on it..")
    for index, file in enumerate(files):
        # Rename each file to this format "Series Name - Season - Episode"
        os.rename(file, f'{name} - S{int(season):02} - E{index}.mp4')
    print("Done, Enjoy the series!")
    answer = input("Please enter a folder path or 'q' to exit: ")
