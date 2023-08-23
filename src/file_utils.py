from io import open;

def open_input_file(filename):
    try:
        with open(filename,'r') as file:
            return file.read();
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.");
    except Exception as e:
        print(f"An error ocurred: {e}.");
    return None

def save_output_file(filename, content):
    try:
        with open(filename,'w') as file:
            content = file.write(content);
    except Exception as e:
        print(f"An error ocurred: {e}.");