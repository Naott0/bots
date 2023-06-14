import time

import dearpygui.dearpygui as dpg
import pytube
from tqdm import tqdm


class Value:

    def __init__(self):
        self.pytube_sop = None

    def print_value(self, sender):
        sop = (dpg.get_value(sender))
        self.pytube_sop = pytube.YouTube(sop)
        print('Fin')

    def download(self):
        self.pytube_sop.streams.download()
        mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x = 0
        dpg.set_value('bar', x)
        for i in tqdm(mylist):
            time.sleep(1)
            x = + 0.1


        print("!!!!")


dpg.create_context()

value = Value()
with dpg.window(tag="Primary Window"):
    dpg.add_text("Hi! download Youtube for yourself ! ")
    dpg.add_button(label="Save", callback=value.download)
    dpg.add_input_text(label='URL', callback=value.print_value)
    dpg.add_progress_bar(tag='bar', default_value=0)

dpg.create_viewport(title='Downloader', width=400, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
