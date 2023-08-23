
def user_selection(line, next_line):
    print(f"""
            Actual Line: {line}
            Next Line: {next_line}
            Please enter how to end this line.
            1) Add a brake line.
            2) Add a blank space.
            other to add nothing.
            """)
    user_input = input("Your choice: ")
    if user_input == '1':
        return '\n';
    elif user_input == '2':
        return ' ';
    else:
        return '';

def manual_selection_process(content, record_identifier):
    new_content = '';
    lines = content.splitlines();
    for idx, line in enumerate(lines):
        new_content += line;
        if idx < len(lines) - 1:
            if lines[idx+1].startswith(record_identifier) and len(line) != 0:
                new_content += '\n';
            else:
                new_content += user_selection(line,lines[idx+1]);

    return new_content;


def manual_selection(content):
    record_identifier = input("Please enter the initial text that identifies the different records: ");

    return manual_selection_process(content, record_identifier);