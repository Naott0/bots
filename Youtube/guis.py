import time
import dearpygui.dearpygui as dpg
import pytube
from tqdm import tqdm


def download():
    pytube_sop.streams.get_highest_resolution().download()
    mylist = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    for i in tqdm(mylist):
        dpg.set_value('bar', i)
        time.sleep(0.1)

    print("Finish")
    with dpg.window(label="", pos=(50,50), tag='modal_id'):
        dpg.add_text('Loading is complete')
        dpg.add_button(label="OK", callback=lambda: dpg.configure_item("modal_id", show=False))







def url(sender):
    global pytube_sop
    global title
    sop = (dpg.get_value(sender))
    pytube_sop = pytube.YouTube(sop)
    title = pytube_sop.title
    print('Url OK')
    print(title)





def on_kill():
    dpg.stop_dearpygui()


class Value:
    pass


dpg.create_context()

value = Value()
with dpg.window(tag="Primary Window"):
    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Exit", callback=on_kill)

        dpg.add_menu_item(label="Help", tag='Help')



    dpg.add_text("Hi! download Youtube for yourself ! ",  pos=(10, 30))
    dpg.add_progress_bar(tag='bar', default_value=0, pos=(10, 60))
    dpg.add_input_text(label='URL', callback=url, tag='url', pos=(10, 90))
    dpg.add_button(label="Download", callback=download, width=100, height=20, tag='Save', pos=(10, 120))

    with dpg.tooltip("Save"):
        dpg.add_text("Click to Download")

    with dpg.tooltip("url"):
        dpg.add_text("Paste url")

    with dpg.tooltip("bar"):
        dpg.add_text("Progress")


dpg.create_viewport(title='Downloader', width=400, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
