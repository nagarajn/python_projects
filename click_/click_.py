import click

@click.command()
@click.option("--name", default="World", help="Name to greet", prompt="Please enter your name")
def hello(name):
    print(f"Hello {name}")


@click.group
def mycommands():
    pass


PRIORITIES = {
    "o": "option",
    "l": "low",
    "m": "medium",
    "h": "high",
    "c": "Crucial"}
@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("--name", "-n", prompt="Enter the TODO name", help="The name of the todo")
@click.option("--description", "-d", prompt="Enter the TODO description", help="The description of the todo item")
def add_todo(name, description, priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "a+") as f:
        f.write(f"{name}: {description} {PRIORITIES[priority]}\n")

@click.command()
@click.argument("idx", type=int, required=True)
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
        lines = f.readlines()
    with open("mytodos.txt", "w") as f:
        for i, line in enumerate(lines):
            if i != idx:
                f.write(line)

@click.command()
@click.option("-p", "--priority", type=click.Choice(PRIORITIES.keys()))
@click.option("todofile", "-f", type=click.Path(exists=True), required=False)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else "mytodos.txt"
    with open(filename, "r") as f:
        for i, line in enumerate(f.readlines()):
            if priority is not None and PRIORITIES[priority] not in line:
                continue
            print(f"{i}: {line}", end="")


mycommands.add_command(hello)
mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)

if __name__ == "__main__":
    mycommands()