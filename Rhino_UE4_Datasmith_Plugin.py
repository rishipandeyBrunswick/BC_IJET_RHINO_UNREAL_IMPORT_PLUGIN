#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal

#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\test.3dm"

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

#take out vray floor

#build import settings then test import! 
import_options = datasmith_file.get_options()
import_options.base_options = unreal.DatasmithImportBaseOptions(scene_handling=unreal.DatasmithImportScene.CURRENT_LEVEL, 
                                                    include_geometry=True, 
                                                    include_material=False, 
                                                    include_light=False, 
                                                    include_camera=False, 
                                                    include_animation=False, 
                                                    asset_options=[], 
                                                    static_mesh_options=[unreal.DatasmithImportLightmapMin.LIGHTMAP_256, unreal.DatasmithImportLightmapMax.LIGHTMAP_512, True, True])
                                                    #static_mesh_options=[minLightMap,maxLightMap,generateLightMap-bool,removeDegenerates-bool]
tesselation_options = unreal.DatasmithTessellationOptions(chord_tolerance=0.2,
                                                        max_edge_length=0,
                                                        normal_tolerance=20,
                                                        stitching_technique=unreal.DatasmithCADStitchingTechnique.STITCHING_SEW)


destination_folder = "/Game/NewRhinoFile"
imported_scene = datasmith_file.import_scene(destination_folder)

if not imported_scene.import_succeed:
    print("Import Failed")
    quit()
#work on optimizations now! 

# print("LIST OF IMPORTED STATIC MESHES")
#this works to access all static meshes
# print(imported_scene.imported_meshes)
# static_meshes = imported_scene.imported_meshes
#flip normals, merge, lod
#uses default tesselation already! or pulls from above maybe, but either way it works