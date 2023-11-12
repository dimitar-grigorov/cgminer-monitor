# CGMiner Monitor

CGMiner Monitor is a Python-based utility that allows you to monitor the performance of your CGMiner. It provides real-time insights into your CGMiner's performance and can be configured to output in different formats.

## Prerequisites

- Python 3
- pip (Python package installer)

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/dimitar-grigorov/cgminer-monitor.git
    ```

2. Navigate into the project directory:

    ```bash
    cd cgminer-monitor
    ```

3. Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the CGMiner Monitor, use the following command:

```bash
python cgminer-monitor.py -a <host> -p <port> -m <mode> -r <min-rate>
```

**Where:**

`<host>`: The host address of the CGMiner.  
`<port>`: The port number on which CGMiner is running. Default is 4028.  
`<mode>`: The output format. Use either Default or PRTG. Default is Default.  
`<min-rate>`: The minimum rate. Use only with `--mode=PRTG`. Default is 0.  

## License

This project is licensed under the [MIT License](https://github.com/dimitar-grigorov/cgminer-monitor/blob/master/LICENSE.md) - see the LICENSE.md file for details.
