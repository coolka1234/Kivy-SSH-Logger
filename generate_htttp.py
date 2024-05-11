from faker import Faker
import random
from datetime import datetime
from pytz import timezone, all_timezones
fake = Faker()

methods = ["GET", "POST", "PUT", "DELETE"]
resources = ["/index.html", "/about.html", "/contact.html", "/products.html", "/login.html"]
status_codes = ["200", "404", "500", "301"]

with open("http_logs.txt", "w") as file:
    for _ in range(100):
        dt = fake.date_time_this_year()
        tz = timezone(random.choice(all_timezones))
        dt = tz.localize(dt)
        log = f'{fake.ipv4()} - - [{dt.strftime("%d/%b/%Y:%H:%M:%S %z")}] "{random.choice(methods)} {random.choice(resources)} HTTP/1.0" {random.choice(status_codes)} {random.randint(1000,5000)}\n'
        file.write(log)