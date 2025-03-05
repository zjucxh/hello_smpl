import numpy as np
import os
import trimesh

def generate_dataset():
    # CMU_mini pose file directory
    mount_dir = '/home/cxh/mnt/cxh/'
    pose_dir = 'Documents/dataset/CMU_mini'
    obj_dir = 'Documents/dataset/CMU_mini_simulation'
    pose_dir = os.path.join(mount_dir, pose_dir)
    obj_dir = os.path.join(mount_dir, obj_dir)
    # walk through all the files in the directory
    for root, dirs, files in os.walk(pose_dir):
        print(f' root : {root}')
        print(f' files : {files}')
        # npz file
        for file in files:
            clo_dir =  file[:-4]
            obj_path = os.path.join(obj_dir, clo_dir)
            npz_file = os.path.join(root, file)
            print(f' npz_file : {npz_file}')
            print(f' root: {root}')
            with np.load(npz_file) as data:
                #print(f' data keys : {data.keys()}')
                gender = "female"
                betas = data["betas"]
                poses = data["poses"][:130]
                print(f' poses shape : {poses.shape}')
                
            # Load obj mesh files
            vertex_seq = []
            face_seq = []
            for i in range(121,251):
                obj_file = os.path.join(obj_path, f'tshirt{i:04}.obj')
                # load obj file via trimesh
                mesh = trimesh.load_mesh(obj_file, file_type='obj')
                vertices = np.array(mesh.vertices,dtype=np.float32)
                #print(f' vertices : {vertices}')
                vertex_seq.append(vertices)
                face_seq.append(mesh.faces)
            face_seq = np.array(mesh.faces, dtype=np.int32)
            vertex_seq = np.array(vertex_seq, dtype=np.float32) 
            print(f' mesh_sequence shape : {vertex_seq.shape}')
            print(f' face_sequence shape : {face_seq.shape}')
            # write gender, beta, poses mesh vertex sequences, faces to file
            out_file = npz_file[:-4] + ".seq"
            out_data = {'gender':gender, 'betas':betas, 'poses':poses,
                        'vertex_seq':vertex_seq, 'face_seq':face_seq}
            np.savez(out_file, **out_data)


if __name__ == "__main__":
    #generate_dataset()
    data_dir = '/home/cxh/mnt/cxh/Documents/dataset/CMU_mini_dataset'
    # walk through all the files in the directory
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            file_path = os.path.join(root, file)
            print(f' file path : {file_path}')
            data = np.load(file_path)
            print(f' data : {data}')
            gender = data['gender']
            betas = data['betas']
            poses = data['poses']
            vertex_seq = data['vertex_seq']
            face_seq = data['face_seq'] 
            print(f' gender : {gender}')
            print(f' betas : {betas}')
            print(f' poses : {poses.shape}')
            print(f' vertex_seq : {vertex_seq.shape}')
            print(f' face_seq : {face_seq.shape}')