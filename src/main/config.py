import platform

# NFT configurations:
nftsPerBatch = 4   # Number of NFTs per batch
renderBatch = 1     # The batch number to render in PNG-Generator
imageName = "ThisCozyPlace_"    # The name of the NFT image produces by PNG-Generator
fileFormat = 'JPEG' # Dictate the image extension when Blender renders the images
# Visit https://docs.blender.org/api/current/bpy.types.Image.html#bpy.types.Image.file_format
# for a list of file formats supported by Blender. Enter the file extension exactly as specified in
# the Blender API documentation above.

# The path to Blend_My_NFTs folder:
save_path_mac = '/Users/torrinleonard/Desktop/Blend_My_NFTs'
save_path_windows = r''
# Example mac: /Users/Path/to/Blend_My_NFTs
# Example windows: C:\Users\Path\to\Blend_My_NFTs

enableMaxNFTs = False  # Turn on the maximum number of NFTs, use this to limit the number of DNA sent to NFTRecord, and subsequent batches
maxNFTs = 100    # The maximum number of NFTs you want to generate - doesn't do anything yet

resetViewport = True # If True: turns all viewport and render cameras on after Image_Generator is finished operations

# 3D model imports and exports variables:
use3DModels = True # Set to True if using external models as attributes instead of Blender objects
# ^Does not work with colour options and rarity, both must be turned off in order to use this.

# Object colour options:
generateColors = False # When set to true this applies the sets of colors listed below to the objects in the collections named below

# The collections below are RGBA Color values. You can put as many or as little color values in these lists as you would like.
# You can create any number of rgbaColorLists and assign them to any number of collections that you would like.
# Each set of rgbaColorList1 assigned to an object by collection name in the colorList will act like an attribute and create a unique variant of that item.
rgbaColorList1 = [(1,0,0,1),(0,1,0,1),(0,0,1,1),(1,1,1,1),(.5,0,0,1)] 
rgbaColorList2 = [(1,1,0,1),(0,1,1,1),(.5,0,1,1),(.5,1,1,1),(0,.5,0,1)]
# The following color list can be as long or as short as you want it to be.
# To use this all you need to do is place the name of the collection you want colored in the "" and the set of colors you want to apply to it after the :
# The collection named can only contain objects and not sub collections. Every object in the collection will be set to the colors you assigned above for each attribute
colorList = {"Sphere_1_0":rgbaColorList1,"CurveA_1_0":rgbaColorList2}

# Utilities - DO NOT TOUCH:
mac = 'Darwin'  # Mac OS
windows = 'Windows'  # Windows
slash = ''  # Leave empty
save_path = None  # Leave empty

# Save_path utilities and os compatibility
if platform.system() == mac:
    save_path = save_path_mac
    slash = '/'
elif platform.system() == windows:
    save_path = save_path_windows
    slash = '\\'

# Paths to folders
batch_save_path = save_path + slash + 'Batch_Json_files' # The output path for batches genreated by Batch_Sorter.py
images_save_path = save_path + slash + 'NFT_Image_Output' # The output path for images generated by Image_Generator.py
modelAssetPath = save_path + slash + "3D_Model_Input" # The input path for 3D models
model_save_path = save_path + slash + "3D_Model_Output" # The output path for 3D models generated by Model_Generator.py

# PLEASE NOTE - The only file format that is supported for imports/exports is .glb
objectFormatImport = 'gltf'  # The file format of the objects you would like to import
objectFormatExport = 'gltf'  # The file format of the objects you would like to export


# FEATURES THAT ARE EXPERIMENTAL AND/OR DO NOT WORK YET:
# Specify the XYZ location for objects imported as external files:
locationObjectAttribute = {
    "Cone": {"x": 0, "y": 0, "z": 0},
    "Cube": {"x": 0, "y": 0, "z": 0}
}

enableRarity = False
# True = include weighted rarity percentages in NFTRecord.json calculations,
# False = Pure random selection of variants


