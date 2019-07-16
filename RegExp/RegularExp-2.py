import re
import json

filereader = open("emails", mode="r", encoding="utf-8")
text = filereader.read()
filereader.close()

template_for_found_names = r"[A-Z][a-z]+\s[A-Z][a-z]+"
template_for_found_emails = r"[\w\-\.]+\@[\w\.-]+"

names = re.findall(template_for_found_names, text)
emails = re.findall(template_for_found_emails, text)

result = {}
for x in range(0, len(names)):
    result[names[x]] = emails[x]

for user in result:
    print(user + ":\n\t" + result[user])

filewriter = open("found_email_addresses.json", mode="w", encoding="utf-8")
json.dump(result, filewriter)
filewriter.close()


# Except some emails
print(len(emails))
template_for_found_emails = r"[\w\-\.]+\@(?!president\.gov)[\w\.-]+"
emails = re.findall(template_for_found_emails, text)
print(len(emails))
