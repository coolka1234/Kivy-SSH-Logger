import re
import sys

def string_to_dict(log):
    pattern = r'(?P<month>\w{3}) (?P<day>\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) (?P<hostname>\w+) (?P<process>\w+)\[(?P<pid>\d+)\]: (?P<description>.*)'
    match = re.match(pattern, log)
    if match:
        return match.groupdict()
    else:
        return None
def create_dict_list(logs):
    dict_list = []
    for log in logs:
        log_dict = string_to_dict(log)
        if log_dict:
            dict_list.append(log_dict)
    return dict_list
def create_list_from_file(file_name):
    with open(file_name, 'r') as f:
        logs = f.readlines()
    f.close()
    return create_dict_list(logs)
if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        logs = f.readlines()
    f.close()
    log_dict = create_dict_list(logs)
    