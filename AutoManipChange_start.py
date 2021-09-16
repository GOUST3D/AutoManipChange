import maya.cmds as cmds
import maya.mel as mel


class AutoManipChange():
    def __init__(self):
        selected = cmds.ls(sl=True)[0]
        print "sucka"
        if cmds.getAttr(str(selected)+".showManipDefault") == 1:
            mel.eval("MoveTool;")
            return
        if cmds.getAttr(str(selected)+".showManipDefault") == 2:
            mel.eval("RotateTool;")
            return
        if cmds.getAttr(str(selected)+".showManipDefault") == 3:
            mel.eval("ScaleTool;")
            return

AutoManipChangeScriptJob = cmds.scriptJob( ct= ["SelectionChanged","AutoManipChange()"], protected=True, kws=True)
