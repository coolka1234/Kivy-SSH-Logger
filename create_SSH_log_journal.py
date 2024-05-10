import os
import sys
import SSHLogEntry
import SSHLogJournal
def create_journal(fileName):
    journal = SSHLogJournal.SSHLogJournal()
    with open(fileName, 'r') as f:
        logs = f.readlines()
    f.close()
    for log in logs:
        journal.append(log)
    return journal