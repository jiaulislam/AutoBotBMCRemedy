from typing import Tuple
import psutil
import sys

BYTES = 1000000000

def get_platform() -> str:
    return sys.platform

def get_python_version() -> str:
    return sys.winver

def get_memory_info() -> Tuple[str]:
    memory = psutil.virtual_memory()
    total = memory[0]/BYTES
    available = memory[1]/BYTES
    percent = memory[2]
    used = memory[3]/BYTES
    free = memory[4]/BYTES
    return (f"{total:.2f} GB", f"{available:.2f} GB", f"{percent}%", f"{used:.2f} GB", f"{free:.2f} GB")
