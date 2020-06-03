#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal
#Path of Rhino File
rhino_file_path = "C:\Users\ijet\Desktop\Rhino_Files\405 CQ Website File.3dm"
#Initializing Datasmith Element
datasmith_file = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(rhino_file_path)

if datasmith_file == None:
    print "Failed to Load Rhino File as Datasmith Element"
    quit()
#load the meshes, if you get a null static mesh add it to a list ot remove or directly remove it

parts_list = datasmith_file.get_all_mesh_actors()
print parts_list