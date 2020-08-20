import os
import datetime
import reports
from run import catalog_data
import emails


def get_info(description_dir):
        names = []
        weights = []
        for file in os.listdir(description_dir):
                full_path = os.path.join(description_dir, file)
                with open(full_path) as f:
                        lines = f.readlines()
                        name = lines[0].strip('\n')
                        weight = lines[1].strip('\n')
                        names.append('name: ' + name)
                        weights.append('weight: ' + weight)
        result_str = ""
        for i in range(len(names)):
                result_str += names[i] + '<br />' + weights[i] + '<br />' + '<br />'
        return result_str


if __name__ == "__main__":
        USER = os.getenv('USER')
        description_dir = "/home/{}/supplier-data/descriptions".format(USER)
        info = get_info(description_dir)
        cur_date = datetime.date.today().strftime("%m/%d/%y")
        title = "Processed Update on {}".format(cur_date)
        reports.generate_report('/tmp/processed.pdf', title, info)
        message = emails.generate_message('automation@example.com', '{}@example.com'.format(USER), 'Upload Completed - Online Fruit Store', 'All fruits are uploaded to our website sucessfully. A detailed list is attached to this email', '/tmp/processed.pdf')
        emails.send_message(message)
