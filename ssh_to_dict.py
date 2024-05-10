import sys
def ssh_to_dict(SSH_log):
    log_dict = {}
    try:
        log= SSH_log.split(': ')
        data_list = log[0].split()
        log_dict['month'] = data_list[0]
        log_dict['day'] = data_list[1]
        log_dict['time'] = data_list[2]
        log_dict['username'] = data_list[3]
        log_dict['pid'] = data_list[4]
        if(len(log)>2):
            log_dict['description'] = log[1] + log[2]
        else:
            log_dict['description'] = log[1]
    except Exception:
        log_dict['description'] = "incorrect log format"
    return log_dict
def file_to_dict_stream(file_name):
    dict_list = []
    with open(file_name, 'r') as f:
        dict_list = [ssh_to_dict(line) for line in f]
    f.close()
    return dict_list
if __name__ == "__main__":
    log_file = sys.argv[1]
    log_dict = file_to_dict_stream(log_file)
    print(log_dict)
    