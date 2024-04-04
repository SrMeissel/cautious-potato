import dearpygui.dearpygui as dpg
from datetime import datetime

#used to set radius from arbitrary input
min = 0
max = 1

# Plot data
dataX = []
dataY = []

#time at GUI init
startTime = 0

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
    global min, max, startTime
    min = lowest
    max = highest
    startTime = datetime.now()

    dpg.create_context()

    # makes it look good
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 0, category=dpg.mvThemeCat_Core)
    dpg.bind_theme(global_theme)

    # adds window content
    with dpg.window(tag="Primary Window", no_resize=True, no_title_bar=True) as window:
        with dpg.group(horizontal=True):
            with dpg.table(header_row=False, borders_innerH=True, borders_outerH=True, borders_innerV=True, borders_outerV=True,
                        policy=dpg.mvTable_SizingFixedFit, no_clip=True, width=420):
                # Wheel grid
                dpg.add_table_column()
                with dpg.table_row():
                    dpg.add_table_cell(tag="cell1")
                    dpg.add_table_cell(tag="cell2")
                dpg.add_table_column()
                with dpg.table_row():
                    dpg.add_table_cell(tag="cell3")
                    dpg.add_table_cell(tag="cell4")
            with dpg.group():
                dpg.add_button(label="Start", tag="Start")
                dpg.add_button(label="Stop", tag="Stop")
                with dpg.group():
                    dpg.add_text("Left Front")
                    dpg.add_text("Right Front")
                    dpg.add_text("Left Back")
                    dpg.add_text("Right Back")

                with dpg.plot(label="Normal Forces", height=350, width=350, no_menus=True, no_mouse_pos=True):
                    dpg.add_plot_axis(dpg.mvXAxis, label="x", tag="x_axis_1" , no_tick_labels=True, no_tick_marks=True, no_gridlines=True)
                    dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis", no_tick_labels=True, no_tick_marks=True, no_gridlines=True)

                    dpg.add_line_series([], [], label="0.5 + 0.5 * sin(x)", parent="y_axis", tag="plot", )
            


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
    dpg.create_viewport(title='Cautious-Potato', width=800, height=540)
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
    global dataX, dataY, startTime

    #update the values of each wheel
    updateWheel(valueSet[0], "WheelLeftFront")
    updateWheel(valueSet[1], "WheelRightFront")
    updateWheel(valueSet[2], "WheelLeftBack")
    updateWheel(valueSet[3], "WheelRightBack")

    dataY.append(valueSet[3])
    dataX.append((datetime.now()-startTime).total_seconds())
    dpg.set_value('plot', [dataX, dataY])
    dpg.fit_axis_data('x_axis_1')
    dpg.fit_axis_data('y_axis')
    
    #draw the damn thing
    dpg.render_dearpygui_frame()

def setStartButtonCallback(callback):
    dpg.set_item_callback("Start", callback)

def setStopButtonCallback(callback):
    dpg.set_item_callback("Stop", callback)

def shutdown():
    dpg.destroy_context()