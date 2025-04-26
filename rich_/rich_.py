from rich.console import Console
from rich.table import Table

console_ = Console()
table_ = Table(title="My Table")

table_.add_column("Name", justify="right", style="cyan", no_wrap=True)
table_.add_column("Age", justify="center", style="magenta")
table_.add_row("John", "20")
table_.add_row("Alice", "30")

console_.print(table_)  
console_.print("This is some text")
console_.print("This is some text", style="bold")
console_.print("This is some text", style="bold underline green")
console_.print("This is some text", style="bold underline green on white")
console_.print("[bold]This[/] is some text", style=" underline green on white")
a=10
b=20
console_.log("Print a and b: ", log_locals=True)