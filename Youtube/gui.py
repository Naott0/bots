import time
import dearpygui.dearpygui as dpg
import pytube
from tqdm import tqdm


def download():
    mylist = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    for i in tqdm(mylist):
        dpg.set_value('bar', i)
        time.sleep(0.1)
        pytube_sop.streams.get_highest_resolution().download()

    print("Finish")
    with dpg.window(label="", pos=(150, 50), tag='modal_id'):
        dpg.add_text('Loading is complete')
        dpg.add_button(label="OK", pos=(70, 50), callback=lambda: dpg.configure_item("modal_id", show=False))


def url(sender):
    global pytube_sop
    global text_tag
    sop = (dpg.get_value(sender))
    pytube_sop = pytube.YouTube(sop)
    text_tag = pytube_sop.title
    print('Url OK')
    print(text_tag)


def on_kill():
    dpg.stop_dearpygui()


dpg.create_context()

with dpg.window(tag="Primary Window"):
    width, height, channels, data = dpg.load_image("video.png")

    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (255, 140, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

        with dpg.theme_component(dpg.mvInputInt):
            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (140, 255, 23), category=dpg.mvThemeCat_Core)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

    with dpg.viewport_menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="Exit", callback=on_kill)

        dpg.add_menu_item(label="Help")

    dpg.bind_theme(global_theme)
    # dpg.add_text("Hi! download Youtube for yourself  ! ", pos=(100, 30))
    dpg.add_progress_bar(tag='bar', default_value=0, pos=(10, 60))
    dpg.add_input_text(label='URL', callback=url, tag='url', pos=(10, 90))
    dpg.add_button(label="Download", callback=download, width=100, height=20, tag='Save', pos=(10, 120))
    dpg.add_image("texture_tag", pos=(310, 50))

    with dpg.tooltip("Save"):
        dpg.add_text("Click to Download")

    with dpg.tooltip("url"):
        dpg.add_text("Paste url")

    with dpg.tooltip("bar"):
        dpg.add_text("Progress bar")

dpg.create_viewport(title='Downloader', width=400, height=100)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
