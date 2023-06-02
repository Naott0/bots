import dearpygui.dearpygui as dpg
import pytube


def donwload():
    print_value.streams.get_highest_resolution().download()
    print('VIN')


def print_value(sender):
    sop = (dpg.get_value(sender))
    yt = pytube.YouTube(sop)
    print('Fin')
    return print_value


dpg.create_context()

with dpg.window(tag="Primary Window"):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save", callback=donwload)
    input_txt1 = dpg.add_input_text(label='URL', callback=print_value)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
