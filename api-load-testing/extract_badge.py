
import re
from fileinput import filename

import csv
from traceback import print_tb

splunk_csv_file = 'csv/splunk.csv'
processed_splunk_csv_file = 'csv/processed_splunk.csv'

athena_badge = 'found_badge.csv'

def extract_from_splunk_log():
    badges=[]
    try:
        with open(splunk_csv_file, 'r') as file:
            while True:
                line = file.readline()
                if not line: # End of file
                    break
                line = line.strip()
                badge_info=line.split("###")
                badge = badge_info[0]
                datainfo = badge_info[1]
                match = re.search(r"----(\d+)----|badge=(\d+)|(.*14733)", badge)
                if match:
                    extracted_number = next((group for group in match.groups() if group is not None), None)
                    badge_data = [extracted_number,datainfo]
                    badges.append(badge_data)
                    print(badge_data)
    except Exception as e:
        print(f"An error occurred: {e}")
    return badges

def write_data_to_csv(filename, data):
    try:
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
            print(f"Data successfully written to {filename}")
    except IOError as e:
        print(f"Error: Could not write to file {filename}. Reason: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def extract_from_athena_result():
    badges = []
    try:
        with open(athena_badge, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile) # Creates a reader object
            # Optional: Skip header row if your CSV has one
            next(csv_reader, None)

            for row in csv_reader:
                badges.append(row[0])

    except Exception as e:
        print(f"An error occurred: {e}")

    return badges

badges = extract_from_splunk_log()
write_data_to_csv(processed_splunk_csv_file, badges)
for badge in badges:
    print(f"'{badge[0]}',")
# athena=extract_from_athena_result()
# print(athena)
#splunk=extract_from_splunk_log()
#print(splunk)

# print("invalid badge list")
# for badge in set(splunk):
#     if badge not in set(athena):
#         print(badge)

# splunk_filter_terms = []
# for number in athena:
#     splunk_filter_terms.append(f'queryParam="*{number}*"')
#
# # Join them with OR
# query_param_filter = " OR ".join(splunk_filter_terms)
#
# print(query_param_filter)
