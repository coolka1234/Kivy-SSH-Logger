import re
import ssh_to_dict
import sys
def get_ipv4s_from_log(log_dict):
    ipv4_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    ipv4_addresses = re.findall(ipv4_pattern, log_dict['description'])
    return ipv4_addresses
if __name__ == "__main__":
    print(get_ipv4s_from_log(ssh_to_dict.ssh_to_dict(sys.argv[1])))