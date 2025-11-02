import subprocess
import os
import pwd


def run_command(cmd):
    """Utility to run shell commands and return stdout."""
    try:
        result = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return e.output.strip()


def check_firewall_enabled():
    output = run_command("ufw status | grep -i active || echo inactive")
    status = "pass" if "active" in output.lower() else "fail"
    return {"check": "Firewall Enabled", "status": status, "weight": 3}


def check_ssh_root_login_disabled():
    output = run_command(
        "grep -i '^PermitRootLogin' /etc/ssh/sshd_config || echo 'not found'")
    status = "pass" if "no" in output.lower() else "fail"
    return {"check": "SSH Root Login Disabled", "status": status}


def check_auditd_running():
    output = run_command("systemctl is-active auditd || echo inactive")
    status = "pass" if "active" in output.lower() else "fail"
    return {"check": "Auditd Service Running", "status": status}


def check_passwd_permissions():
    perms = oct(os.stat("/etc/passwd").st_mode)[-3:]
    status = "pass" if perms == "644" else "fail"
    return {"check": "/etc/passwd Permissions", "status": status, "weight": 2}


def check_shadow_permissions():
    perms = oct(os.stat("/etc/shadow").st_mode)[-3:]
    status = "pass" if perms == "640" else "fail"
    return {"check": "/etc/shadow Permissions", "status": status}


def check_root_accounts():
    root_users = [u.pw_name for u in pwd.getpwall() if u.pw_uid == 0]
    status = "pass" if root_users == ["root"] else "fail"
    return {"check": "Only Root Has UID 0", "status": status}


def check_system_updates():
    result = run_command(
        "apt list --upgradable 2>/dev/null | grep -v 'Listing...' | wc -l")
    try:
        updates = int(result)
    except ValueError:
        updates = 0
    status = "pass" if updates == 0 else "fail"
    return {"check": "System Packages Up To Date", "status": status}


def check_system_config(baseline=None):
    """Run all system configuration checks."""
    results = []
    results.append(check_firewall_enabled())
    results.append(check_ssh_root_login_disabled())
    results.append(check_auditd_running())
    results.append(check_passwd_permissions())
    results.append(check_shadow_permissions())
    results.append(check_root_accounts())
    results.append(check_system_updates())
    return results
