import os
import sys
import time
import random

RED = "\033[31m"
RESET = "\033[0m"

BANNER = RED + r"""
 _____      ____ _                            
|_   _|_  _/ ___| |__   __ _ _ __   __ _  ___ _ __
  | | \ \/ / |   | '_ \ / _` | '_ \ / _` |/ _ \ '__|
  | |  >  <| |___| | | | (_| | | | | (_| |  __/ |
  |_| /_/\_\\____|_| |_|\__,_|_| |_|\__, |\___|_|
                                    |___/
""" + RESET + RED + "        made by v4idbro\n" + RESET


def load_proxies(path):
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(full_path, "r") as f:
        return [line.strip() for line in f if line.strip()]


def ask(prompt):
    return input(RED + prompt + RESET)


def apply_proxy(proxy):
    os.environ["HTTP_PROXY"] = proxy
    os.environ["HTTPS_PROXY"] = proxy
    os.environ["http_proxy"] = proxy
    os.environ["https_proxy"] = proxy
    print(RED + "IP Changed to " + proxy + RESET)


def proxy_changer():
    proxies = load_proxies("proxies.txt")
    interval_raw = ask("How soon should it change? ")
    duration_raw = ask("For how long? (Leave blank for infinite time) ")

    try:
        interval = float(interval_raw)
    except ValueError:
        interval = 60.0

    duration = None
    if duration_raw.strip():
        try:
            duration = float(duration_raw)
        except ValueError:
            duration = None

    start = time.time()
    while True:
        proxy = random.choice(proxies)
        apply_proxy(proxy)
        if duration is not None and (time.time() - start) >= duration:
            break
        time.sleep(interval)


def main():
    print(BANNER)
    print(RED + "[1] Proxy Changer" + RESET)
    choice = ask("> ")
    if choice.strip() == "1":
        proxy_changer()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
