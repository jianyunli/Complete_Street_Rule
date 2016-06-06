'''
Created on May 24, 2016

@author: Tanvi
'''
from scripting import *

# get a CityEngine instance
ce = CE()

outputFolder = "\\BatchExport\\"
generateBoolean = False
deleteBoolean = False
collectTexturesBoolean = False
vertexNormals = "SET_MISSING"
centerLocation=[0.0,0.0,0.0]



# Turn off User Interface updates, or script might take forever.
@noUIupdate
def main(outputFolder):
    # This function will export in batch web scenes to the input outputFolder
    layers = ce.getObjectsFrom(ce.scene, ce.isLayer)
    print("There are " + str(len(layers)) + " layers in the current scene.")
    counter = 0
    for layer in layers:
        try:
            ce.setSelection(layer)
            OID = ce.getOID(layer)
            layerName = ce.getName(layer)
            if generateBoolean:
                # generate models on selected shapes (assumes size of file is too big)
                ce.generateModels(ce.selection())
                ce.waitForUIIdle()
            print ("Setting export settings for layer named: " + str(layerName))
            exportSettings = FBXExportModelSettings()
            exportSettings.setCollectTextures(collectTexturesBoolean)            
            exportSettings.setVertexNormals(vertexNormals)
            #exportSettings.setGlobalOffset(centerLocation)
            exportSettings.setOutputPath(ce.toFSPath("models") + str(outputFolder))
            exportSettings.setBaseName(layerName)
            ce.export(ce.selection()[0], exportSettings)
            print ("Exported layer named: " + str(layerName) + "to models/BatchExport3WS")
            counter += 1
            if deleteBoolean:
                ce.delete(ce.selection())
                pass
            print "Exported web scene for layer named:" + str(layerName)
            # Change this to an absolute path that points to your KML files.
        except:
            print "Could not execute on counter " + str(counter)
            counter += 1
            pass


# Call
if __name__ == '__main__':
    print("Batch Layer script started.")
    main(outputFolder)
    print("Script completed.")
