from cli_interface import CLIInterface
from utils.database import Session

def main():
    session = Session()
    cli_interface = CLIInterface(session)
    cli_interface.main()

if __name__ == "__main__":
    main()