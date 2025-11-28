import subprocess
import time



def log(prefix):
    def func(msg):
        print(f"[{prefix}] {msg}")
    return func

error = log("ERROR")


def exec(cmd):
    try:
        subprocess.run(cmd, shell=True, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        error(e)


def return_cmd(app_name: str):
    app_name = app_name.lower()
    match app_name:
        case 'zoom':
            return "osascript -e 'tell application id \"us.zoom.xos\" to quit'"
        case _:
            return f'osascript -e \'tell application "{app_name}" to quit\''


def quit_app(app_name):
    print(f"Завершаю: {app_name}")
    exec(return_cmd(app_name))



def main():
    APPS = [
        "Google Chrome",
        "Visual Studio Code",
        "Tailscale",
        "OrbStack",
        "Notes",
        "Obsidian",
        "Telegram",
        "Zoom",
    ]

    for app in APPS:
        quit_app(app)

    print("\nГотово! Все процессы завершены.")

if __name__ == "__main__":
    main()
