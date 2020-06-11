#BC iJet Lab's Rhino Unreal Engine Import Plugin
import unreal

#Path of Rhino File
rhino_file_path = "C:\\Users\\ijet\\Desktop\\Rhino_Files\\h-22 tropics materialized.3dm"

#Check to make sure the file exists
if not (unreal.Paths.file_exists(rhino_file_path)):
    print "File Does Not Exist"
    quit()
    
#Initializing Datasmith Element
datasmith_file = unreal.DatasmithSceneElement.construct_datasmith_scene_from_file(rhino_file_path)

if datasmith_file is None:
    print "Failed to Load Rhino File as Datasmith Element"
    quit()

#Set Import Options for Datasmith Scene
import_options = datasmith_file.get_options()
#Create min and max for lightmap. This will be a scroll down option in UI.
#Larger Geometry should be atleast in the lightmap bounds of [512,1024]
light_map_min = unreal.DatasmithImportLightmapMin.LIGHTMAP_512
light_map_max = unreal.DatasmithImportLightmapMax.LIGHTMAP_1024
#Create Base Options
#scene_handling = (level the scene should be imported to)
#include_geomtry = (bool of whether meshes should be included)
#include_material = (bool of whether materials should be included) does this work with vray? FIX THIS
#include_light,camera,and animation all set to false as they do not pertain to this project
#asset_options = [] because there are no fields in this object
#static_mesh_options=[minLightMap,maxLightMap,generateLightMap-bool,removeDegenerates-bool]
import_options.base_options = unreal.DatasmithImportBaseOptions(scene_handling=unreal.DatasmithImportScene.NEW_LEVEL, 
                                                    include_geometry=True, 
                                                    include_material=False, 
                                                    include_light=False, 
                                                    include_camera=False, 
                                                    include_animation=False, 
                                                    asset_options=[], 
                                                    static_mesh_options=[light_map_min, light_map_max, True, True])

#tesselation_options may no be necessary as they are the same as the default ones
tesselation_options = unreal.DatasmithTessellationOptions(chord_tolerance=0.2,
                                                        max_edge_length=0,
                                                        normal_tolerance=20,
                                                        stitching_technique=unreal.DatasmithCADStitchingTechnique.STITCHING_SEW)

#In Game Destination Folder
destination_folder = "/Game/NewRhinoFile2"  
#Imported Datasmith Scene 
imported_scene = datasmith_file.import_scene(destination_folder)


if not imported_scene.import_succeed:
    print("Import Failed")
    quit()

#FLIP NORMALS looks like the solution would be to set everything to have a two sided material
#Two sided materials MAY produce artifacts under static lighting!
#Material settings -> double sided this is the first attempt fix.
# i believe the type is Static Mesh Actor, can confirm once we compile with unreal
# static_meshes = imported_scene.imported_meshes

# for sm in static_meshes:
#     sm.
#     # sm.static_mesh_component #this gets the StaticMeshComponent object from the StaticMeshActor
#     # unreal.Material.two_sided = True this is the expression! 
#     # link it to the static mesh