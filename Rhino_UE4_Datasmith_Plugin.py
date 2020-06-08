#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal

#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\test2.3dm"

#Check to make sure the file exists
if not (unreal.Paths.file_exists(rhino_file_path)):
    print "File Does Not Exist"
    quit()
    
#Initializing Datasmith Element
datasmith_file = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(rhino_file_path)

if datasmith_file is None:
    print "Failed to Load Rhino File as Datasmith Element"
    quit()

#load the meshes, if you get a null static mesh add it to a list ot remove or directly remove it
#good way to describe process: import data, delete small objectds and null static meshes,
#build lvl of detail and lighting conditions
#merge objects (stiching and tesselation and such)
#materialize objects (S.T. extra data from rhino team)
#export as asset! 
#create a new folder in the content folder for everything
#thinking we have to load the scene first before accessing meshes and stuff


#build import settings then test import! 
import_options = datasmith_file.get_options()

import_options.base_options = unreal.DatasmithImportBaseOptions(scene_handling=unreal.DatasmithImportScene.CURRENT_LEVEL, 
                                                    include_geometry=True, 
                                                    include_material=False, 
                                                    include_light=False, 
                                                    include_camera=False, 
                                                    include_animation=False, 
                                                    asset_options=[], 
                                                    static_mesh_options=[unreal.DatasmithImportLightmapMin.LIGHTMAP_128, unreal.DatasmithImportLightmapMax.LIGHTMAP_512, True, True])
                                                    #static_mesh_options=[minLightMap,maxLightMap,generateLightMap-bool,removeDegenerates-bool]
tesselation_options = unreal.DatasmithTessellationOptions(chord_tolerance=0.2,
                                                        max_edge_length=0,
                                                        normal_tolerance=20,
                                                        stiching_technique=unreal.DatasmithCADStichingTechnique.STICHING_SEW)


print(import_options.tesselation_options)

# destination_folder = "/Game/NewRhinoFile"
# result = datasmith_file.import_scene(destination_folder)

#merge actors? 
#implement LOD
if not result.import_succeed:
    print("Import Failed")
    quit()

#DESTROY AT END