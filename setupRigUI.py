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

def checkCharName():
    '''
    This function finds the name of the character
    '''
    pass


def setCharName():
    '''
    This function sets the name of the character
    '''
    pass


def setNamespace():
    '''
    This function sets the a namespace for the character
    '''
    pass


def setupRigUI():
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
    config_radio = 'cRig_config_radio'
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
                width=323,
                height=362,
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
                l='Query skin name...', c='cm_checkCharName')

    # --------------------------------------------------

    # SHOW WINDOW --------------------------------------

    cmds.showWindow(name_win)

    # --------------------------------------------------


'''
//4. Main global procedure to run setup Gui window:
global proc cm_setupRigGui (){//Open procedure...
 //Declare unique GUI strings for the path and names:
   string $defaultPath = "C:/CMaraffi_bookFiles/";
   string $nameWin = "cm_setupGuiWin";
   string $pathField = "cm_pathField";
   string $nameField = "cm_nameField";
   string $warning1 = "cm_guiWarning1";
   string $checkCharButt = "cm_checkCharButton";
   string $setCharButt = "cm_setCharacterButton";
   string $basRigButt = "cm_basicIkRigButton";
   string $armRigButt = "cm_advArmRigButton";
   string $legRigButt = "cm_advLegRigButton";
   string $headRigButt = "cm_advHeadRigButton";
   string $torsoRigButt = "cm_advTorsoRigButton";
   string $bindCheckBox = "cm_bindCheckBox";
   string $proxyCheckBox = "cm_proxyCheckBox";
   string $applyWtsButt = "cm_applyWeightsButton";
   string $copyWtsButt = "cm_proxyWeightsButton";
   string $blendsButt = "cm_blendWrapButton";
   string $smoothWtsButt = "cm_smoothWeightsButton";
   string $feedback = "cm_bindFeedback";
   string $configRadios = "cm_configRadios";
   string $colorButt = "cm_colorPickButton";
   string $charGuiButt = "cm_charGuiButton";
 //----------------------------------------------------------------------
 //Create the main setup GUI window:
   if(`window -ex $nameWin`) deleteUI $nameWin;
   window -t "CMaraffi Rig Creator" $nameWin;
   string $layout = `columnLayout -p $nameWin`;
 //Create controls for running the rig scripts:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
          -l "1.Type in the pathway to your rig files:";
 //Text field for to set directory path for all files:
   textField -w 300 -p $layout -tx $defaultPath $pathField;
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
          -l "2a.Select the main skin node, and click button:";
   button -w 300 -p $layout -bgc 0.0 1.0 0.0 -l "Query skin name..."
          -c "cm_checkCharName" $checkCharButt;
 //----------------------------------------------------------------------
 //Set the name to be used for the top node and namespace:
   text -w 300 -p $layout -l " " $warning1;
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
          -l "2b.Use the field name, or type in new name:";
 //Text field for the rig name:
   textField  -w 300 -p $layout -tx "Name of Character" -en 0 $nameField;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -en 0 -l "Set Rig Name!"
          -c "cm_setCharName" $setCharButt;
 //----------------------------------------------------------------------
 //GUI controls to run all the basic rig scripts:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "3.Click the button to create the basic rig:";
 //Button to create the entire basic IK rig:
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -en 0 -l "Create Basic Rig!"
           -c "source Cmaraffi_basicIkRig" $basRigButt;
 //----------------------------------------------------------------------
 //GUI controls to run the advanced arm rig script:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "4.Click the button to add the advanced Arm rig:";
 //Button to add the advanced arm rig:
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Create Arm Rig!"
            -en 0 -c "source Cmaraffi_advArms" $armRigButt;
 //----------------------------------------------------------------------
 //GUI controls to run the advanced leg rig script:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "5.Click the button to add the advanced Leg rig:";
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Create Leg Rig!"
            -en 0 -c "source Cmaraffi_advLegs" $legRigButt;
 //----------------------------------------------------------------------
 //GUI controls to run the advanced head rig script:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "6.Click the button to add the advanced Head rig:";
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Create Head Rig!"
            -en 0 -c "source Cmaraffi_advHead" $headRigButt;
 //----------------------------------------------------------------------
 //GUI controls to run the advanced torso rig script:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "7.Click the button to add the advanced Torso rig:";
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Create Torso Rig!"
            -en 0 -c "source Cmaraffi_advTorso" $torsoRigButt;
 //----------------------------------------------------------------------
 //GUI controls to run the bind rig script:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "8.Deform the skin through binding and blend shapes:";
 //Check boxes and buttons for binding the rig:
   checkBox -v 0 -l "Bind Skin to Rig!" -en 0 -onc "cm_bindSkin(0)"
            -ofc "cm_bindDetach(0)" $bindCheckBox;
   text -w 300 -p $layout -l " " $feedback;
   checkBox -v 0 -l "Bind Proxy Skin!" -en 0 -onc "cm_bindSkin(1)"
            -ofc "cm_bindDetach(1)" $proxyCheckBox;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Apply Proxy Weights from File!"
            -en 0 -c "cm_getProxyWts" $applyWtsButt;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Copy Proxy Weights to Skin!"
            -en 0 -c "cm_copyWeights" $copyWtsButt;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Add Face Blend Shapes!"
            -en 0 -c "cm_blendWrap" $blendsButt;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Smooth Final Skin Weights!"
            -en 0 -c "cm_smoothWts" $smoothWtsButt;
 //----------------------------------------------------------------------
 //GUI controls to run the advanced character GUI scripts:
   text -w 400 -p $layout -fn "smallBoldLabelFont" -al "left"
         -l "9.Create a character control Gui:";
   radioButtonGrp -p $layout -sl 0 -nrb 3 -cal 1 "left" -cw4 100 70 70 70
	-en 0 -l "Set main config:" -la3 "Left3" "Right3" "Quad"
	-on1 "button -e -en 1 cm_charGuiButton"
	-on2 "button -e -en 1 cm_charGuiButton"
	-on3 "button -e -en 1 cm_charGuiButton" $configRadios;
 //Button to open color picker for GUI background color:
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Choose GUI Color!"
            -en 0 -c "cm_setColor(1)" $colorButt;
   button -w 300 -p $layout -bgc 1.0 0.0 0.0 -l "Create Character GUI!"
            -en 0 -c {"source Cmaraffi_characterGui; cm_characterGui;"}
            $charGuiButt;
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