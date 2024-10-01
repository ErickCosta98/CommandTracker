import argparse
from CommandTracker.core import run_command

def main():
    parser = argparse.ArgumentParser(description="Tool to execute and monitor resource usage of commands.")
    subparsers = parser.add_subparsers(dest="command")
    # Subcommand 'monitor'
    monitor_parser = subparsers.add_parser("monitor", help="Monitor CPU and memory usage of a command")
    monitor_parser.add_argument('exec_command', nargs=argparse.REMAINDER, help='The command to monitor (e.g., "php artisan ...")')
    monitor_parser.add_argument('-g', '--graph', action='store_true', help='Generate a graph of CPU and memory usage over time')

    args = parser.parse_args()

    if args.command == "monitor":
        run_command(args.exec_command,graph=args.graph)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
