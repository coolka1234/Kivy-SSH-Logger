# exapmle - 192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395
import re
class HTTPLogEntry():
    def __init__(self, log):
        self._raw_desc = log
        self._dict = self._parse_log(log)
        self.remote_host = self._dict['remote_host']
        self.date = self._dict['date']
        self.timezone = self._dict['timezone']
        self.status_code = self._dict['status_code']
        self.method = self._dict['method']
        self.resource = self._dict['resource']
        self.size = self._dict['size']
    def _parse_log(self, log):
        pattern = r'(?P<remote_host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(?P<date>\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} (?P<timezone>[-+]\d{4}))\] "(?P<method>\w+) (?P<resource>.*) HTTP/1.0" (?P<status_code>\d{3}) (?P<size>\d+)'
        match = re.match(pattern, log)
        if match:
            return match.groupdict()
        else:
            return None
    def get_messege_type(self):
        if self.status_code == "200":
            return "OK"
        elif self.status_code == "404":
            return "Not Found"
        elif self.status_code == "403":
            return "Forbidden"
        else:
            return "Other"
    def __str__(self):
        return f"{self.remote_host} {self.date} {self.timezone} {self.status_code} {self.method} {self.resource} {self.size}"
    def __repr__(self):
        return f"{self.remote_host} {self.date} {self.timezone} {self.status_code} {self.method} {self.resource} {self.size}"
if __name__ == "__main__":
    log=HTTPLogEntry('192.168.2.20 - - [28/Jul/2006:10:27:10 -0300] "GET /cgi-bin/try/ HTTP/1.0" 200 3395')
    print(str(log))