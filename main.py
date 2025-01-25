from cli_interface.main import CLIInterface

def main():
    try:
        cli = CLIInterface()
        cli.main()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()