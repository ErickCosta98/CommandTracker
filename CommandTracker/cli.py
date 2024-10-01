import argparse
from CommandTracker.core import run_command
from CommandTracker.history import get_history, getAll_history


def main():
    parser = argparse.ArgumentParser(
        description="Tool to execute and monitor resource usage of commands.")
    subparsers = parser.add_subparsers(dest="command")

    # Subcommand 'monitor'
    monitor_parser = subparsers.add_parser(
        "monitor", help="Monitor CPU and memory usage of a command")
    monitor_parser.add_argument('exec_command', nargs=argparse.REMAINDER,
                                help='The command to monitor (e.g., "php artisan ...")')
    monitor_parser.add_argument('-g', '--graph', action='store_true',
                                help='Generate a graph of CPU and memory usage over time')

    # Subcommand 'history'
    history_parser = subparsers.add_parser(
        "history", help="Show the history of commands")
    history_parser.add_argument('exec_command', nargs=argparse.REMAINDER,
                                help='The command to display history for (optional)')

    args = parser.parse_args()

    if args.command == "monitor":
        run_command(args.exec_command, graph=args.graph)
    elif args.command == "history":
        if args.exec_command:
            get_history(args.exec_command)
        else:
            getAll_history()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
