| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/commandtracker.svg)](https://pypi.org/project/CommandTracker/) |
# CommandTracker

CommandTracker is a Python tool designed to execute a command and monitor its resource usage in real time. It tracks CPU and memory consumption, providing valuable performance metrics like average CPU load and peak memory usage. This tool is ideal for developers and system administrators looking to optimize the performance of commands or processes.

## Features

- Monitor CPU and memory usage of any command.
- Real-time resource tracking during command execution.
- Provides performance statistics, including average CPU usage and peak memory consumption.

## Installation

You can install CommandTracker via pip:

```bash
pip install commandtracker
```

## Usage

Once installed, you can use `ctracker` to monitor a command’s resource usage:

```bash
ctracker monitor <command>
```

For example:

```bash
ctracker monitor php artisan calcular:liquidaciones --fecha=2024-01-01
```

### Example Output:

```bash
Iniciando proceso con PID 12345...

Output of your command...

Proceso terminado.
Tiempo total de ejecución: 10.25 segundos.

Estadísticas de uso de recursos:
Promedio de uso de CPU: 35.67%
Máximo uso de memoria: 120.45 MB
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
- Historical resource tracking.
- Graph generation for resource usage.
- Alert system for resource thresholds.

