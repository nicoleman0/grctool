# Compliance checker code

This tool helps automate the process of compliance checking.

It currently supports firewall, password policy, and ssh checking capabilities.

## How to set up

`baseline.yml` is where you store the baseline configurations that the tool checks against.

The checks are individually located within the `/checks` directory:

- `firewall_check.py`
- `password_policy_check.py`
- `ssh_check.py`

The report template is located at `/templates/report_template.html`.

If you'd like the tool to include more metadata when it checks your system, you can add more fields by accessing the system metadata function at `/utils.py`.

It currently supports:
- hostname
- os/os_version
- user
- timestamp
