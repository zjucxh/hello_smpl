# hello_smpl
SMPLX model demo

## Note
SMPLX pose dimension: (165,)
Add animation : bpy.ops.object.smplx_add_animation(filepath="/home/cxh/mnt/cxh/Documents/dataset/CMU/06/06_03_stageii.npz")
Modified smpl blender plugin __init__.py in blender script folder
- All gender has been changed to female
- translation set to 0

For ERROR: No key block for Shape010, 011, 012, ..., 015:
Dimension of Legacy version of SMPL is 10 not 15, so error can be ignored.
when read factory.blend blender should run in background otherwise error occurs
## Install

Add smpl_blender addon 
Add blender to PATH
Modify blender python  path 
run blender -P smpl_blender.py  
to run in background add -b option


