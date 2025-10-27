# this module uses the system command 'ufw' to check the firewall status against a given baseline.

import subprocess


def check_firewall(baseline):
    results = []
    try:
        output = subprocess.check_output(
            ["sudo", "ufw", "status"], stderr=subprocess.STDOUT).decode()
        if "Status: active" in output:
            status = True
        else:
            status = False
        if status == baseline.get("required", True):
            results.append({"check": "Firewall enabled", "status": "pass"})
        else:
            results.append({"check": "Firewall enabled", "status": "fail"})
    except subprocess.CalledProcessError as e:
        results.append({"check": "Firewall check",
                       "status": "fail", "reason": str(e)})
    return results
