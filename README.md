[![PyPI Latest Release](https://img.shields.io/pypi/v/commandtracker.svg)](https://pypi.org/project/CommandTracker/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/CommandTracker)](https://pypi.org/project/CommandTracker/)
 [![GitHub Release Date](https://img.shields.io/github/release-date/ErickCosta98/CommandTracker)](https://github.com/ErickCosta98/CommandTracker/releases) [![GitHub License](https://img.shields.io/github/license/ErickCosta98/CommandTracker)](https://github.com/ErickCosta98/CommandTracker/blob/main/LICENSE)

# CommandTracker

CommandTracker is a Python tool designed to execute a command and monitor its resource usage in real time. It tracks CPU and memory consumption, providing valuable performance metrics like average CPU load and peak memory usage. This tool is ideal for developers and system administrators looking to optimize the performance of commands or processes.

## Features

- Monitor CPU and memory usage of any command.
- Real-time resource tracking during command execution.
- Provides performance statistics, including average CPU usage and peak memory consumption.

## Installation

You can install CommandTracker via pip:

```bash
pip install CommandTracker
```

## Usage

Once installed, you can use `ctracker` to monitor a command’s resource usage:

```bash
ctracker monitor <command>
```

For example:

```bash
ctracker monitor php artisan calc --date=2024-01-01
```

### Example Output:

```bash
Starting process with PID 12345...

Output of your command...

Process finished.
Total execution time: 10.25 seconds.

Resource usage statistics:
Average CPU usage: 35.67%
Maximum memory usage: 120.45 MB
```

## Requirements

- Python 3.6+
- psutil library

## Contributing

Feel free to contribute by submitting issues or pull requests. More features and optimizations will be added in future versions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Future Enhancements

Planned features for future releases include:
• Generation of graphs to visualize resource usage.  
• Historical logging of command execution.  
• Automatic alerts if a process exceeds certain CPU or memory thresholds.  
• Stress testing to simulate intensive workloads.


