import subprocess
import time
import psutil
import argparse
import threading

def monitor_resources(pid, cpu_usage, memory_usage):
    try:
        p = psutil.Process(pid)
        while p.is_running():
            cpu_usage.append(p.cpu_percent(interval=0.1))
            memory_usage.append(p.memory_info().rss / 1024 ** 2)
            time.sleep(0.5)
    except psutil.NoSuchProcess:
        pass

def run_command(command):
    start_time = time.time()
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pid = process.pid
    print(f"Iniciando proceso con PID {pid}...")

    cpu_usage = []
    memory_usage = []

    monitor_thread = threading.Thread(target=monitor_resources, args=(pid, cpu_usage, memory_usage))
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
        print(f"Error en la ejecución: {str(e)}")

    monitor_thread.join()

    end_time = time.time()
    execution_time = end_time - start_time
    print("\nProceso terminado.")
    print(f"Tiempo total de ejecución: {execution_time:.2f} segundos.")

    if cpu_usage:
        print("\nEstadísticas de uso de recursos:")
        print(f"Promedio de uso de CPU: {sum(cpu_usage)/len(cpu_usage):.2f}%")
        print(f"Máximo uso de memoria: {max(memory_usage):.2f} MB")


def main():
    parser = argparse.ArgumentParser(description="Tool to execute and monitor resource usage of commands.")
    subparsers = parser.add_subparsers(dest="command")

    # Subcomando 'monitor'
    monitor_parser = subparsers.add_parser("monitor", help="Monitor CPU and memory usage of a command")
    monitor_parser.add_argument('exec_command', nargs=argparse.REMAINDER, help='The command to monitor (e.g., "php artisan ...")')

    args = parser.parse_args()

    if args.command == "monitor":
        run_command(args.exec_command)
    else:
        parser.print_help()

