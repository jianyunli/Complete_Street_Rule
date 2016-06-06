'''
Created on May 10, 2016

@author: Tanvi
'''

from scripting import *

# get a CityEngine instance
ce = CE() 
# Declare variables
outputFolder = "/BatchExport/"
width = 1920
height = 1080
fileType = ".png"
generateBoolean = False
deleteBoolean = False


# Turn off User Interface updates, or script might take forever.
# @noUIupdate
def turnLayersInvisible(layersList):
    print("Turning off visibility for all layers.")
    for layer in layersList:
        layer.setVisible(False)


def main():
    # This function will export in batch images to the input outputFolder suggested resolution and file type can also be
    # declared.
    layers = ce.getObjectsFrom(ce.scene, ce.isLayer)
    print(
        "There are " + str(len(layers) - 2) + " layers in the current scene.")  # -2 To remove Panorama and Scene Light
    counter = 0
    # Turns off visibility of all layers.
    turnLayersInvisible(layers)
    print("Iterating through all layers")
    for layer in layers:
        try:
            layerName = str(ce.getName(layer))
            if layerName == "Panorama" or layerName == "Scene Light":
                continue  # skip
            # print layer.getVisible()
            layer.setVisible(False)
            # print layer.getVisible()
            layer.setVisible(True)
            layerView = ce.getObjectsFrom(ce.get3DViews(), ce.isViewport)
            if len(layerView) < 1:
                counter += 1
                print "No Views found on object number " + str(counter)
            else:
                ce.waitForUIIdle()
                ce.setSelection(layer)
                if generateBoolean:
                    # generate models on selected shapes (assumes size of file is too big)
                    ce.generateModels(ce.selection())
                    ce.waitForUIIdle()
                layerView[0].snapshot(ce.toFSPath("images") + outputFolder + str(layerName) + fileType, width, height)
                counter += 1
                print "Exported snapshot for layer named:" + str(layerName)

            layer.setVisible(False)
            # After Snap Shots are retrieved delete the selection, memory management
            if deleteBoolean:
                ce.delete(ce.selection())
                pass
        except:
            print "Could not execute on counter " + str(counter)
            counter += 1
            pass
            # Change this to an absolute path that points to your KML files.


# Call
if __name__ == '__main__':
    print("Batch Layer script started.")
    main()
    print("Script completed.")