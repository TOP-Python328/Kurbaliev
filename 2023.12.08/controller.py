import model
import view


class Application:
    def save_email(email):
        model.FileIO.add_email(email)
        return f"save_email {email}"

    def get_emails():
        while get_email := view.CLI.get_email():
            try:
                email = model.Email(get_email)
                model.FileIO.add_email(email.email)
                view.CLI.save_email()
            except Exception:
                view.CLI.invalid_email()
                break

