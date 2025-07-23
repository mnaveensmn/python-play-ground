import csv
from datetime import datetime,timezone

athena = 'csv/athena.csv'
splunk = 'csv/processed_splunk.csv'
format_string = "%Y-%m-%dT%H:%M:%S"

class BadgeScanInfo:
    def __init__(self,badge_id,timestamp):
        self.badge_id = badge_id
        self.timestamp = timestamp

    def __str__(self):
        return f"BadgeScanInfo(Badge ID: {self.badge_id}, Timestamp: {self.timestamp})"

def read_athena_csv():
    athena_badge_scans = []
    try:
        with open(athena, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            next(csv_reader, None)
            for row in csv_reader:
                parts = row[1].split('.')
                # seconds_part = parts[0]
                # microseconds_and_z_part = parts[1]
                # if len(microseconds_and_z_part)>=7:
                #     microseconds_truncated = microseconds_and_z_part[:6]
                # else:
                #     microseconds_truncated = microseconds_and_z_part.replace("Z", "")
                cleaned_date_string = f"{parts[0]}"
                dt_object = datetime.strptime(cleaned_date_string, format_string)
                dt_object_utc = dt_object.replace(tzinfo=timezone.utc)
                athena_badge_scans.append(BadgeScanInfo(row[0],dt_object_utc))
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

    return athena_badge_scans

def read_splunk_csv():
    splunk_badge_scan = []
    try:
        with open(splunk, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            #next(csv_reader, None)
            for row in csv_reader:
                if '.' in row[1]:
                    data_info = row[1].split('.')
                else:
                    data_info = row[1].split('+')
                transformed_date_string = f"{data_info[0]}"
                dt_object = datetime.strptime(transformed_date_string, format_string)
                dt_object_utc = dt_object.replace(tzinfo=timezone.utc)
                splunk_badge_scan.append(BadgeScanInfo(row[0], dt_object_utc))
    except Exception as e:
        print(f"An error occurred: {e}")

    return splunk_badge_scan

athena_badge_scans = read_athena_csv()
athena_badge_set = set([i.badge_id for i in athena_badge_scans])
print('Athena_badge_set')
print(athena_badge_set)

splunk_badge_scans = read_splunk_csv()
splunk_badge_set =set([i.badge_id for i in splunk_badge_scans])
print('Splunk_badge_set')
print(splunk_badge_set)


print('Invalid_badge_list')
invalid_badge_list = [badge_id for badge_id in splunk_badge_set if badge_id not in athena_badge_set ]
for i in set(invalid_badge_list):
    print(i)
#
# print(set([i.badge_id for i in splunk_badge_scans]))
#
# for splunk_badge_scan in splunk_badge_scans:
#     for athena_badge_scan in athena_badge_scans:
#         if splunk_badge_scan.badge_id == athena_badge_scan.badge_id and splunk_badge_scan.timestamp > athena_badge_scan.timestamp:
#             print(f"{splunk_badge_scan.badge_id} => splunk: {splunk_badge_scan.timestamp} > athena: {athena_badge_scan.timestamp}")
#
#
#
