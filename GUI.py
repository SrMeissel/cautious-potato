import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

#used to set radius from arbitrary input
min = 0
max = 1

# Wheel prefab
class Wheel:
    def __init__(self, wheelKey):
        with dpg.stage() as self._staging_container_id:
            # self._id = dpg.add_drawlist(width=200, height=200, tag= wheelKey + "Drawing")
            # self._id = dpg.draw_circle((100, 200/2), 100, tag= wheelKey, fill=[255, 255, 0], parent= wheelKey+ "Drawing")
            # self._id = dpg.add_text("Force: NA", tag= wheelKey + "text")

            with dpg.group() as group:
                dpg.add_drawlist(width=200, height=200, tag= wheelKey + "Drawing")
                dpg.draw_circle((100, 200/2), 100, tag= wheelKey, fill=[255, 255, 0], parent= wheelKey+ "Drawing")
                dpg.add_text("Force: NA", tag= wheelKey + "text")
            self._id = group



def init(lowest, highest):
    global min, max
    min = lowest
    max = highest

    dpg.create_context()

    # makes it look good
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(global_theme)

    # adds window content
    with dpg.window(tag="Primary Window", width=200, height=225, no_resize=True, no_title_bar=True) as window:
        pass
        # dpg.add_text("Force: NA", tag= "text")

        # with dpg.drawlist(width=200, height=200, ):
        #     dpg.draw_circle((100, 200/2), 100, tag= "Wheel", fill=[255, 255, 0])

    # Creates wheel instance and gives it a unique name and put it in the window
    leftWheel = Wheel("Wheel")
    dpg.move_item(leftWheel._id, parent="Primary Window")

    dpg.create_viewport(title='Cautious-Potato', width=600, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()

def update(value):
    # compute value within specified range
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    # min = 10, max = 90
    radius = (value - min) * (90 - 10) / (max - min) + 10

    # update graphic
    dpg.configure_item("Wheel", radius=radius)
    dpg.configure_item("Wheeltext", default_value=f"Force: {value}")
    dpg.render_dearpygui_frame()

def shutdown():
    dpg.destroy_context()