
def by_recordID_and_line_length_content_process(content, line_length, record_identifier):
    new_content = '';
    lines = content.splitlines();
    for idx, line in enumerate(lines):
        new_content += line;
        if idx < len(lines) - 1:
            if lines[idx+1].startswith(record_identifier) and len(line) != 0:
                new_content += '\n';
            elif len(line) == line_length - 1:
                new_content += ' ';
            elif len(line) < line_length and len(line) != 0:
                new_content += '\n';

    return new_content;

def by_recordID_and_line_length(content):
    record_identifier = input("Please enter the initial text that identifies the different records: ");
    line_length = int(input("Please enter the length of the line: "));

    return by_recordID_and_line_length_content_process(content, line_length, record_identifier);
