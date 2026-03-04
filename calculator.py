import tkinter as tk


class CalculatorApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self) -> None:
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Segoe UI", 20),
            justify="right",
            bd=8,
            relief="sunken",
            state="readonly",
            readonlybackground="white",
        )
        display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            ("=", 4, 1),
            ("+", 4, 2),
            ("C", 4, 3),
        ]

        for text, row, col in buttons:
            if text == "=":
                command = self.calculate
            elif text == "C":
                command = self.clear
            else:
                command = lambda value=text: self.on_button_click(value)

            button = tk.Button(
                self.root,
                text=text,
                font=("Segoe UI", 16),
                width=4,
                height=2,
                command=command,
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        for index in range(4):
            self.root.grid_columnconfigure(index, weight=1)

    def on_button_click(self, value: str) -> None:
        if self.display_var.get() == "Error":
            self.expression = ""

        self.expression += value
        self.display_var.set(self.expression)

    def clear(self) -> None:
        self.expression = ""
        self.display_var.set("0")

    def calculate(self) -> None:
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.expression = ""
            self.display_var.set("Error")
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
