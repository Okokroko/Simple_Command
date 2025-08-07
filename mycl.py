import os
import subprocess

while True:
    try:
        # Display prompt
        command = input("mysh> ").strip()

        # Exit command
        if command.lower() == "exit":
            break

        # Skip empty input
        if not command:
            continue

        # Parse command
        args = command.split()

        # Handle 'cd' as a built-in
        if args[0] == "cd":
            try:
                os.chdir(args[1])
            except IndexError:
                print("cd: missing argument")
            except FileNotFoundError:
                print("cd: no such directory")
            continue

        # Run external command
        subprocess.run(args)

    except KeyboardInterrupt:
        print()  # Move to next line on Ctrl+C
    except EOFError:
        break  # Ctrl+D exits the shell
