from pathlib import Path
import sqlite3
import csv
command_dir = Path("commands/")
conn = sqlite3.connect("productdatabase.db")
cursor = conn.cursor()
try:
    cursor.execute('create table if not exists Stock (name text, price real, quantity integer)')
    cursor.execute('create table if not exists Transactions (date text, name text, quantity integer)')
except Exception:
    print('Table cannot be created')


def get_command_file(command):
    return command_dir / f'{command}.py' 
         
def execute_command(command, args):
    try:
        with open(get_command_file(command)) as f:
            exec(f.read())

            if len(args) >= 1 and args[0] == "-v":
                print("Version ", eval('version'))
            else:
                verify = eval(f"check(*args)")
                if verify:
                    print(eval(f"run(*args)"))
                else:
                    print("Usage:", eval("usage"))
    except Exception as e:
        print(e)

def verify_command(command):
    return get_command_file(command).exists()

def list_commands():
    for f in command_dir.glob("*.py"):
        command = f.stem.lower()
        with open(get_command_file(command)) as f:
            exec(f.read())
            d = eval("description")
            #usage = eval("usage")
            print(f"{command}\t{d}")

def main():
    while True:
        command = input("Command> ")

        match command:
            case 'bye' | 'q' | 'quit':
                break
            case '?' | 'h' | 'help':
                list_commands()
            case _:
                name, *args = command.split()
                if verify_command(name):
                    execute_command(name, args)
                else:
                    print("Unknown command: ", name)

if __name__ == '__main__':
    main()

conn.commit()
conn.close()