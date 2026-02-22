import argparse
import os
from program.autompg import AutoMPGData

def my_parser():
    """
    Command-Line Interface for AutoMPGData Processing, allows users
    to process and sort automobile MPG data using command-line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('log', type=str, help='Name of log file my_log.log')
    parser.add_argument('save', type=str, help='Store output in log file')
    parser.add_argument('-y', '--year', action='store_true', help='Sort data by year')
    parser.add_argument('-m', '--mpg', action='store_true', help='Sort data by mpg')


    return parser

if __name__ == "__main__":
    parser = my_parser()
    args = parser.parse_args()

    log_folder = args.log
    save_folder = args.save
    sort_year = args.year
    sort_mpg = args.mpg

    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    auto_mpg_data = AutoMPGData(sort_year=sort_year, sort_mpg=sort_mpg)
    sorted_data = auto_mpg_data.sort_data()

    if sort_year and sort_mpg:
        file_name = 'auto.data.year.mpg.txt'
    elif sort_year:
        file_name = 'auto.data.year.txt'
    elif sort_mpg:
        file_name = 'auto.data.mpg.txt'
    else:
        file_name = 'auto-mpg.data.txt'

    file_path = os.path.join(save_folder, file_name)
    auto_mpg_data.save_data(file_path)

    print(f'Data saved to {file_path}')

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣵⣿⠿⢟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠈⡀⠀⠀⠀⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⢛⠩⠥⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⢀⡠⠖⠉⡠⢶⡄⠀⣀⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠋⠀⡀⠀⢠⣾⣿⣿⣿⣿⣿⡿⢋⡵⠛⢁⣠⠶⠋⣀⣀⣠⠴⠋⠁⠀⠟⣁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⣠⡾⠋⢁⡀⢰⠄⣴⣿⣿⣿⣿⣿⢟⡡⠞⠉⢀⣴⠟⠁⠀⣾⠟⠋⢀⣀⠀⡠⣠⣾⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣜⡟⠁⡴⠟⢀⠆⣼⣿⣿⣿⡿⢟⡤⠊⠀⢀⣴⠟⢁⠀⢀⣆⣠⣾⠀⠟⣡⢞⣵⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⢀⣾⡏⠀⠈⠀⠀⠊⣾⡟⣿⣿⠋⡴⠋⠀⠀⣠⡿⠃⠀⠀⣰⣿⣿⣿⢃⣴⣿⣵⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⢸⡇⣿⣿⠁⠀⠀⠀⣠⣼⠋⠜⠉⡡⠊⠀⢠⢏⣼⠏⡠⢂⠀⢠⣻⣿⠋⠁⣠⣵⠆⠙⠛⠿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⣸⡟⢻⡇⠀⠀⠀⠀⡿⠁⠀⠀⠄⠀⠀⣰⢃⡾⢁⣼⣷⢋⡄⣾⣿⡏⢠⡾⠟⣁⠤⠀⠀⠀⢼⣿⣿⠇⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀
# ⠀⢹⡇⠆⡇⠀⠀⠀⠸⠁⠀⠀⠂⠀⠀⢰⣧⡞⢠⣿⡿⢁⣾⣿⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡟⠀⠀⠀⡼⠁⣴⣷⠀⠀⠀⠀⠀
# ⠀⠸⠃⠀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡟⢡⣿⡟⠀⢾⣿⡏⣿⣿⡇⠀⠀⠀⢠⣤⣄⣀⠒⠀⠀⠀⠀⠀⠀⠁⢀⠈⠁⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢰⣿⣁⣾⣿⡇⠈⠙⠛⠇⣿⣿⡇⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⣆⠀⠀⠀⠀⢠⠀⠠⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⣿⣿⣿⡿⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣆⠀⠀⠀⠈⠀⠀⡠⠃⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⢿⡇⢀⣴⠀⢸⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⣠⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠘⣧⢆⠻⠀⡄⢿⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠇⢴⣿⣿⠟⣣⣴⢿⣿⠿⠿⠛⠿⡆⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠈⡀⠐⠢⠈⠸⣷⡀⢳⠈⠀⢸⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣦⣤⣤⣈⣠⣺⠇⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⢃⠀⠀⠀⠁⠛⠁⣸⡇⠀⢸⠀⠐⣿⠄⠀⠀⠀⠀⠀⡀⠀⢰⣿⣿⣿⣿⣿⣿⠿⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⢻⡷⠆⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣛⣋⠁⢤⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⠖⢒⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡙⠛⠿⢿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⡁⠰⣶⡄⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠦⠀⠾⠿⠿⠦⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡦⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠸⠿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣤⣀⣠⣤⣤
# ⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿