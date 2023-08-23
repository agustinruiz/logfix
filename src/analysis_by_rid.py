import re ;

def by_record_identifier_content_process(content, record_identifier):
    pattern = r'\n(?!' + re.escape(record_identifier) + r')';
    return re.sub(pattern, '', content);

def by_record_identifier(content):
    record_identifier = input("Please enter the initial text that identifies the different records: ");

    return by_record_identifier_content_process(content, record_identifier);