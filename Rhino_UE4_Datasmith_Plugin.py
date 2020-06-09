#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal

#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\test.3dm"
#two sided materials? 
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
#implementing a setting that allows you to edit the min and max lightmap in the UI is important.
#this is because super large objects will have overlapping UV's if it isn't large
#super small objects will not have overlapping UVs even with a 64, so by looking at the number of meshes you can change that.
#can we catch an overlapping UV's error and improve on it later in the script? ie: you see that the UV's are overlapping at (128,512)
#then you loop through the meshes and bump it up? then rebuild
#build import settings then test import! 
import_options = datasmith_file.get_options()
light_map_min = unreal.DatasmithImportLightmapMin.LIGHTMAP_512
light_map_max = unreal.DatasmithImportLightmapMax.LIGHTMAP_1024
import_options.base_options = unreal.DatasmithImportBaseOptions(scene_handling=unreal.DatasmithImportScene.CURRENT_LEVEL, 
                                                    include_geometry=True, 
                                                    include_material=False, 
                                                    include_light=False, 
                                                    include_camera=False, 
                                                    include_animation=False, 
                                                    asset_options=[], 
                                                    static_mesh_options=[light_map_min, light_map_max, True, True])
                                                    #static_mesh_options=[minLightMap,maxLightMap,generateLightMap-bool,removeDegenerates-bool]
tesselation_options = unreal.DatasmithTessellationOptions(chord_tolerance=0.2,
                                                        max_edge_length=0,
                                                        normal_tolerance=20,
                                                        stitching_technique=unreal.DatasmithCADStitchingTechnique.STITCHING_SEW)


destination_folder = "/Game/NewRhinoFile2"   
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