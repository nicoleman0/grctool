import yaml
from checks.ssh_check import check_ssh_config
from checks.password_policy_check import check_password_policy
from checks.firewall_check import check_firewall
from report_generator import generate_report
from utils import get_system_metadata


def load_baseline():
    with open("policies/baseline.yml") as f:
        return yaml.safe_load(f)


def main():
    baseline = load_baseline()
    all_results = []

    print("[*] Collecting system metadata...")
    metadata = get_system_metadata()

    print("[*] Running SSH checks...")
    all_results.extend(check_ssh_config(baseline["ssh"]))

    print("[*] Running password policy checks...")
    all_results.extend(check_password_policy(baseline["password_policy"]))

    print("[*] Running firewall checks...")
    all_results.extend(check_firewall(baseline["firewall"]))

    generate_report(all_results, metadata)


if __name__ == "__main__":
    main()
