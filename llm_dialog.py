import llm
from prompt_toolkit import shortcuts


@llm.hookimpl
def register_tools(register):
    register(prompt)
    register(Dialog)


def prompt(message: str) -> str:
    """Prompt the user for input."""
    return shortcuts.prompt(message)


class Dialog(llm.Toolbox):
    def message(self,
        title: str = '',
        text: str = '',
        ok_text: str = 'OK'
    ) -> None:
        """Display a simple message box and wait until the user presses enter."""
        return shortcuts.message_dialog(title, text, ok_text).run()

    def yes_no(self,
        title: str = '',
        text: str = '',
        yes_text: str = 'Yes',
        no_text: str = 'No'
    ) -> bool:
        """Display a Yes/No dialog."""
        return shortcuts.yes_no_dialog(title, text, yes_text, no_text).run()

    def input(self,
        title: str = '',
        text: str = '',
        ok_text: str = 'OK',
        cancel_text: str = 'Cancel',
        password: bool = False,
        default: str = ''
    ) -> str | None:
        """Display a text input box. Return the given text, or None when cancelled."""
        return shortcuts.input_dialog(
            title, text, ok_text, cancel_text, password, default
        ).run()

    def radiolist(self,
        title: str = '',
        text: str = '',
        ok_text: str = 'OK',
        cancel_text = 'Cancel',
        values: list[str] = [],
        default: str | None = None
    ) -> str | None:
        """Display a list of elements the user can choose amongst. Only one element can be selected at a time using Arrow keys and Enter. The focus can be moved between the list and the Ok/Cancel button with tab."""
        return shortcuts.radiolist_dialog(
            title, text, ok_text, cancel_text,
            [(x, x) for x in values], default
        ).run()

    def checkboxlist(self,
        title: str = '',
        text: str = '',
        ok_text: str = 'OK',
        cancel_text = 'Cancel',
        values: list[str] = [],
        default_values: list[str] = []
    ) -> str | None:
        """Display a list of elements the user can choose multiple values amongst. Several elements can be selected at a time using Arrow keys and Enter. The focus can be moved between the list and the Ok/Cancel button with tab."""
        return shortcuts.checkboxlist_dialog(
            title, text, ok_text, cancel_text,
            [(x, x) for x in values], default_values
        ).run()
