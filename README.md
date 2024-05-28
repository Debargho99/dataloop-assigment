# Pong Game

This project sets up two FastAPI servers that play a ping-pong game with each other. The game can be controlled using a CLI tool.

## Project Structure

pong_game/
├── server1/
│ ├── main.py
├── server2/
│ ├── main.py
├── cli/
│ ├── pong_cli.py
├── requirements.txt
├── README.md
└── .gitignore


## Setup

1. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the servers:

    ```bash
    # In one terminal
    uvicorn server1.main:app --port 8000

    # In another terminal
    uvicorn server2.main:app --port 8001
    ```

3. Control the game using the CLI tool:

    ```
    # Start the game with a 1-second interval between pings
    python cli/pong_cli.py start 1000

    # Pause the game
    python cli/pong_cli.py pause

    # Resume the game
    python cli/pong_cli.py resume

    # Stop the game
    python cli/pong_cli.py stop
    ```
## Bash Script
```
#Make the Script Executable
chmod +x pong_cli.sh

./pong_cli.sh start 1000

./pong_cli.sh pause

./pong_cli.sh resume

./pong_cli.sh stop

```
## .gitignore

Add the `.gitignore` file to exclude unnecessary files from version control:

