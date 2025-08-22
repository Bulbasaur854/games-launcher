import os

def scan_directory_for_games(directory):
    if (not os.path.isdir(directory)):
        print("Error: Given path is not a directory")    
        return    
    print(f"Scanning folder... ['{directory}']")

    games_paths = get_exe_files_recursive(directory)
    games_dict = generate_games_dictionary(games_paths)
    print(games_dict)

def get_exe_files_recursive(src_path):
    results = []

    if os.path.isfile(src_path):
        if src_path.lower().endswith(".exe"):
            results.append(src_path)
    else:
        try:
            for item in os.listdir(src_path):
                src_item = os.path.join(src_path, item)
                results.extend(get_exe_files_recursive(src_item))
        except PermissionError:
            pass
        except Exception as e:
            print(f"Error: {e}")

    return results

def generate_games_dictionary(paths):
    results = {}

    for path in paths:
        name = os.path.basename(path).split('.')[0]
        results[name] = path

    return results