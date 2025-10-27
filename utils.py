import platform
import socket
from datetime import datetime
import os


def get_system_metadata():
    """Collects and returns system metadata for reporting."""
    metadata = {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "user": os.getenv("USER", "unknown"),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    return metadata
