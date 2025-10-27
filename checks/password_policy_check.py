# This module checks the system's password policy (in /etc/login.defs) against a given baseline.

def get_value_from_login_defs(key):
    with open("/etc/login.defs", "r") as f:
        for line in f:
            if line.strip().startswith(key):
                parts = line.split()
                if len(parts) >= 2:
                    return parts[1]
    return None


def check_password_policy(baseline):
    min_len = get_value_from_login_defs("PASS_MIN_LEN")
    results = []
    if min_len and int(min_len) >= baseline["min_length"]:
        results.append(
            {"check": f"Min length ≥ {baseline['min_length']}", "status": "pass"})
    else:
        results.append(
            {"check": f"Min length ≥ {baseline['min_length']}", "status": "fail"})
    return results
