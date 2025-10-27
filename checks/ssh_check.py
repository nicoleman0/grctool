import re

# This function reads /etc/ssh/sshd_config and verifies that each key/value matches the baseline.


def check_ssh_config(baseline):
    results = []
    try:
        with open("etc/ssh/sshd_config", "r") as f:
            config = f.read()
    except FileNotFoundError:
        return [{"check": "SSH config file exists", "status": "fail", "reason": "File not found"}]

    for key, expected_value in baseline.items():
        pattern = rf"^{key}\s+{expected_value}$"
        if re.search(pattern, config, re.MULTILINE):
            results.append(
                {"check": f"{key} = {expected_value}", "status": "pass"})
        else:
            results.append(
                {"check": f"{key} = {expected_value}", "status": "fail"})
    return results
