import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def init():
    dpg.create_context()

    with dpg.window(tag="Primary Window", width=225, height=300, no_resize=True, no_title_bar=True) as window:
        dpg.add_text("Force: NA", tag= "text1", pos=(225/2, 0))
        dpg.draw_circle((0, 0), 100, tag= "Wheel")
        

    dpg.create_viewport(title='Cautious-Potato', width=600, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # dpg.set_primary_window("Primary Window", True)

def update(value):
    dpg.configure_item("Wheel", radius=value/4)
    dpg.configure_item("text1", default_value=f"Force: {value}")
    dpg.render_dearpygui_frame()
    # print("frame rendered")

def shutdown():
    dpg.destroy_context()