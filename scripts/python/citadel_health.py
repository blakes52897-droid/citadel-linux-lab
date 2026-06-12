import shutil
import subprocess
from pathlib import Path
from datetime import datetime


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"


def get_memory():
    meminfo = Path("/proc/meminfo").read_text()
    total = available = None

    for line in meminfo.splitlines():
        if line.startswith("MemTotal:"):
            total = int(line.split()[1])
        elif line.startswith("MemAvailable:"):
            available = int(line.split()[1])

    used = total - available
    percent_used = round((used / total) * 100, 1)

    return total // 1024, used // 1024, available // 1024, percent_used


def get_disk():
    total, used, free = shutil.disk_usage("/")
    percent_used = round((used / total) * 100, 1)

    return total // (2**30), used // (2**30), free // (2**30), percent_used


def get_service_status(service):
    output = run_command(f"systemctl is-active {service}")
    return output if output else "unknown"


def build_report():
    disk_total, disk_used, disk_free, disk_percent = get_disk()
    mem_total, mem_used, mem_free, mem_percent = get_memory()

    uptime = run_command("uptime -p")
    cpu_load = run_command("uptime | awk -F'load average:' '{ print $2 }'")
    ufw_status = run_command("sudo ufw status | head -n 1")
    fail2ban_status = get_service_status("fail2ban")
    apache_status = get_service_status("apache2")
    cloudflared_status = get_service_status("cloudflared")

    report = f"""================================
      CITADEL HEALTH REPORT
================================

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Uptime: {uptime}
CPU Load Average:{cpu_load}

Disk: {disk_used}GB used / {disk_total}GB total ({disk_percent}%)
Free Disk: {disk_free}GB

Memory: {mem_used}MB used / {mem_total}MB total ({mem_percent}%)
Free Memory: {mem_free}MB

Services:
UFW: {ufw_status}
Fail2Ban: {fail2ban_status}
Apache: {apache_status}
Cloudflared: {cloudflared_status}

Citadel status: ONLINE
"""
    return report


def save_report(report):
    reports_dir = Path.home() / "python" / "health_reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    report_file = reports_dir / f"{timestamp}_report.txt"

    report_file.write_text(report)

    return report_file


def main():
    report = build_report()
    print(report)

    report_file = save_report(report)
    print(f"Report saved to: {report_file}")


if __name__ == "__main__":
    main()
