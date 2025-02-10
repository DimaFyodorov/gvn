import core.shape as shape


class CommandProcessor:

    def __init__(self, ru: bool):
        self.ru = ru
        self.coordinates = [0, 0]
        self.logs = []
        self.stack = []
        self.draw_color = "black"
        self.fill_color = "None"
        self.save_file = None

    def process(self, token: list[str]) -> None:
        match token[1]:
            case "Set":
                self.coordinates = [float(token[2]), float(token[3])]
                self.logs.append(f"Cordinates set: {self.coordinates}")
            case "Set_Draw_Color":
                self.draw_color = token[2]
                self.logs.append(f"Draw color set: {self.draw_color}")
            case "Set_Fill_Color":
                self.fill_color = token[2]
                self.logs.append(f"Fill color set: {self.fill_color}")
            case "Save":
                self.save_file = token[2]
                self.logs.append(f"Save file: {self.save_file}")
                self.stack.append(self.save_file)
            case "Circle":
                self.logs.append(f"Create circle: {token[2:]}")
                self.stack.append(
                    shape.Circle(
                        *(float(i) for i in token[2:]),
                        fill_color=self.fill_color,
                        draw_color=self.draw_color,
                    )
                )
            case "Ellipse":
                self.logs.append(f"Create ellipse: {token[2:]}")
                self.stack.append(
                    shape.Ellipse(
                        (float(token[2]), float(token[4])),
                        (float(token[3]), float(token[5])),
                        fill_color=self.fill_color,
                        draw_color=self.draw_color,
                    )
                )
            case "Rectangle":
                self.logs.append(f"Create rectangle: {token[2:]}")
                self.stack.append(
                    shape.Rectangle(
                        (float(token[2]), float(token[4])),
                        (float(token[3]), float(token[5])),
                        fill_color=self.fill_color,
                        draw_color=self.draw_color,
                    )
                )
            case "Line":
                self.logs.append(f"Create line: {token[2:]}")
                self.stack.append(
                    shape.Line(
                        (float(token[2]), float(token[4])),
                        (float(token[3]), float(token[5])),
                        draw_color=self.draw_color,
                    )
                )
            case "Line_to":
                self.logs.append(f"Create line: {token[2:]}, to {self.coordinates}")
                self.stack.append(
                    shape.Line(
                        (float(token[2]), self.coordinates[0]),
                        (float(token[3]), self.coordinates[1]),
                        draw_color=self.draw_color,
                    )
                )
            case "Fill":
                x, y = float(token[2]), float(token[3])
                for fig in self.stack:
                    if type(fig) == str:
                        continue
                    if fig.is_dot_inside(x, y):
                        fig.draw_color = token[4]
            case _:
                self.logs.append(f"Unknown command. Token: {token}")

        return None
