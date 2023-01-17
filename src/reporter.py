import json
import os
import time

class Reporter:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), 'out')
        report_name = f'report_{time.time()}.json'
        if not os.path.exists(path=self.path):
            os.makedirs(self.path)
        self.path = os.path.join(self.path, report_name)
        if not os.path.exists(path=self.path):
            with open(self.path, 'w') as f:
                f.write(json.dumps([], indent=4))

    def log_report(self, save: object):
        f = open(self.path, 'r')
        reports: list = json.load(f)
        reports.append(save)
        with open(self.path, 'w') as f:
            f.write(json.dumps(reports, indent=4))

    @staticmethod
    def print_json(obj: dict):
        print(json.dumps(obj, indent=4))