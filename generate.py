# Draft. Not final yet.

stms = []
names = []

import csv
with open('raw_data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if row[0] == 'STM ID':
            continue
        
        stms.append(row[0])
        names.append(row[8])

        with open(row[0] + ".html", "w") as stmfile:
            stmfile.write(f"""<!DOCTYPE html>
            <html>
            <head><title>{row[0]}: STM Registry</title></head>
            <body>
            <h1>{row[0]}: {row[8]}</h1>

            <h2>Authors</h2>
            <pre>
            {row[2]}
            </pre>

            <h2>Venue and Year</h2>
            <pre>
            {row[5]}, {row[3]}
            </pre>

            <h2>Original Work</h2>
            <pre>
            <a href='{row[6]}'>{row[1]}</a>
            </pre>

            <h2>Defense Modality</h2>
            <pre>
            {row[9]}
            </pre>

            <h2>Core Method(s)</h2>
            <pre>
            {row[10]}
            </pre>

            <h2>Input-Output Mapping</h2>
            <pre>
            {row[11].replace(">", "&gt;")}
            </pre>

            <h2>Targeted Contracts</h2>
            <pre>
            {row[12]}
            </pre>

            <h2>Threat Model</h2>
            <i>Vulnerable contract, malicious contract, or both</i>
            <pre>
            {row[13]}
            </pre>

            <h2>Targeted Vulnerabilities</h2>
            <pre>
            {row[14]}
            </pre>


            </body>
            </html>""")


header = """
<!DOCTYPE html>
<html>
    <head><title>STM Registry</title></head>
    <body>
        <h1>STM Registry</h1>
"""

body = "<ul>\n"

for i in range(len(stms)):
    body += f"""<li><a href="{stms[i]}.html">{stms[i]}: {names[i]}</a></li>\n"""

body += "</ul>\n"

footer = """
    </body>
</html>
"""

total = header + body + footer

with open("index.html", "w") as indexfile:
    indexfile.write(total)