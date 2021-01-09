import bpy
import bpy_extras
from random import randint, random, uniform
import math
import csv

# Alt P to run
# A to select all objects, X to delete, D to confirm
# CAMERA: To align move the viewport into position, select the camera and click ctrl+alt+Num0
# ORIGIN: Move Cursor to point, right click object and select > Set Origin to 3D Cursor


C = bpy.context
D = bpy.data

scene = bpy.context.scene
obj = bpy.context.object
co = bpy.context.scene.cursor.location


# Output settings
bpy.context.scene.render.resolution_x = 800
bpy.context.scene.render.resolution_y = 600


def get_rand_circle_points(radius):
    t, = 2 * math.pi * random(), 
    u, r = random() + random(), None
    if u > 1: r = 2 - u
    else: r = u
    return radius * r * math.cos(t), radius * r * math.sin(t)


# Materials and Environment
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.0561691, 0.0267681, 0.722677, 1)
bpy.ops.object.select_by_type(extend=False, type='MESH')
bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[0].default_value = (0.770442, 0.731745, 0.8, 1)
bpy.ops.object.select_all(action='DESELECT')

point_list = [["index", "image", "x", "y"]]


for i in range(15000):
    #bpy.data.objects["Dart"].select_set(True)
    #obj = bpy.data.objects.get("Dart")

    # Calulate random points
    dx, dy = get_rand_circle_points(100)
    rx, ry, rz = uniform(0, 4), uniform(0, 0.7), uniform(0, 4)

    # Set Dart Location
    bpy.context.object.location = [dx, dy, 0]
    bpy.context.object.rotation_euler = [rx, ry, rz]
    
    
    
    # Move Sun
    """
    bpy.data.objects["Dart"].select_set(False)
    bpy.data.objects["Sun"].select_set(True)

    obj = bpy.data.objects.get("Sun")
    dx, dy = uniform(-50, 50), uniform(-50, 50)
    bpy.context.object.location = [dx, dy, 0]

    bpy.data.objects["Sun"].select_set(False)
    """
    

    # Camera view pixel coordinates of dart point (xy)
    co_2d = bpy_extras.object_utils.world_to_camera_view(scene, D.objects["Camera"], obj.location)
    render_scale = scene.render.resolution_percentage / 100
    render_size = (int(scene.render.resolution_x * render_scale),
                   int(scene.render.resolution_y * render_scale))

    u, v = round(co_2d.x * render_size[0]), round(co_2d.y * render_size[1])
    x, y = u, render_size[1] - v
    print("Pixel Coords (x, y) :", x, y)

    # Render
    file_name = f"rand_dart{i}"
    bpy.context.scene.render.filepath = f"C:\\python\\FlightVision\\blender\\batch1\\{file_name}"
    bpy.ops.render.render(write_still=True)
    
    point_list.append([i, file_name+'.jpg', x, y])



csv_path = r"C:\python\FlightVision\blender\batch1.csv"
             
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerows(point_list)