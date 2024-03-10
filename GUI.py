import dearpygui.dearpygui as dpg
import dearpygui.demo as demo

#used to set radius from arbitrary input
min = 0
max = 1

# Wheel prefab
class Wheel:
    def __init__(self, wheelKey):
        with dpg.stage() as self._staging_container_id:
            with dpg.group() as group:
                dpg.add_text(default_value= wheelKey)
                dpg.add_drawlist(width=200, height=200, tag= wheelKey + "Drawing")
                dpg.draw_circle((100, 200/2), 100, tag= wheelKey, fill=[255, 255, 0], parent= wheelKey+ "Drawing")
                dpg.add_text("Force: NA", tag= wheelKey + "text")
            self._id = group

def init(lowest, highest):
    #I dont like python scoping :(
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
    with dpg.window(tag="Primary Window", no_resize=False, no_title_bar=True) as window:
        with dpg.table(header_row=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True,
                       policy=dpg.mvTable_SizingFixedFit, no_clip=True, width=420):
            dpg.add_table_column()
            dpg.add_table_column()
            with dpg.table_row():
                dpg.add_table_cell(tag="cell1")
                dpg.add_table_cell(tag="cell2")
            with dpg.table_row():
                dpg.add_table_cell(tag="cell3")
                dpg.add_table_cell(tag="cell4")

    # Creates wheel instance and gives it a unique name and puts it in the window
    leftWheelFront = Wheel("WheelLeftFront")
    dpg.move_item(leftWheelFront._id, parent="cell1")
    
    rightWheelFront = Wheel("WheelRightFront")
    dpg.move_item(rightWheelFront._id, parent="cell2")
    
    leftWheelBack = Wheel("WheelLeftBack")
    dpg.move_item(leftWheelBack._id, parent="cell3")
    
    rightWheelBack = Wheel("WheelRightBack")
    dpg.move_item(rightWheelBack._id, parent="cell4")
    
    dpg.set_primary_window("Primary Window", True)
    dpg.create_viewport(title='Cautious-Potato', width=600, height=600)
    dpg.setup_dearpygui()
    dpg.show_viewport()

# Prive abstraction for update function, no longer renders frame
def updateWheel(value, key):
    # compute value within specified range
    # https://www.arduino.cc/reference/en/language/functions/math/map/
    # min = 10, max = 90
    radius = (value - min) * (90 - 10) / (max - min) + 10

    # update graphic
    dpg.configure_item(key, radius=radius)
    dpg.configure_item(key + "text", default_value=f"Force: {value}")
    
def update(valueSet):
    #update the values of each wheel
    updateWheel(valueSet[0], "WheelLeftFront")
    updateWheel(valueSet[1], "WheelRightFront")
    updateWheel(valueSet[2], "WheelLeftBack")
    updateWheel(valueSet[3], "WheelRightBack")
    
    #draw the damn thing
    dpg.render_dearpygui_frame()


def shutdown():
    dpg.destroy_context()