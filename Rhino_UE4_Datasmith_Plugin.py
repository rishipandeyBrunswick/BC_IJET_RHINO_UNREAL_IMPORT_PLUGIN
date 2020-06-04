#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal
#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\test.3dm"
#Initializing Datasmith Element
datasmith_file = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(rhino_file_path)

if datasmith_file is None:
    print "Failed to Load Rhino File as Datasmith Element"
    quit()
else: 
    print "file loading successful" 

#load the meshes, if you get a null static mesh add it to a list ot remove or directly remove it
#good way to describe process: import data, delete small objectds and null static meshes,
#build lvl of detail and lighting conditions
#merge objects (stiching and tesselation and such)
#materialize objects (S.T. extra data from rhino team)
#export as asset! 

mesh_list = datasmith_file.get_all_mesh_actors()

print mesh_list
