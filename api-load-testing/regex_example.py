import re

text = ""
match = re.search("----(\d{1,20})----|badge=(\d+)", text)

if match:
    extracted_value = next((group for group in match.groups() if group is not None), None)
    print(extracted_value)
else:
    print("Number not found")