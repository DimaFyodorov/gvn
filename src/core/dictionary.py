type XY_COORDINATES = tuple[float, float]
type XY_COORDINATES_RADIUS = tuple[float, float, float]
type XY_COORDINATES_COLOR = tuple[float, float, str]
type XY1_XY2_COORDINATES = tuple[float, float, float, float]
type COLOR = str
type NAME = str

type_dict = {
    XY_COORDINATES: "X1, Y1",
    XY_COORDINATES_RADIUS: "X1, Y1, Radius",
    XY_COORDINATES_COLOR: "X1, Y1, Color",
    XY1_XY2_COORDINATES: "X1, Y1, X2, Y2",
    COLOR: "Color",
    NAME: "File name",
}

type_dictionary = {
    "Set": XY_COORDINATES,
    "Line_to": XY_COORDINATES,
    "Line": XY1_XY2_COORDINATES,
    "Circle": XY_COORDINATES_RADIUS,
    "Ellipse": XY1_XY2_COORDINATES,
    "Rectangle": XY1_XY2_COORDINATES,
    "Set_Draw_Color": COLOR,
    "Set_Fill_Color": COLOR,
    "Fill": XY_COORDINATES_COLOR,
    "Save": NAME,
}

dictionary_ru = {
    "Установить": "Set",
    "Линия_к": "Line_to",
    "Линия": "Line",
    "Окружность": "Circle",
    "Эллипс": "Ellipse",
    "Прямоугольник": "Rectangle",
    "Цвет_Рисования": "Set_Draw_Color",
    "Цвет_Закраски": "Set_Fill_Color",
    "Закрасить": "Fill",
    "Сохранить": "Save",
}
