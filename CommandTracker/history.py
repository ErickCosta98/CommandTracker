# history for commands
import os
import datetime


def create_history(command, execute_time, cpu_usage, memory_usage):
    # get home path
    home = os.path.expanduser("~")
    log_path = home + "/command_history.log"
    # create log file  if not exist
    if not os.path.exists(log_path):
        open(log_path, "w").close()

    # create logs info

    execute_time_str = f"Total execution time: {execute_time:.2f} seconds."
    cpu_usage_str = ""
    memory_usage_str = ""
    # si la longitud de cpu_usage es mayor a 0, mostrar el promedio
    if len(cpu_usage) > 0:
        cpu_usage_str = f"Average CPU usage: {
            sum(cpu_usage)/len(cpu_usage):.2f}%"
    if len(memory_usage) > 0:
        memory_usage_str = f"Maximum memory usage: {max(memory_usage):.2f} MB"
    # open log file
    logs = open(log_path, "a")
    # date time yyyy-mm-dd hh:mm:ss
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # add logs to file
    logs.write(
        date_time + " " +
        " ".join(command) + " " + execute_time_str + " " +
        cpu_usage_str + " " + memory_usage_str + "\n"
    )
    logs.close()
# get all logs and print in console


def getAll_history():
    # get home path
    home = os.path.expanduser("~")
    log_path = home + "/command_history.log"
    # open log file
    logs = open(log_path, "r")
    print(logs.read())
    logs.close()
# get all logs of command and print in console


def get_history(command):
    # get home path
    home = os.path.expanduser("~")
    log_path = home + "/command_history.log"
    # open log file
    logs = open(log_path, "r")
    # find command in log file
    command_str = " ".join(command)
    for line in logs.read().split("\n"):
        # si el comando se encuentra en la linea imprimirla
        if line.find(command_str) > -1:
            print(line)
    logs.close()
