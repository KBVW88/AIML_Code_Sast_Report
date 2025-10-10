import json
from json2html import json2html

with open("snyk_report.json") as f:
    data = json.load(f)

with open("snyk_report.html", "w") as f:
    f.write(json2html.convert(json=data))