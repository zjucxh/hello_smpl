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
    #rest_pose = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11167845129966736, 0.04289207234978676, -0.41644084453582764, 0.10881128907203674, -0.06598565727472305, -0.756219744682312, -0.0963931530714035, -0.09091583639383316, -0.18845966458320618, -0.11809506267309189, 0.050943851470947266, -0.5295845866203308, -0.14369848370552063, 0.055241718888282776, -0.704857349395752, -0.019182899966835976, -0.0923367589712143, -0.3379131853580475, -0.45703303813934326, -0.1962839663028717, -0.6254575848579407, -0.21465237438678741, -0.06599827855825424, -0.5068942308425903, -0.36972442269325256, -0.0603446289896965, -0.07949023693799973, -0.14186954498291016, -0.08585254102945328, -0.6355276107788086, -0.3033415675163269, -0.05788097903132439, -0.6313892006874084, -0.17612087726593018, -0.13209305703639984, -0.3733545243740082, 0.850964367389679, 0.2769227623939514, -0.09154807031154633, -0.4998386800289154, 0.026556432247161865, 0.052880801260471344, 0.5355585217475891, 0.045960985124111176, -0.27735769748687744, 0.11167845129966736, -0.04289207234978676, 0.41644084453582764, 0.10881128907203674, 0.06598565727472305, 0.756219744682312, -0.0963931530714035, 0.09091583639383316, 0.18845966458320618, -0.11809506267309189, -0.050943851470947266, 0.5295845866203308, -0.14369848370552063, -0.055241718888282776, 0.704857349395752, -0.019182899966835976, 0.0923367589712143, 0.3379131853580475, -0.45703303813934326, 0.1962839663028717, 0.6254575848579407, -0.21465237438678741, 0.06599827855825424, 0.5068942308425903, -0.36972442269325256, 0.0603446289896965, 0.07949023693799973, -0.14186954498291016, 0.08585254102945328, 0.6355276107788086, -0.3033415675163269, 0.05788097903132439, 0.6313892006874084, -0.17612087726593018, 0.13209305703639984, 0.3733545243740082, 0.850964367389679, -0.2769227623939514, 0.09154807031154633, -0.4998386800289154, -0.026556432247161865, -0.052880801260471344, 0.5355585217475891, -0.045960985124111176, 0.27735769748687744])
    #np.save('assets/rest_pose.npy', rest_pose)
    #pose = np.load('assets/rest_pose.npy')
    #print(f'rest_pose: {pose - rest_pose}')
    #sample_cmu()
    print(f' .....')
    load_cmu() 