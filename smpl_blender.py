import os
import bpy
import numpy as np
import pickle as pkl

def create_smpl():
    bpy.data.window_managers["WinMan"].smplx_tool.smplx_gender = 'female'
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.scene.smplx_add_gender()
    bpy.ops.object.smplx_snap_ground_plane()



def load_cmu(cmu_dir="/home/cxh/mnt/cxh/Documents/dataset/BMLrub"):
    for root, dirs, files in os.walk(cmu_dir):
        for file in files:
            if file.endswith(".npz") and not file.startswith('neutral'):

                npz_file = os.path.join(root, file)
                # Delect all objects
                #bpy.ops.object.select_all(action='SELECT')
                #bpy.ops.object.delete(use_global=True)
                #bpy.ops.wm.read_factory_settings()
                bpy.ops.wm.read_homefile(filepath='assets/factory.blend')

                #bpy.ops.object.delete()
                print(f'loading {npz_file}')
                bpy.ops.object.smplx_add_animation(filepath=os.path.join(root, file))


if __name__ == "__main__":

    load_cmu() 