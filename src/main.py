import argparse

import core.parser as parser
import core.visualizer as visualizer
import core.engine as engine


cli_parser = argparse.ArgumentParser(
    prog="gvn",
    description="GVN - GVN is Vector Notation.\nIt is a simple language for describing vector graphics.",
    epilog="You can find more information on GitHub: https://github.com/DimaFyodorov/gvn",
    formatter_class=argparse.RawTextHelpFormatter,
)
cli_parser.add_argument(
    "file",
    type=str,
    help="Path to file with program",
)
cli_parser.add_argument(
    "-r",
    "--russian",
    action="store_true",
    help="Use russian dictionary",
)
cli_parser.add_argument(
    "-c",
    "--code",
    action="store_true",
    help="Visualize the source code",
)
cli_parser.add_argument(
    "-g",
    "--show_grid",
    action="store_true",
    help="Add grid to image.",
)
cli_parser.add_argument(
    "-s",
    "--show",
    action="store_true",
    help="Open interactive window.",
)


def main(text: str, ru: bool, grid: bool, show: bool, show_code: bool):
    code, source_code = parser.pars(text, ru)
    if type(code) == str:
        print(code)
        exit()

    if show_code:
        visualizer.show_code(source_code)

    processor = engine.CommandProcessor(ru)

    for token in code:
        processor.process(token)

    figures = processor.stack

    max_y = max_x = 0
    min_y = min_x = float("inf")
    for fig in figures:
        if type(fig) == str:
            continue

        min_x = min(min_x, fig.hitbox[0][0])
        max_x = max(max_x, fig.hitbox[0][1])
        min_y = min(min_y, fig.hitbox[1][0])
        max_y = max(max_y, fig.hitbox[1][1])

    x_lim = (min_x - 1, max_x + 1)
    y_lim = (min_y - 1, max_y + 1)

    visualizer.draw(figures, x_lim, y_lim, grid, show)


if __name__ == "__main__":
    args = cli_parser.parse_args()

    with open(args.file, "r", encoding="utf-8") as file:
        text = file.read()

    main(text, args.russian, args.show_grid, args.show, args.code)
