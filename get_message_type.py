import re
def get_messege_type(log):
    success_pattern = r'check pass'
    fail_pattern = r'authentication failure|authentication failures'
    disconnect_pattern = r'disconnect|Connection closed'
    failed_password_pattern = r'Failed password|failed password'
    invalid_user_pattern = r'invalid user|Invalid user'
    break_in_attempt_pattern = r'POSSIBLE BREAK-IN ATTEMPT!'
    if re.search(success_pattern, log['description']):
        return 'success_login'
    elif re.search(fail_pattern, log['description']):
        return 'failed_login'
    elif re.search(disconnect_pattern, log['description']):
        return 'disconnect'
    elif re.search(failed_password_pattern, log['description']):
        return 'failed password'
    elif re.search(invalid_user_pattern, log['description']):
        return 'invalid user'
    elif re.search(break_in_attempt_pattern, log['description']):
        return 'break in attempt'
    else:
        return 'other'
