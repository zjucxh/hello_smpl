import os
import bpy
import numpy as np

def create_smpl():
    bpy.data.window_managers["WinMan"].smplx_tool.smplx_gender = 'female'
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.scene.smplx_add_gender()
    bpy.ops.object.smplx_snap_ground_plane()

# sample cmu data, copy all 0x_01.npz to cmu_mini folder
def sample_cmu():
    cmu_dir = "/home/cxh/mnt/cxh/Documents/dataset/CMU"
    cmu_mini_dir = "/home/cxh/mnt/cxh/Documents/dataset/CMU_mini"
    for root, dirs, files in os.walk(cmu_dir):
        for file in files:
            if file.endswith(".npz") and '_01' in file:
                npz_file = os.path.join(root, file)
                print(f'copying {npz_file}')
                os.system(f'cp {npz_file} {cmu_mini_dir}')


def load_cmu(cmu_dir="/home/cxh/mnt/cxh/Documents/dataset/CMU_mini"):
    for root, dirs, files in os.walk(cmu_dir):
        for file in files:
            if file.endswith(".npz") and not file.startswith('neutral'):
                print(f' dirs : {dirs}')
                print(f' root : {root}')
                print(f' file : {file}')
                out_dir = os.path.join('/home/cxh/mnt/cxh/Documents/dataset/CMU_simulation/',file[:-4])
                print(f' out_dir : {out_dir}')
                npz_file = os.path.join(root, file)
                
                # Comment out the following line to run blender in background mode to avoid memory leak
                bpy.ops.wm.read_homefile(filepath='assets/factory.blend')

                #bpy.ops.object.delete()
                print(f'loading {npz_file}')
                # Scale up avatar 40 times for better cloth simulation results

                bpy.ops.object.smplx_add_animation(filepath=os.path.join(root, file))
                #for object in bpy.data.collections["Collection"].all_objects:
                    #object.scale = (40,40,40)
                for object in bpy.context.scene.objects:
                    print(f' object name : {object.name}')
                    # if object name start from SMPLX-female or SMPLX-male, then scale it
                    if object.name.startswith('SMPLX-female') or object.name.startswith('SMPLX-male'):
                        object.scale = (40,40,40)
                #bpy.ops.object.select_all(action='SELECT')
                for obj in bpy.context.scene.objects:
                    print(f' obj type : {obj.type}')
                    if obj.type == 'MESH':
                        # Add collision modifier
                        obj.select_set(True)
                        bpy.ops.object.modifier_add(type='COLLISION')
                        obj.select_set(False)

                # Add garment template
                bpy.ops.wm.obj_import(filepath='assets/template.obj')

                # Add cloth simulation
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects['tshirt'].select_set(True)
                # Add cloth and collision modifier
                bpy.ops.object.modifier_add(type='CLOTH')
                bpy.ops.object.modifier_add(type='COLLISION')
                # Set cloth simulation properties
                bpy.context.object.modifiers["Cloth"].collision_settings.collision_quality = 8


                # export obj file sequences
                #bpy.context.scene.frame_start = 1
                #bpy.context.scene.frame_end = 250
                #bpy.context.scene.frame_step = 1
                #bpy.context.scene.frame_current = 1
                #bpy.context.scene.frame_set(1)
                bpy.ops.object.select_all(action='DESELECT')
                bpy.data.objects['tshirt'].select_set(True)
                # Export obj file sequences
                # If export_selected_objects is False, avatar will be exported as well
                bpy.ops.wm.obj_export(filepath=os.path.join(out_dir,'tshirt.obj'), export_animation=True,start_frame=1,end_frame=250,export_selected_objects=True,export_materials=False)
                

                


if __name__ == "__main__":
    print(f' .....')
    load_cmu() 