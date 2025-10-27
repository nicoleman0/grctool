from jinja2 import Environment, FileSystemLoader


def generate_report(results):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    html_content = template.render(results=results)
    with open("compliance_report.html", "w") as f:
        f.write(html_content)

    print("[+] Compliance report generated: compliance_report.html")
