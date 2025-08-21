import os

def scan_directory_for_games(directory):
    if (not os.path.isdir(directory)):
        print("Error: Given path is not a directory")    
        return    
    print(f"Scanning folder... ['{directory}']")

    game_paths = get_exe_files_recursive(directory)
    print_games_file_names(game_paths)

def get_exe_files_recursive(src_path):
    results = []

    if os.path.isfile(src_path):
        if src_path.endswith(".exe"):
            results.append(src_path)
    else:
        for item in os.listdir(src_path):
            src_item = os.path.join(src_path, item)
            results.extend(get_exe_files_recursive(src_item))

    return results

def print_games_file_names(paths_list):
    index = 1
    for path in paths_list:       
        game_file_name = os.path.basename(path)
        print(f"{index}. {game_file_name}")
        index += 1