import bpy
import numpy as np
import pickle as pkl

def create_smpl():
    bpy.data.window_managers["WinMan"].smplx_tool.smplx_gender = 'female'
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.scene.smplx_add_gender()
    bpy.ops.object.smplx_snap_ground_plane()

#bpy.ops.object.select_all(action='DESELECT')
#bpy.ops.object.smplx_set_poseshapes()
#bpy.ops.object.smplx_set_handpose()
#bpy.ops.scene.smplx_add_gender()
#bpy.ops.object.editmode_toggle()
#bpy.ops.object.editmode_toggle()
#bpy.ops.object.smplx_update_joint_locations()
#bpy.ops.object.smplx_add_animation(filepath="/home/cxh/mnt/cxh/Documents/dataset/CMU/02/02_05_stageii.npz")


def load_animation(filepath:str="/home/cxh/mnt/cxh/Documents/dataset/CMU/01/01_02_stageii.npz"):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.smplx_set_poseshapes()
    bpy.ops.object.smplx_set_handpose()
    bpy.ops.scene.smplx_add_gender()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.smplx_update_joint_locations()
    bpy.ops.object.smplx_add_animation(filepath=filepath)
    #bpy.ops.screen.animation_play() 
    #frame_end = bpy.context.scene.frame_end
    #for frame in range(frame_end):
    #    bpy.context.scene.frame_set(frame)
    #    bpy.ops.object.smplx_update_joint_locations()
    #    bpy.ops.object.smplx_set_poseshapes()

def load_cmu(filepath:str="/home/cxh/mnt/cxh/Documents/dataset/CMU/01/01_02_stageii.npz"):
    cmu = np.load(filepath, allow_pickle=True)
    for e in cmu.keys():
        print(f'key : {e} ')
    gender = cmu['gender']
    surface_model_type = cmu['surface_model_type']
    mocap_frame_rate = cmu['mocap_frame_rate']
    mocap_time_length = cmu['mocap_time_length']
    markers_latent = cmu['markers_latent']
    latent_labels = cmu['latent_labels']
    markers_latent_vids = cmu['markers_latent_vids']
    trans = cmu['trans']
    poses = cmu['poses']
    # save pose as pickle
    with open('poses.pkl', 'wb') as f:
        pkl.dump(poses[0], f,encoding='latin1')
        pkl.dump(obj=poses[0],)
    print(f' trans : {trans.shape}')
    print(f' pose shape : {poses.shape}')
    betas = cmu['betas']
    print(f' betas shape : {betas.shape}')
    root_orient = cmu['root_orient']
    pose_body = cmu['pose_body']
    pose_jaw = cmu['pose_jaw']
    pose_eye = cmu['pose_eye']
    # modify gender as female

def pose_shape():
    pose = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.11167845129966736, 0.04289207234978676, -0.41644084453582764, 0.10881128907203674, -0.06598565727472305, -0.756219744682312, -0.0963931530714035, -0.09091583639383316, -0.18845966458320618, -0.11809506267309189, 0.050943851470947266, -0.5295845866203308, -0.14369848370552063, 0.055241718888282776, -0.704857349395752, -0.019182899966835976, -0.0923367589712143, -0.3379131853580475, -0.45703303813934326, -0.1962839663028717, -0.6254575848579407, -0.21465237438678741, -0.06599827855825424, -0.5068942308425903, -0.36972442269325256, -0.0603446289896965, -0.07949023693799973, -0.14186954498291016, -0.08585254102945328, -0.6355276107788086, -0.3033415675163269, -0.05788097903132439, -0.6313892006874084, -0.17612087726593018, -0.13209305703639984, -0.3733545243740082, 0.850964367389679, 0.2769227623939514, -0.09154807031154633, -0.4998386800289154, 0.026556432247161865, 0.052880801260471344, 0.5355585217475891, 0.045960985124111176, -0.27735769748687744, 0.11167845129966736, -0.04289207234978676, 0.41644084453582764, 0.10881128907203674, 0.06598565727472305, 0.756219744682312, -0.0963931530714035, 0.09091583639383316, 0.18845966458320618, -0.11809506267309189, -0.050943851470947266, 0.5295845866203308, -0.14369848370552063, -0.055241718888282776, 0.704857349395752, -0.019182899966835976, 0.0923367589712143, 0.3379131853580475, -0.45703303813934326, 0.1962839663028717, 0.6254575848579407, -0.21465237438678741, 0.06599827855825424, 0.5068942308425903, -0.36972442269325256, 0.0603446289896965, 0.07949023693799973, -0.14186954498291016, 0.08585254102945328, 0.6355276107788086, -0.3033415675163269, 0.05788097903132439, 0.6313892006874084, -0.17612087726593018, 0.13209305703639984, 0.3733545243740082, 0.850964367389679, -0.2769227623939514, 0.09154807031154633, -0.4998386800289154, -0.026556432247161865, -0.052880801260471344, 0.5355585217475891, -0.045960985124111176, 0.27735769748687744]
    pose = np.array(pose)
    print(' pose shape : {0}'.format(pose.shape))

if __name__ == "__main__":
    #create_smpl()
    #load_animation()
    #load_cmu()
    #pose_shape()
    # load pkl
    #with open('poses.pkl', 'rb') as f:
    #    pose = pkl.load(f)
    #print(f' pose shape : {pose}')
    bpy.ops.object.smplx_add_animation(filepath="/home/cxh/mnt/cxh/Documents/dataset/CMU/06/06_03_stageii.npz")
    frame_end = bpy.context.scene.frame_end
    for frame in range(frame_end):
        bpy.context.scene.frame_set(frame)
        bpy.ops.object.smplx_update_joint_locations()
        bpy.ops.object.smplx_set_poseshapes()