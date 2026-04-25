import tkinter as tk


class CalculatorLogic:
    """Handles the underlying math logic and state for the calculator."""
    def __init__(self) -> None:
        self.expression = ""

    def append(self, value: str) -> str:
        if self.expression == "Error":
            self.expression = ""
        self.expression += str(value)
        return self.expression

    def clear(self) -> str:
        self.expression = ""
        return "0"

    def calculate(self) -> str:
        if not self.expression:
            return "0"
        try:
            # Safely evaluate the math expression by restricting builtins and locals.
            # Note: For a production app, consider a dedicated math parser (e.g., ast-based).
            result = eval(self.expression, {"__builtins__": {}}, {})
            
            # Format nicely (remove trailing .0 for integers)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            self.expression = str(result)
            return self.expression
        except ZeroDivisionError:
            self.expression = ""
            return "Error"
        except Exception:
            self.expression = ""
            return "Error"


class CalculatorApp:
    """Handles the graphical user interface for the calculator."""
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)

        self.logic = CalculatorLogic()
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
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("=", 4, 1), ("+", 4, 2), ("C", 4, 3),
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
        new_display = self.logic.append(value)
        self.display_var.set(new_display)

    def clear(self) -> None:
        new_display = self.logic.clear()
        self.display_var.set(new_display)

    def calculate(self) -> None:
        new_display = self.logic.calculate()
        self.display_var.set(new_display)


def main() -> None:
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()