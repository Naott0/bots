import time
import dearpygui.dearpygui as dpg
import pytube
from tqdm import tqdm


def download():
    pytube_sop.streams.get_highest_resolution().download()
    mylist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    

    for i in tqdm(mylist):
        dpg.set_value('bar', i)
        time.sleep(0.1)


    print("!!!!")


def url(sender):
    global pytube_sop
    sop = (dpg.get_value(sender))
    pytube_sop = pytube.YouTube(sop)
    print('Fin')


class Value:
    pass


dpg.create_context()

value = Value()
with dpg.window(tag="Primary Window"):
    dpg.add_text("Hi! download Youtube for yourself ! ")
    dpg.add_button(label="Save", callback=download)
    dpg.add_input_text(label='URL', callback=url)
    dpg.add_progress_bar(tag='bar', default_value=0)

dpg.create_viewport(title='Downloader', width=400, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
