#!/bin/bash

# Usage information
usage() {
    echo "Usage: $0 {start|pause|resume|stop} [pong_time_ms]"
    exit 1
}

# Check for at least one argument
if [ $# -lt 1 ]; then
    usage
fi

COMMAND=$1
PONG_TIME_MS=$2

# Define the CLI script location
CLI_SCRIPT="cli/pong_cli.py"

# Function to execute the CLI command
execute_cli_command() {
    local cmd=$1
    local param=$2

    if [ "$cmd" == "start" ]; then
        if [ -z "$param" ]; then
            echo "Error: pong_time_ms parameter is required for start command."
            usage
        fi
        python $CLI_SCRIPT $cmd $param
    else
        python $CLI_SCRIPT $cmd
    fi
}

# Execute the command based on user input
case $COMMAND in
    start)
        execute_cli_command start $PONG_TIME_MS
        ;;
    pause)
        execute_cli_command pause
        ;;
    resume)
        execute_cli_command resume
        ;;
    stop)
        execute_cli_command stop
        ;;
    *)
        usage
        ;;
esac
