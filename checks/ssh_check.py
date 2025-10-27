import re
import os


def check_ssh_config(baseline):
    results = []

    ssh_path = "/etc/ssh/sshd_config"

    if not os.path.exists(ssh_path):
        results.append({
            "check": "SSH Configuration",
            "status": "not installed",
            "reason": f"{ssh_path} not found"
        })
        return results

    try:
        with open(ssh_path, "r") as f:
            config = f.read()
    except FileNotFoundError:
        results.append({
            "check": "SSH config file exists",
            "status": "fail",
            "reason": "File not found"
        })
        return results

    for key, expected_value in baseline.items():
        pattern = rf"^{key}\s+{expected_value}$"
        if re.search(pattern, config, re.MULTILINE):
            results.append({
                "check": f"{key} = {expected_value}",
                "status": "pass"
            })
        else:
            results.append({
                "check": f"{key} = {expected_value}",
                "status": "fail"
            })

    return results
