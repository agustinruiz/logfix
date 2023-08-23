import re;
from file_utils import save_output_file, open_input_file;

def by_record_identifier_process(content, record_identifier):
    pattern = r'\n(?!' + re.escape(record_identifier) + r')';
    return re.sub(pattern, '', content);

def by_record_identifier(filename):
    record_identifier = input("Please enter the initial text that identifies the different records: ");

    file_content = open_input_file(filename);

    if file_content:
        new_content = by_record_identifier_process(file_content, record_identifier);
        save_output_file(f"{filename}-fixed",new_content);

def by_recordID_and_line_length_process(content, line_length, record_identifier):
    new_content = '';
    lines = content.splitlines();
    for idx, line in enumerate(lines):
        new_content += line;
        if idx < len(lines) - 1:
            if lines[idx+1].startswith(record_identifier) and len(line) != 0:
                new_content += '\n';
            elif len(line) == int(line_length) - 1:
                new_content += ' ';
            elif len(line) < int(line_length) and len(line) != 0:
                new_content += '\n';

    return new_content;

def by_recordID_and_line_length(filename):
    record_identifier = input("Please enter the initial text that identifies the different records: ");
    line_length = input("Please enter the length of the line: ");
    file_content = open_input_file(filename);

    if file_content:
        new_content = by_recordID_and_line_length_process(file_content, line_length, record_identifier);
        save_output_file(f"{filename}-fixed",new_content);

def analysis_menu(analysis_options):
    user_input = '';

    input_message = "Pick an option:\n";

    for key, (descriptor, _) in analysis_options.items():
        input_message += f'{key}) {descriptor}\n';

    input_message += 'Your choice: ';

    while user_input not in analysis_options.keys():
        user_input = input(input_message);

    print('You picked: ' + analysis_options[user_input][0]);
    return analysis_options[user_input];


def main():
    filename = input("Please enter the file path: ");

    analysis_options = {
        '1': ('Only by record identifier', by_record_identifier),
        '2': ('By record identifier and line length', by_recordID_and_line_length),
    }

    analysis_choice = analysis_menu(analysis_options);

    analysis_choice[1](filename);

    

if __name__ == "__main__":
    main();