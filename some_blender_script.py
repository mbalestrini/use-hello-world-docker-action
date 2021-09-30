import bpy
import os


D = bpy.data
C = bpy.context

filename = "./render_test.jpg"

def executeRender(filename, render) : 
    render.image_settings.file_format = 'JPEG' #'PNG'
    render.use_file_extension
    render.resolution_percentage = 0.25
    render.use_file_extension = True
    render.filepath = filename

    print("Rendering "+filename + " ...")
    bpy.ops.render.render(write_still=True, use_viewport=False)


executeRender(filename, C.scene.render)
