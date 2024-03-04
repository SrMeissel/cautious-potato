import dearpygui.dearpygui as dpg
import dearpygui.demo as demo


def init():
    dpg.create_context()

    # makes it look good
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(global_theme)

    # adds window content
    with dpg.window(tag="Primary Window", width=200, height=225, no_resize=True, no_title_bar=True) as window:

        dpg.add_text("Force: NA", tag= "text1")

        with dpg.drawlist(width=200, height=200, ):
            dpg.draw_circle((100, 200/2), 100, tag= "Wheel", fill=[255, 255, 0])

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