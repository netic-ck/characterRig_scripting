__author__ = 'Ernesto Ruiz Velasco'
__script__ = 'setupRigUI.py'

'''
This script contains procedures that crate a setup UI for all the scripts that create a biped rig.
Based in the book "MEL Scripting a Character Rig in Maya 2008"
'''

#    checkCharName()
#    setCharName()
#    setNamespace()
#    setupRigUI()

import maya.cmds as cmds

def checkCharName(*args):
    '''
    This function finds the name of the character
    '''
    pass


def setCharName(*args):
    '''
    This function sets the name of the character
    '''
    pass


def setNamespace(*args):
    '''
    This function sets the a namespace for the character
    '''
    pass


def setupRigUI(*args):
    '''
    This function launches the SetupRigUI
    '''

    #Declare unique UI strings
    defaultPath = 'C:/CMaraffi_bookFiles/'
    name_win = 'cRig_window'
    path_txt = 'cRig_path_txt'
    name_txt = 'cRig_name_txt'
    warning1 = 'cRig_UI_warning1'
    checkChar_btn = 'cRig_checkChar_btn'
    setChar_btn = 'cRig_setCharacter_btn'
    basRig_btn = 'cRig_basicIkRig_btn'
    armRig_btn = 'cRig_advArmRig_btn'
    legRig_btn = 'cRig_advLegRig_btn'
    headRig_btn = 'cRig_advHeadRig_btn'
    torsoRig_btn = 'cRig_advTorsoRig_btn'
    bind_chb = 'cRig_bind_chb'
    proxy_chb = 'cRig_proxy_chb'
    applyWts_btn = 'cRig_applyWeights_btn'
    copyWts_btn = 'cRig_proxyWeights_btn'
    blends_btn = 'cRig_blendWrap_btn'
    smoothWts_btn = 'cRig_smoothWeights_btn'
    feedback = 'cRig_bindFeedback'
    config_radioGrp = 'cRig_config_radioGrp'
    color_btn = 'cRig_colorPick_btn'
    charGui_btn = 'cRig_charGui_btn'

    # CREATE WINDOW -----------------------------------
    #check if window was already created
    if cmds.window(name_win, ex=True):
        cmds.deleteUI(name_win)

    #delete window prefs before creating
        if cmds.windowPref(name_win, exists=True):
            cmds.windowPref(name_win, remove=True)

    #crete window
    cmds.window(name_win,
                title='Rig Creator v0.1',
                width=400,
                height=600,
                sizeable=False,
                toolbox=True,
                menuBar=True)


    #create main layout
    main_layout = cmds.columnLayout(p=name_win)

    # UI start:

    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='1.Type in the pathway to your rig files:')

    cmds.textField(path_txt, w=300, p=main_layout, tx=defaultPath)

    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='2a.Select the main skin node, and click button:')

    cmds.button(checkChar_btn, w=300, p=main_layout, bgc=(0.0, 1.0, 0.0),
                l='Query skin name...', c=checkCharName)


    #Set the name to be used for the top node and namespace:
    cmds.text(w=300, p=main_layout, l=' ' + warning1)
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='2b.Use the field name, or type in new name:')

    #Text field for the rig name:
    cmds.textField(name_txt, w=300, p=main_layout, en=False, tx='Name of Character')
    cmds.button(setChar_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Set Rig Name!', c=setCharName)

    #GUI controls to run all the basic rig scripts:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='3.Click the button to create the basic rig:')

    #Button to create the entire basic IK rig:
    cmds.button(basRig_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Basic Rig!', c="source Cmaraffi_basicIkRig")

    #GUI controls to run the advanced arm rig script:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='4.Click the button to add the advanced Arm rig:')

    #Button to add the advanced arm rig:
    cmds.button(armRig_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Arm Rig!', c="source Cmaraffi_advArms")

    #GUI controls to run the advanced leg rig script:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='5.Click the button to add the advanced Leg rig:')
    cmds.button(legRig_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Leg Rig!', c="source Cmaraffi_advLegs")

    #GUI controls to run the advanced head rig script:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='6.Click the button to add the advanced Head rig:')
    cmds.button(headRig_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Head Rig!', c="source Cmaraffi_advHead")

    #GUI controls to run the advanced torso rig script:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='7.Click the button to add the advanced Torso rig:')
    cmds.button(torsoRig_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Torso Rig!', c="source Cmaraffi_advTorso")

    #GUI controls to run the bind rig script:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='8.Deform the skin through binding and blend shapes:')

    #Check boxes and buttons for binding the rig:
    cmds.checkBox(bind_chb, v=False, en=False, l='Bind Skin to Rig!',
                  onc="cm_bindSkin(0)", ofc="cm_bindDetach(0)")
    cmds.text(feedback, w=300, p=main_layout, l=' ')
    cmds.checkBox(proxy_chb, v=False, en=False, l='Bind Proxy Skin!',
                  onc="cm_bindSkin(1)", ofc="cm_bindDetach(1)")

    cmds.button(applyWts_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Apply Proxy Weights from File!', c="cm_getProxyWts")
    cmds.button(copyWts_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Copy Proxy Weights to Skin!', c="cm_copyWeights")
    cmds.button(blends_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Add Face Blend Shapes!', c="cm_blendWrap")
    cmds.button(smoothWts_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Smooth Final Skin Weights!', c="cm_smoothWts")

    #GUI controls to run the advanced character GUI scripts:
    cmds.text(w=400, p=main_layout, fn='smallBoldLabelFont', al='left',
              l='9.Create a character control Gui:')

    cmds.radioButtonGrp(config_radioGrp, p=main_layout, sl=0, nrb=3, cal=[1, "left"],
                        en=False, cw4=[100, 70, 70, 70], l='Set main config:', la3=["Left3", "Right3", "Quad"],
                        on1 = "button -e -en 1 cm_charGuiButton",
                        on2 = "button -e -en 1 cm_charGuiButton",
                        on3 = "button -e -en 1 cm_charGuiButton")

    #Button to open color picker for GUI background color:
    cmds.button(color_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Choose GUI Color!', c="cm_setColor(1)")
    cmds.button(charGui_btn, w=300, p=main_layout, bgc=(1.0, 0.0, 0.0), en=False,
                l='Create Character GUI!', c="source Cmaraffi_characterGui; cm_characterGui;")

    # --------------------------------------------------

    # SHOW WINDOW --------------------------------------

    cmds.showWindow(name_win)

    # --------------------------------------------------

setupRigUI()


'''
 //----------------------------------------------------------------------
   window -e -wh 325 600 -tlc 130 50 $nameWin;
   showWindow $nameWin;
}//Close procedure.
  print "cm_setupRigGui global proc is now in Maya's memory.\n";
//************************************************************************
  print "------------------------------------------------------\n";
  print "Running all procs to create the rig setup GUI!\n";
  print "------------------------------------------------------\n";
//Run proc to create setup Gui for rig:
  cm_setupRigGui;
  print "------------------------------------------------------\n";
  print "CMaraffi_setupRigGui script done!\n";
  print "*********************************************************\n";
  print " \n";
'''