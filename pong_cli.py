import sys
import httpx

def send_command(url: str, command: str, param: int = None):
    client = httpx.Client()
    if command == "start":
        response = client.post(f"{url}/control/start", json={"pong_time": param})
    elif command == "pause":
        response = client.post(f"{url}/control/pause")
    elif command == "resume":
        response = client.post(f"{url}/control/resume")
    elif command == "stop":
        response = client.post(f"{url}/control/stop")
    else:
        print(f"Unknown command: {command}")
        return
    print(response.json())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pong_cli.py <command> <param>")
        sys.exit(1)

    command = sys.argv[1]
    param = int(sys.argv[2]) if len(sys.argv) > 2 else None

    server1_url = "http://localhost:8000"
    server2_url = "http://localhost:8001"

    send_command(server1_url, command, param)
    send_command(server2_url, command, param)
