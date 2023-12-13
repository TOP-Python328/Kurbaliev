import controller
import view


def start():
    view.CLI.start_email()

def main():
    controller.Application.get_emails()

def end():
    view.CLI.end_email()

if __name__ == "__main__":
    start()
    main()
    end()
