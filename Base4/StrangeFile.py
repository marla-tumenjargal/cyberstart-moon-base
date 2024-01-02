try:
    with open("/tmp/alien-signal.txt", "r") as alien_file:
        print(alien_file.read())
except FileNotFoundError:
    print(f"The file '{"/tmp/alien-signal.txt"}' was not found.")
