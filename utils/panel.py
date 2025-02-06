from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
import json

def Panel():
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")

    # ASCII Title in Red
    ascii_title = Text("""__                       ___       ____    ___                                           
     /\ \                     /\_ \     /\  _`\ /\_ \                                          
   __\ \ \___     ___   __  __\//\ \    \ \ \/\_\//\ \     ___     ___      __   _ __          
 /'_ `\ \  _ `\  / __`\/\ \/\ \ \ \ \    \ \ \/_/_\ \ \   / __`\ /' _ `\  /'__`\/\`'__\        
/\ \L\ \ \ \ \ \/\ \L\ \ \ \_\ \ \_\ \_   \ \ \L\ \\_\ \_/\ \L\ \/\ \/\ \/\  __/\ \ \/         
\ \____ \ \_\ \_\ \____/\ \____/ /\____\   \ \____//\____\ \____/\ \_\ \_\ \____\\ \_\         
 \/___L\ \/_/\/_/\/___/  \/___/  \/____/    \/___/ \/____/\/___/  \/_/\/_/\/____/ \/_/         
   /\____/                                                                                     
   \_/__/                                                                                          
""", style="bold red")

    console = Console()
    console.print(ascii_title)

    # Define custom styles for ON and OFF
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    # Create a table with 2 columns
    table = Table(title="Ghoul Cloner", show_header=True, header_style="bold")
    table.add_column("Setting", style="cyan", no_wrap=True, width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    console.print(table)


def Panel_Run(guild, user):
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")

    # ASCII Title in Red
    ascii_title = Text("""
__                       ___       ____    ___                                           
     /\ \                     /\_ \     /\  _`\ /\_ \                                          
   __\ \ \___     ___   __  __\//\ \    \ \ \/\_\//\ \     ___     ___      __   _ __          
 /'_ `\ \  _ `\  / __`\/\ \/\ \ \ \ \    \ \ \/_/_\ \ \   / __`\ /' _ `\  /'__`\/\`'__\        
/\ \L\ \ \ \ \ \/\ \L\ \ \ \_\ \ \_\ \_   \ \ \L\ \\_\ \_/\ \L\ \/\ \/\ \/\  __/\ \ \/         
\ \____ \ \_\ \_\ \____/\ \____/ /\____\   \ \____//\____\ \____/\ \_\ \_\ \____\\ \_\         
 \/___L\ \/_/\/_/\/___/  \/___/  \/____/    \/___/ \/____/\/___/  \/_/\/_/\/____/ \/_/         
   /\____/                                                                                     
   \_/__/
""", style="bold red")

    console = Console()
    console.print(ascii_title)

    # Define custom styles for ON and OFF
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    # Create a table with 2 columns
    table = Table(title="Ghoul Cloner", show_header=True, header_style="bold")
    table.add_column("Setting", style="cyan", no_wrap=True, width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        table.add_row(setting.capitalize(), Text("ON" if status else " OFF", style=on_style if status else off_style))

    console.print(table)