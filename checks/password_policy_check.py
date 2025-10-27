import subprocess


def check_password_policy(baseline):
    results = []
    try:
        output = subprocess.check_output(
            ["sudo", "grep", "PASS", "/etc/login.defs"]).decode()
        if f"PASS_MIN_LEN\t{baseline['min_length']}" in output:
            results.append(
                {"check": f"Min length = {baseline['min_length']}", "status": "pass"})
        else:
            results.append({"check": "Password min length", "status": "fail"})
    except Exception as e:
        results.append({"check": "Password policy check",
                       "status": "fail", "reason": str(e)})
    return results
