"""Построчный парсинг для последующей работы."""

# Импорты
from copy import deepcopy


import core.dictionary as dct
import core.visualizer as visualizer

import matplotlib.colors


def is_comment(token: list[str]) -> bool:
    if token[1].startswith("#"):
        return 1
    return 0


def valid(token: list[str], ru: bool = False) -> bool:
    if ru:
        name_spapase = dct.dictionary_ru.keys()
    else:
        name_spapase = dct.dictionary_ru.values()

    if token[1] not in name_spapase:
        token[0] = "!" + str(token[0])
        visualizer.show_error(token, 1, ru)

        return 1

    elif len(token) == 2:
        token[0] = "!" + str(token[0])
        visualizer.show_error(token, 2, ru)

        return 1

    return 0


def lang_swap(token: list[str]) -> list[str]:
    new_token = token.copy()
    new_token[1] = dct.dictionary_ru[token[1]]
    return new_token


def valid_color(args: list[str]) -> bool:
    if len(args) != 1:
        return 1
    if not matplotlib.colors.is_color_like(args[0]):
        return 1
    return 0


def valid_float(args: list[str], count: int) -> bool:
    if "inf" in args:
        return 1
    try:
        for i in range(count):
            float(args[i])
    except ValueError:
        return 1
    return 0


def valid_xy_color(args: list[str]) -> bool:
    if len(args) != 3:
        return 1
    if valid_float(args[:2], 2) or valid_color([args[2]]):
        return 1
    return 0


def valid_words(args: list[str], count: int) -> bool:
    if len(args) != count:
        return 1
    for arg in args:
        if type(arg[0]) != str:
            return 1
    return 0


def args_validator(token: list[str], ru) -> bool:
    if ru:
        token_type = dct.type_dictionary[dct.dictionary_ru[token[1]]]
    else:
        token_type = dct.type_dictionary[token[1]]
    match token_type:
        case dct.XY_COORDINATES:
            ret = valid_float(token[2:], 2)
        case dct.XY_COORDINATES_RADIUS:
            ret = valid_float(token[2:], 3)
        case dct.XY1_XY2_COORDINATES:
            ret = valid_float(token[2:], 4)
        case dct.XY_COORDINATES_COLOR:
            ret = valid_xy_color(token[2:])
        case dct.COLOR:
            ret = valid_color(token[2:])
        case dct.NAME:
            ret = valid_words(token[2:], 1)
        case _:
            ret = 999

    if ret:
        visualizer.show_error(token, 3, ru)

    return ret


def pars(text: str, ru: bool = False) -> tuple[list[list[str]] | str, list[list[str]]]:
    err = 0
    code = []
    source_code = []

    text = text.splitlines()
    for line, n in zip(text, range(1, len(text) + 1)):
        source_code.append(line.split())
        source_code[n - 1].insert(0, n)

    for token in source_code:
        if len(token) == 1:
            continue

        if is_comment(token):
            continue

        if ru:
            if valid(token, ru):
                err += 1
                continue
            code.append(lang_swap(token))
        else:
            if valid(token):
                err += 1
                continue
            code.append(token.copy())

        err += args_validator(token, ru)

    if err:
        return (f"The code cannot be executed. {err} errors found.", source_code)
    return (code, source_code)
