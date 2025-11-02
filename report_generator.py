import jinja2
import datetime
import os


def calculate_compliance_score(results):
    """Calculate weighted compliance score."""
    total_weight = 0
    achieved_weight = 0

    for r in results:
        weight = r.get("weight", 1)
        total_weight += weight
        if r["status"].lower() == "pass":
            achieved_weight += weight

    if total_weight == 0:
        return 0
    return round((achieved_weight / total_weight) * 100, 2)


def generate_report(results, metadata):
    """Render compliance report to HTML."""
    score = calculate_compliance_score(results)
    metadata["compliance_score"] = score

    # ✅ Use correct template path (portable and safe)
    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template("report_template.html")

    output = template.render(results=results, metadata=metadata)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = os.path.join(os.path.dirname(__file__), "reports")
    os.makedirs(report_dir, exist_ok=True)

    filename = os.path.join(report_dir, f"compliance_report_{timestamp}.html")
    with open(filename, "w") as f:
        f.write(output)

    print(f"[+] Compliance report generated: {filename}")
    print(f"[+] Overall compliance score: {score}%")
