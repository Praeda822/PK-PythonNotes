import builtins
from decimal import Decimal # handles decimals

class Colours:
    RESET = '\033[0m'
    STRING = '\033[93m'  # Yellow (strings)
    INTEGER = '\033[94m'  # Blue (integers)
    FLOAT = '\033[96m'  # Cyan (floats)
    DECIMAL = '\033[34m'  # Bright blue (decimals)
    BOOLEAN = '\033[95m'  # Purple/magenta (booleans)
    ERROR = '\033[91m'  # Red (errors/warnings)

# Save the original print function
original_print = builtins.print

def coloured_print(*args, **kwargs):
    coloured_args = []
    for arg in args:
        if isinstance(arg, str):
            coloured_args.append(f"{Colours.STRING}{arg}{Colours.RESET}")
        elif isinstance(arg, int):
            coloured_args.append(f"{Colours.INTEGER}{arg}{Colours.RESET}")
        elif isinstance(arg, float):
            coloured_args.append(f"{Colours.FLOAT}{arg}{Colours.RESET}")
        elif isinstance(arg, Decimal):  # Check specifically for decimal.Decimal
            coloured_args.append(f"{Colours.DECIMAL}{arg}{Colours.RESET}")
        elif isinstance(arg, bool):
            coloured_args.append(f"{Colours.BOOLEAN}{arg}{Colours.RESET}")
        else:
            coloured_args.append(arg)  # Fallback for unsupported types

    # Call the original print function
    original_print(*coloured_args, **kwargs)

# Override the built-in print with the coloured version
builtins.print = coloured_print
