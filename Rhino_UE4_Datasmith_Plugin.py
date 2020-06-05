#we may have to consider using a udatasmith function or "reimport" after using datsmith
#then it would be just an optimization tool not an import plugin
#BC iJet Lab's Rhino Unreal Engine Import Plugin



import unreal

#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\test.3dm"

#Check to make sure the file exists
if not (unreal.Paths.file_exists(rhino_file_path)):
    print "File Does Not Exist"
    quit()
    
#let folder name be an input in UI 
#print unreal.Paths.file_exists(import_folder)

#Initializing Datasmith Element
#i feel like it isnt working because the cad importer plugin isnt enabled in this action
#like normally we would have the cad plugin enabled AND datasmith enabled
#maybe that is why it isnt reading the file
datasmith_file = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(rhino_file_path)

if datasmith_file is None:
    print "Failed to Load Rhino File as Datasmith Element"
    quit()

print(datasmith_file.get_all_mesh_actors())
#i think there example is outdated, we will have to import first before handling any meshes

#load the meshes, if you get a null static mesh add it to a list ot remove or directly remove it
#good way to describe process: import data, delete small objectds and null static meshes,
#build lvl of detail and lighting conditions
#merge objects (stiching and tesselation and such)
#materialize objects (S.T. extra data from rhino team)
#export as asset! 
#create a new folder in the content folder for everything
#thinking we have to load the scene first before accessing meshes and stuff

import_base_options = unreal.DatasmithImportBaseOptions(scene_handling=unreal.DatasmithImportScene.CURRENT_LEVEL, 
                                                    include_geometry=True, 
                                                    include_material=False, 
                                                    include_light=False, 
                                                    include_camera=False, 
                                                    include_animation=False, 
                                                    asset_options=[], 
                                                    static_mesh_options=[unreal.DatasmithImportLightmapMin.LIGHTMAP_128, unreal.DatasmithImportLightmapMax.LIGHTMAP_512, True, True])

import_options = datasmith_file.get_options()

import_options.base_options = import_base_options

# destination_folder = "C:\\Users\\ijet\\Documents\\Unreal Projects\\RhinoUnrealTest\\Content\\RhinoAsset2"
# destination_folder = "C:\\Users"
# print(unreal.Paths.validate_path(destination_folder))
# result = datasmith_file.import_scene("C:/Users/ijet/Documents/Unreal Projects/RhinoUnrealTest/Content/RhinoAsset2")

# if result.import_succeed:
    # print("import succeeded")
# else:
    # print("import failed")
