from analysis_by_rid import by_record_identifier;
from analysis_by_rid_llen import by_recordID_and_line_length;

def analysis_menu_selection(analysis_options):
    user_input = '';

    input_message = "Pick an option:\n";

    for key, (descriptor, _) in analysis_options.items():
        input_message += f'{key}) {descriptor}\n';

    input_message += 'Your choice: ';

    while user_input not in analysis_options.keys():
        user_input = input(input_message);

    print('You picked: ' + analysis_options[user_input][0]);
    return analysis_options[user_input];

def analysis(content):
    analysis_options = {
        '1': ('Only by record identifier', by_record_identifier),
        '2': ('By record identifier and line length', by_recordID_and_line_length),
    }

    analysis_choice = analysis_menu_selection(analysis_options);

    return analysis_choice[1](content);
