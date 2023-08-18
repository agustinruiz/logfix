import re;
from file_utils import save_output_file, open_input_file;

def content_process(content, record_identifier):
    pattern = r'\n(?!' + re.escape(record_identifier) + r')';
    return re.sub(pattern, '', content);

def logfix_process(filename, record_identifier):
    file_content = open_input_file(filename);

    if file_content:
        new_content = content_process(file_content, record_identifier);
        save_output_file(f"{filename}-fixed",new_content);


def main():
    filename = input("Please enter the file path: ");

    record_identifier = input("Please enter the initial text that identifies the diferents records: ");

    logfix_process(filename, record_identifier);

    

if __name__ == "__main__":
    main();