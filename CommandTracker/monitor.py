import time
import psutil

def monitor_resources(pid, cpu_usage, memory_usage):
    try:
        p = psutil.Process(pid)
        while p.is_running():
            cpu_usage.append(p.cpu_percent(interval=0.1))
            memory_usage.append(p.memory_info().rss / 1024 ** 2)  # Convert to MB
            time.sleep(0.5)
    except psutil.NoSuchProcess:
        pass

