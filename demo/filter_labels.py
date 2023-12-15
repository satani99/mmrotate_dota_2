import os

def remove_lines_from_file(file_path, condition):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove lines that doesn't match the condition
    modified_lines = [line for line in lines if condition(line)]

    with open(file_path, 'w') as file:
        file.writelines(modified_lines)

def main():
    folder_paths = ['split_ss_dota/train/annfiles/', 'split_ss_dota/val/annfiles/']
    condition_to_remove = lambda line: 'storage-tank' in line or 'small-vehicle' in line or 'large-vehicle' in line or 'roundabout' in line or 'container-crane' in line

    for folder_path in folder_paths:
    	for filename in os.listdir(folder_path):
        	if filename.endswith('.txt'):
        	    file_path = os.path.join(folder_path, filename)
        	    remove_lines_from_file(file_path, condition_to_remove)
        	    print(f"Lines removed from {filename}")

if __name__ == "__main__":
    main()
