import subprocess
import threading
import time
from CommandTracker.monitor import monitor_resources
from CommandTracker.graph import generate_graph
from CommandTracker.history import create_history


def run_command(command, graph=False):
    start_time = time.time()

    if isinstance(command, str):
        command = command.split()

    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pid = process.pid
    print(f"Starting process with PID {pid}...")

    cpu_usage = []
    memory_usage = []

    monitor_thread = threading.Thread(
        target=monitor_resources, args=(pid, cpu_usage, memory_usage))
    monitor_thread.start()

    try:
        while process.poll() is None:
            output = process.stdout.readline()
            if output:
                print(output.strip())
            error = process.stderr.readline()
            if error:
                print(f"ERROR: {error.strip()}")

        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.strip())
        if stderr:
            print(f"ERROR: {stderr.strip()}")
    except Exception as e:
        print(f"Execution error: {str(e)}")

    monitor_thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print("\nProcess finished.")
    print(f"Total execution time: {execution_time:.2f} seconds.")

    if cpu_usage:
        print("\nResource usage statistics:")
        print(f"Average CPU usage: {sum(cpu_usage)/len(cpu_usage):.2f}%")
        print(f"Maximum memory usage: {max(memory_usage):.2f} MB")
        if graph:
            generate_graph(cpu_usage, memory_usage, execution_time)

    create_history(command, execution_time, cpu_usage, memory_usage)
