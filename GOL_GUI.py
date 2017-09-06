from Tkinter import *
from GOL_Simulation import GOL_Simulation


def init_widgets(widgets):
    for row, row_list in enumerate(widgets):
        for col, widget in enumerate(row_list):
            widget.grid(row=row, column=col)


def validate_float(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789.-+':
        try:
            if action != 0 and len(prior_value) > 1:
                float(value_if_allowed)

            return True
        except ValueError:
            return False
    else:
        return False


def validate_int(action, index, value_if_allowed, prior_value, text, validation_type, trigger_type, widget_name):
    if text in '0123456789-+':
        try:
            if action != 0 and len(prior_value) > 1:
                int(value_if_allowed)

            return True
        except ValueError:
            return False
    else:
        return False


def _get_conf_values():
    values = []

    for row in CONFIG_WIDGET_LIST:
        for widget in row:
            if widget.winfo_class() == 'Entry':

                if not widget.get():
                    values.append(None)
                elif '.' in widget.get():
                    values.append(float(widget.get()))
                else:
                    values.append(int(widget.get()))
    return values


def create_simulation():
    default_values = [50, 5, 5, 50, 0.025, 5]
    param_values = _get_conf_values()

    param_values = [v if v else default_values[i] for i, v in enumerate(param_values)]

    CONFIG_FRAME.destroy()

    NEW_SIM = GOL_Simulation(*param_values)


ROOT = Tk()
CONFIG_FRAME = Frame(ROOT)

VCMD_FLOAT = (ROOT.register(validate_float), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
VCMD_INT = (ROOT.register(validate_int), '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')

CONFIG_WIDGET_LIST = [
    [
        Label(CONFIG_FRAME, text='Population size:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_INT)
    ],
    [
        Label(CONFIG_FRAME, text='Creature width:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_INT)
    ],
    [
        Label(CONFIG_FRAME, text='Creature height:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_INT)
    ],
    [
        Label(CONFIG_FRAME, text='Evaluation iterations:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_INT)
    ],
    [
        Label(CONFIG_FRAME, text='Mutation chance:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_FLOAT)
    ],
    [
        Label(CONFIG_FRAME, text='Creatures to remain:'),
        Entry(CONFIG_FRAME, validate='key', validatecommand=VCMD_INT)
    ],
    [
        Button(CONFIG_FRAME, text='Create simulation', command=create_simulation)
    ]
]

init_widgets(CONFIG_WIDGET_LIST)

CONFIG_FRAME.pack()

ROOT.mainloop()
