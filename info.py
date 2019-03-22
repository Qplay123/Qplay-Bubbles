from time import sleep, time


def show_score(canvas, texts, score):
    """
    Shows Score
    :param texts:
    :param canvas:
    :param score:
    :return:
    """
    canvas.itemconfig(texts["score"], text=str(score))


def show_level(canvas, texts, level):
    """
    Shows Level
    :param canvas:
    :param texts:
    :param level:
    :return:
    """
    canvas.itemconfig(texts["level"], text=str(level))


def show_speed(canvas, texts, speed):
    """
    Shows Speed
    :param texts:
    :param canvas:
    :param speed:
    :return:
    """
    canvas.itemconfig(texts["speed"], text=str(speed))


def show_lives(canvas, texts, lives):
    """
    Shows Lives
    :param canvas:
    :param texts:
    :param lives:
    :return:
    """
    canvas.itemconfig(texts["lives"], text=str(lives))


def show_score_point(canvas, texts, data):
    """
    Shows score status value
    :param texts:
    :param canvas:
    :param data:
    :return:
    """
    canvas.itemconfig(texts["scorestate"], text=data)


def show_protection(canvas, texts, on_off):
    """
    shows security-state
    :param canvas:
    :param texts:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["secure"], text=on_off)


def show_slowmotion(canvas, texts, on_off):
    """
    shows slow motion state
    :param texts:
    :param canvas:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["slowmotion"], text=on_off)


def show_confusion(canvas, texts, on_off):
    """
    shows confusion state
    :param canvas:
    :param texts:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["confusion"], text=on_off)


def show_timebreak(canvas, texts, on_off):
    """
    shows timebreak state
    :param texts:
    :param canvas:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["timebreak"], text=on_off)


def show_spdboost(canvas, texts, on_off):
    """
    shows speedboost state
    :param texts:
    :param canvas:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["speedboost"], text=on_off)


def show_paralis(canvas, texts, on_off):
    """
    shows paralis state
    :param texts:
    :param canvas:
    :param on_off:
    :return:
    """
    canvas.itemconfig(texts["paralis"], text=on_off)


def show_shotspeed(canvas, texts, integer):
    """
    Shows Shot-speed state
    :param canvas:
    :param texts:
    :param integer:
    :return:
    """
    canvas.itemconfig(texts["shotspeed"], text=integer)


def show_tps(canvas, texts, integer):
    """
    Shows Teleports
    :param canvas:
    :param texts:
    :param integer:
    :return:
    """
    canvas.itemconfig(texts["shiptp"], text=str(integer))


def show_notouch(canvas, texts, integer):
    """
    Shows Teleports
    :param canvas:
    :param texts:
    :param integer:
    :return:
    """
    canvas.itemconfig(texts["notouch"], text=str(integer))


def show_diamond(canvas, texts, integer):
    """
    Shows Diamonds
    :param canvas:
    :param texts:
    :param integer:
    :return:
    """
    canvas.itemconfig(texts["diamond"], text=str(integer))


def show_coin(canvas, texts, integer):
    """
    Shows Coins
    :param texts:
    :param canvas:
    :rtype: object

    :param integer:
    """
    canvas.itemconfig(texts["coin"], text=str(integer))


def view_level(canvas, root, texts, level):
    """
    Viewes level
    """
    canvas.itemconfig(texts["level-view"], text="Level " + str(level))
    root.update()
    sleep(2)
    canvas.itemconfig(texts["level-view"], text="")
    root.update()


def show_info(canvas, texts, stats):
    """
    Shows all information:
    Score, Level, status-time etc.
    :return:
    """
    show_score(canvas, texts, stats["score"])
    show_level(canvas, texts, stats["level"])
    show_speed(canvas, texts, stats["shipspeed"])
    show_lives(canvas, texts, stats["lives"])
    show_score_point(canvas, texts, str(int(stats["scorestate-time"] - time())))
    show_protection(canvas, texts, str(int(stats["secure-time"] - time())))
    show_slowmotion(canvas, texts, str(int(stats["slowmotion-time"] - time())))
    show_confusion(canvas, texts, str(int(stats["confusion-time"] - time())))
    show_timebreak(canvas, texts, str(int(stats["timebreak-time"] - time())))
    show_spdboost(canvas, texts, str(int(stats["speedboost-time"] - time())))
    show_paralis(canvas, texts, str(int(stats["paralis-time"] - time())))
    show_shotspeed(canvas, texts, str(int(stats["shotspeed-time"] - time())))
    show_notouch(canvas, texts, str(int(stats["notouch-time"] - time())))
    show_tps(canvas, texts, stats["teleports"])
    show_diamond(canvas, texts, stats["diamonds"])
    show_coin(canvas, texts, stats["coins"])