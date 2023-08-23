from file_utils import save_output_file, open_input_file;

from analysis import analysis;

def main():
    filename = input("Please enter the file path: ");
    file_content = open_input_file(filename);
    if file_content is None: exit;

    new_content = analysis(file_content);    

    save_output_file(f"{filename}-fixed",new_content);

if __name__ == "__main__":
    main();