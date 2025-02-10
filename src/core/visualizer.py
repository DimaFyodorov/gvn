"""Рисование объектов в matplotlib, и прикольного строкового представления."""

import sys
from colorama import init as colorama_init
from colorama import Fore, Style

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.lines import Line2D

import core.dictionary as dct
import core.shape as shape

colorama_init(autoreset=True)
GRAY = "\033[90m"
UNDERLINE = "\033[4;31m"


def show_code(source_code: list[list[str]]) -> None:
    print(f"{Fore.MAGENTA}Source code:")
    for token in source_code:
        if len(token) == 1:
            print(f"{Fore.GREEN}[{Fore.CYAN}{token[0]:2}{Fore.GREEN}]")
            continue
        if token[1].startswith("#"):
            print(f'{GRAY}[{token[0]:2}] - [{" ".join(token[1:])}]')
            continue
        if str(token[0]).startswith("!"):
            print(
                f'{UNDERLINE}{Fore.RED}[{Fore.YELLOW}{token[0]:2}{Fore.RED}] - [{Fore.YELLOW}{" ".join(token[1:])}{Fore.RED}]'
            )
            continue
        print(
            f'{Fore.GREEN}[{Fore.CYAN}{token[0]:2}{Fore.GREEN}] - [{Fore.BLUE}{token[1]} {Fore.RED}{" ".join(token[2:])}{Fore.GREEN}]'
        )


def show_error(token: list, err_code: int, ru=False) -> None:
    if ru:
        if err_code == 1:
            print(
                f'{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{UNDERLINE}{Fore.YELLOW}{" ".join(token[1:])}{Fore.RED}]',
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 1] - {Fore.YELLOW}Неизвестная команда:{UNDERLINE}{Fore.RED} {token[1]}.",
                file=sys.stderr,
            )

        elif err_code == 2:
            print(
                f"{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{Fore.BLUE}{token[1]} {UNDERLINE}{Fore.YELLOW}  ?  {Style.RESET_ALL}{Fore.RED}]",
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 2] - {Fore.YELLOW}Не указан ни один аргумент. Ожидались:{UNDERLINE} {dct.type_dict[dct.type_dictionary[dct.dictionary_ru[token[1]]]]}.",
                file=sys.stderr,
            )

        elif err_code == 3:
            print(
                f'{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{Fore.BLUE}{token[1]} {UNDERLINE}{Fore.YELLOW}{" ".join(token[2:])}{Style.RESET_ALL}{Fore.RED}]',
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 3] - {Fore.YELLOW}Не верные аргументы. Ожидались:{UNDERLINE} {dct.type_dict[dct.type_dictionary[dct.dictionary_ru[token[1]]]]}.",
                file=sys.stderr,
            )

        else:
            print(
                f"{UNDERLINE}{Fore.RED}[{token[0]:2}] - [{token[0:]}]",
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 0] - {Fore.YELLOW}Неизвестная ошибка.", file=sys.stderr
            )

    else:
        if err_code == 1:
            print(
                f'{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{UNDERLINE}{Fore.YELLOW}{" ".join(token[1:])}{Fore.RED}]',
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 1] - {Fore.YELLOW}Unknown token:{UNDERLINE}{Fore.RED} {token[1]}.",
                file=sys.stderr,
            )

        elif err_code == 2:
            print(
                f"{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{Fore.BLUE}{token[1]} {UNDERLINE}{Fore.YELLOW}  ?  {Style.RESET_ALL}{Fore.RED}]",
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 2] - {Fore.YELLOW}No arguments specified. Expected:{UNDERLINE} {dct.type_dict[dct.type_dictionary[token[1]]]}.",
                file=sys.stderr,
            )

        elif err_code == 3:
            print(
                f'{Fore.RED}[{Fore.MAGENTA}{token[0]:2}{Fore.RED}] - [{Fore.BLUE}{token[1]} {UNDERLINE}{Fore.YELLOW}{" ".join(token[2:])}{Style.RESET_ALL}{Fore.RED}]',
                file=sys.stderr,
            )
            print(
                f"{Fore.RED}[ERR 3] - {Fore.YELLOW}Invalid arguments. Expected:{UNDERLINE} {dct.type_dict[dct.type_dictionary[token[1]]]}.",
                file=sys.stderr,
            )

        else:
            print(
                f"{UNDERLINE}{Fore.RED}[{token[0]:2}] - [{token[0:]}]",
                file=sys.stderr,
            )
            print(f"{Fore.RED}[ERR 0] - {Fore.YELLOW}Unknown error.", file=sys.stderr)


def draw(
    figures: list[str | shape.Circle | shape.Ellipse | shape.Rectangle | shape.Line],
    x_lim: tuple[float, float],
    y_lim: tuple[float, float],
    grid: bool,
    show: bool,
) -> None:
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.tight_layout()
    ax.set(xlim=x_lim, ylim=y_lim)

    if grid:
        plt.grid()

    for fig in figures:
        match fig:
            case shape.Circle():
                ax.add_patch(
                    patches.Circle(
                        *fig.coordinates,
                        facecolor=fig.fill_color,
                        edgecolor=fig.draw_color,
                    )
                )
            case shape.Ellipse():
                ax.add_patch(
                    patches.Ellipse(
                        *fig.coordinates,
                        facecolor=fig.fill_color,
                        edgecolor=fig.draw_color,
                    )
                )
            case shape.Rectangle():
                ax.add_patch(
                    patches.Rectangle(
                        *fig.coordinates,
                        facecolor=fig.fill_color,
                        edgecolor=fig.draw_color,
                    )
                )
            case shape.Line():
                ax.add_line(Line2D(*fig.coordinates, color=fig.draw_color))
            case str():
                plt.savefig(fig)
            case _:
                print(f"Unknown figure type: {type(fig)}")
                continue

    if show:
        plt.show()
