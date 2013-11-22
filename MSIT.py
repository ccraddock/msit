#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.78.01), Fri
Sep 13 11:44:42 2013 If you publish work using this script please cite the
relevant PsychoPy publications:

Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of
    Neuroscience Methods, 162(1-2), 8-13.
Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers
    in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys


############################
# Define                   #
############################

# Turn fullscreen off for testing on monitor that is not 1024x768
FULL_SCREEN=False

# CC here are some parameters that determine the behavior of the task
STIM_ISI_SECONDS = 1.75
NSTIM_BLOCK = 24
NBLOCK = 8
FIXATION_BUFFER_SECONDS = 30

# constants that define the blocks
CONTROL_BLOCK = 333
INTERFERENCE_BLOCK = 444

# constants that we will use to control the behavior
# of the LUMINA device

# Flag determining whether we wish to use the Lumina (will cause task to fail 
# if Lumina is not found).
LUMINA = 0

# Value returned by the Lumina when each of the buttons is pressed
LUMINA_BUTTON_1 = 0
LUMINA_BUTTON_2 = 1
LUMINA_BUTTON_3 = 2

# Value returned by the Lumina when a trigger (scanner) pulse is received
LUMINA_TRIGGER = 4

# Task instructions:
task_instructions1 = """\
Every few seconds, a set of three numbers (1, 2, 3, or 0)"""
task_instructions2 = """\
will appear in the center of the screen.""" 
task_instructions3 = """\
One number will always be different from the other two."""
task_instructions4 = """\
Press the button corresponding to the identity,"""
task_instructions5 = """\
not the position, of the differing number."""
task_instructions6 = """\
The values corresponding to the buttons are:"""
task_instructions7 = """\
index finger = 1, middle finger = 2, and ring finger = 3"""
task_instructions8 = """\
Answer as accurately and quickly as possible."""

# The possible stimuli for the control condition
all_ctrl_stim=['100','020','003']

# The possible stimuli for the interference condition
all_int_stim=['221','212','331','313','112','211','332','233','131','311',\
    '232','322']

############################
# Initialize Communication #
# with the Lumina          #
############################

## initialize communication with the Lumina

if LUMINA == 1:
    import pyxid # to interact with the Lumina box

    ## initialize communication with the Lumina
    devices=pyxid.get_xid_devices()

    if devices:
        lumina_dev=devices[0]
    else:
        print "Could not find Lumina device"
        sys.exit(1)

    print "Found response box:", lumina_dev

    # restart timers associated with Lumina box
    if lumina_dev.is_response_device():
        lumina_dev.reset_base_timer()
        lumina_dev.reset_rt_timer()
    else:
        print "Error: Lumina device is not a response device??"
        log.write("Error: Lumina device is not a response device??")
        sys.exit(1)

###############################
# Get remaining configuration #
# parameters.                 #
###############################

# Store info about the experiment session
expName = 'MSIT'  # from the Builder filename that created this script

# gui dialogue to get participant id, session number, and type of first
# block (useful for counterbalancing)
expInfo = {'Participant ID':'',\
           'Session':'001', \
           'Starting Block': ['Control', 'Interference']}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

# if user pressed cancel, quit
if dlg.OK == False:
    core.quit()

# set a few more configuration parameters
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

####################################
# Set up output files and logging. #
####################################

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error

filename = 'data' + os.path.sep + '%s' %(expInfo['expName']) \
    + os.path.sep + '%s_%s_%s_%s' %(expInfo['Participant ID'],\
                                    expInfo['Session'],\
                                    expInfo['Starting Block'],\
                                    expInfo['date'])

logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

#####################
# Setup the Window. #
#####################

# Setup the Window
win = visual.Window(size=(1024, 768),
                    fullscr=FULL_SCREEN,
                    screen=0,
                    allowGUI=False,
                    allowStencil=False,
                    monitor='testMonitor',
                    color=[0,0,0],
                    colorSpace='rgb')

# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win._getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

#########################################
# Initialize various display components #
#########################################

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instruct_text1 = visual.TextStim(win=win, ori=0, name='instruct_text1',
    text=task_instructions1,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, 0.5], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text2 = visual.TextStim(win=win, ori=0, name='instruct_text2',
    text=task_instructions2,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, 0.42], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text3 = visual.TextStim(win=win, ori=0, name='instruct_text3',
    text=task_instructions3,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, 0.26], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text4 = visual.TextStim(win=win, ori=0, name='instruct_text4',
    text=task_instructions4,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, 0.08], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text5 = visual.TextStim(win=win, ori=0, name='instruct_text5',
    text=task_instructions5,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, 0.0], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text6 = visual.TextStim(win=win, ori=0, name='instruct_text6',
    text=task_instructions6,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, -0.16], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text7 = visual.TextStim(win=win, ori=0, name='instruct_text7',
    text=task_instructions7,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, -.24], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

instruct_text8 = visual.TextStim(win=win, ori=0, name='instruct_text8',
    text=task_instructions8,
    font='Arial',alignHoriz='center', alignVert='center',
    pos=[0, -0.40], height=0.08, wrapWidth=1.5,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "fixation"
fixationClock = core.Clock()
fix_stim = visual.Circle(win=win,
    radius=[0.01875,0.025],
    edges=32,
    ori=0,
    name='fix_stim',
    pos=[0, 0],
    lineColor='white',
    fillColor='white',
    lineColorSpace='rgb',
    opacity=1,
    depth=0.0)

# Initialize components for Routine "control"
controlClock = core.Clock()
control_stim = visual.TextStim(win=win,
    ori=0, name='control_stim',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


# CC begin experiment
all_ctrl_stim=['100','020','003']
ctrl_stim=all_ctrl_stim[np.random.randint(len(all_ctrl_stim))]
prev_ctrl_stim=ctrl_stim

for i in ctrl_stim:
    if ctrl_stim.count(i) == 1:
        ctrl_correct=i
        break


# Initialize components for Routine "trial"
trialClock = core.Clock()
stim_text = visual.TextStim(win=win, ori=0, name='stim_text',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0)
# CC begin experiment
all_target_stim=['221','212','331','313','112','211','332','233','131','311','232','322']
target_stim=all_target_stim[np.random.randint(len(all_target_stim))]
prev_target_stim=target_stim

for i in target_stim:
   if target_stim.count(i) == 1:
      target_correct=i
      break

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thanks = visual.TextStim(win=win, ori=0, name='thanks',
    text='Thanks!',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instruct"-------
t = 0
instructClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
ready = event.BuilderKeyResponse()  # create an object of type KeyResponse
ready.status = NOT_STARTED
# keep track of which components have finished
instructComponents = []
instructComponents.append(instruct_text1)
instructComponents.append(instruct_text2)
instructComponents.append(instruct_text3)
instructComponents.append(instruct_text4)
instructComponents.append(instruct_text5)
instructComponents.append(instruct_text6)
instructComponents.append(instruct_text7)
instructComponents.append(instruct_text8)
instructComponents.append(ready)

for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


#-------Start Routine "instruct"-------
continueRoutine = True

while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    for thisComponent in instructComponents:
        if hasattr(thisComponent, 'status'):
            # *instruct_text* updates
            if t >= 0.0 and thisComponent.status == NOT_STARTED:
            # keep track of start time/frame for later
                thisComponent.tStart = t  # underestimates by a little under one frame
                thisComponent.frameNStart = frameN  # exact frame index
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(True)

    # *ready* updates
    if t >= 0.0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t  # underestimates by a little under one frame
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents()
    if ready.status == STARTED:
        # check for a keypress from a keyboard
        theseKeys = event.getKeys(keyList=['1','2','3'])
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

        # check for a LUMINA_TRIGGER from the Lumina box
        if LUMINA == 1:
            lumina_dev.poll_for_response()
            while lumina_dev.response_queue_size() > 0:
                response = lumina_dev.get_next_response() 
                if response["pressed"]: 
                    print "Lumina received: %s, %d"%(response["key"],response["key"])
                    if response["key"] == LUMINA_TRIGGER:
                        continueRoutine = False

    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
         routineTimer.reset()

#-------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix_stim)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_stim* updates
    if t >= 0.0 and fix_stim.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_stim.tStart = t  # underestimates by a little under one frame
        fix_stim.frameNStart = frameN  # exact frame index
        fix_stim.setAutoDraw(True)
    elif fix_stim.status == STARTED and t >= (0.0 + 30):
        fix_stim.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
exp_loop = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=u'/Users/bodhi/Desktop/PhD/NY2013/rtfmri_ex/psyPy/MSIT/MSIT_ctrl_int.psyexp',
    trialList=[None],
    seed=None, name='exp_loop')
thisExp.addLoop(exp_loop)  # add the loop to the experiment
thisExp_loop = exp_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisExp_loop.rgb)
if thisExp_loop != None:
    for paramName in thisExp_loop.keys():
        exec(paramName + '= thisExp_loop.' + paramName)

for thisExp_loop in exp_loop:
    currentLoop = exp_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop.keys():
            exec(paramName + '= thisExp_loop.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    ctrl_loop = data.TrialHandler(nReps=24, method='random', 
        extraInfo=expInfo, originPath=u'/Users/bodhi/Desktop/PhD/NY2013/rtfmri_ex/psyPy/MSIT/MSIT_ctrl_int.psyexp',
        trialList=[None],
        seed=None, name='ctrl_loop')
    thisExp.addLoop(ctrl_loop)  # add the loop to the experiment
    thisCtrl_loop = ctrl_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisCtrl_loop.rgb)
    if thisCtrl_loop != None:
        for paramName in thisCtrl_loop.keys():
            exec(paramName + '= thisCtrl_loop.' + paramName)
    
    for thisCtrl_loop in ctrl_loop:
        currentLoop = ctrl_loop
        # abbreviate parameter names if possible (e.g. rgb = thisCtrl_loop.rgb)
        if thisCtrl_loop != None:
            for paramName in thisCtrl_loop.keys():
                exec(paramName + '= thisCtrl_loop.' + paramName)
        
        #------Prepare to start Routine "control"-------
        t = 0
        controlClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.750000)
        # update component parameters for each repeat
        control_stim.setText(ctrl_stim)
        control_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        control_resp.status = NOT_STARTED
        # CC begin routine
        
        
        # set next stimulus
        set_diff=np.setdiff1d(all_ctrl_stim,prev_ctrl_stim)
        np.random.shuffle(set_diff)
        ctrl_stim=set_diff[0]
        prev_ctrl_stim=ctrl_stim
        
        for i in ctrl_stim:
            if ctrl_stim.count(i) == 1:
                ctrl_correct=i
                break
        #print ctrl_stim
        
        # logging
        ctrl_loop.addData('ctrl_stim',ctrl_stim)
        ctrl_loop.addData('ctrl_correct',ctrl_correct)
        # keep track of which components have finished
        controlComponents = []
        controlComponents.append(control_stim)
        controlComponents.append(control_resp)
        for thisComponent in controlComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "control"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = controlClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *control_stim* updates
            if t >= 0.0 and control_stim.status == NOT_STARTED:
                # keep track of start time/frame for later
                control_stim.tStart = t  # underestimates by a little under one frame
                control_stim.frameNStart = frameN  # exact frame index
                control_stim.setAutoDraw(True)
            elif control_stim.status == STARTED and t >= (0.0 + 1.75):
                control_stim.setAutoDraw(False)
            
            # *control_resp* updates
            if t >= 0.0 and control_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                control_resp.tStart = t  # underestimates by a little under one frame
                control_resp.frameNStart = frameN  # exact frame index
                control_resp.status = STARTED
                # keyboard checking is just starting
                control_resp.clock.reset()  # now t=0
                event.clearEvents()
            elif control_resp.status == STARTED and t >= (0.0 + 1.75):
                control_resp.status = STOPPED
            #if control_resp.status == STARTED:
                # check for a LUMINA_TRIGGER from the Lumina box
                if LUMINA == 1:
                    theseKeys=[]
                    lumina_dev.poll_for_response()
                    while lumina_dev.response_queue_size() > 0:
                        response = lumina_dev.get_next_response() 
                        if response["pressed"]:
                            print "Lumina received: %s, %d"%(response["key"],response["key"])
                            if response["key"] in [0,1,2]: 
                                theseKeys.append(str(response["key"]+1))
                else:
                    theseKeys = event.getKeys(keyList=['1', '2', '3'])

                if len(theseKeys) > 0:  # at least one key was pressed
                    control_resp.keys = theseKeys[-1]  # just the last key pressed
                    control_resp.rt = control_resp.clock.getTime()
                    # was this 'correct'?
                    if (control_resp.keys == str(ctrl_correct)): control_resp.corr = 1
                    else: control_resp.corr=0
            

            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in controlComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "control"-------
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if len(control_resp.keys) == 0:  # No response was made
           control_resp.keys=None
           # was no response the correct answer?!
           if str(ctrl_correct).lower() == 'none': control_resp.corr = 1  # correct non-response
           else: control_resp.corr = 0  # failed to respond (incorrectly)
        # store data for ctrl_loop (TrialHandler)
        ctrl_loop.addData('control_resp.keys',control_resp.keys)
        ctrl_loop.addData('control_resp.corr', control_resp.corr)
        if control_resp.keys != None:  # we had a response
            ctrl_loop.addData('control_resp.rt', control_resp.rt)
        
        thisExp.nextEntry()
        
    # completed 24 repeats of 'ctrl_loop'
    
    
    # set up handler to look after randomisation of conditions etc
    target_loop = data.TrialHandler(nReps=24, method='random', 
        extraInfo=expInfo, originPath=u'/Users/bodhi/Desktop/PhD/NY2013/rtfmri_ex/psyPy/MSIT/MSIT_ctrl_int.psyexp',
        trialList=[None],
        seed=None, name='target_loop')
    thisExp.addLoop(target_loop)  # add the loop to the experiment
    thisTarget_loop = target_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTarget_loop.rgb)
    if thisTarget_loop != None:
        for paramName in thisTarget_loop.keys():
            exec(paramName + '= thisTarget_loop.' + paramName)
    
    for thisTarget_loop in target_loop:
        currentLoop = target_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTarget_loop.rgb)
        if thisTarget_loop != None:
            for paramName in thisTarget_loop.keys():
                exec(paramName + '= thisTarget_loop.' + paramName)
        
        #------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.750000)
        # update component parameters for each repeat
        stim_text.setColor('white', colorSpace='rgb')
        stim_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        stim_response.status = NOT_STARTED
        # CC begin routine
        
        
        # set next stimulus
        
        set_diff=np.setdiff1d(all_target_stim,prev_target_stim)
        np.random.shuffle(set_diff)
        target_stim=set_diff[0]
        prev_target_stim=target_stim
        
        for i in target_stim:
           if target_stim.count(i) == 1:
              target_correct=i
              break
        #print target_stim
        
        # logging
        target_loop.addData('target_stim',target_stim)
        target_loop.addData('target_correct',target_correct)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(stim_text)
        trialComponents.append(stim_response)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim_text* updates
            if t >= 0.0 and stim_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_text.tStart = t  # underestimates by a little under one frame
                stim_text.frameNStart = frameN  # exact frame index
                stim_text.setAutoDraw(True)
            elif stim_text.status == STARTED and t >= (0.0 + 1.75):
                stim_text.setAutoDraw(False)
            if stim_text.status == STARTED:  # only update if being drawn
                stim_text.setText(target_stim, log=False)
            
            # *stim_response* updates
            if t >= 0 and stim_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                stim_response.tStart = t  # underestimates by a little under one frame
                stim_response.frameNStart = frameN  # exact frame index
                stim_response.status = STARTED
                # keyboard checking is just starting
                stim_response.clock.reset()  # now t=0
                event.clearEvents()
            elif stim_response.status == STARTED and t >= (0 + 1.75):
                stim_response.status = STOPPED

            if stim_response.status == STARTED:
                # check for a LUMINA_TRIGGER from the Lumina box
                if LUMINA == 1:
                    theseKeys=[]
                    lumina_dev.poll_for_response()
                    while lumina_dev.response_queue_size() > 0:
                        response = lumina_dev.get_next_response() 
                        if response["pressed"]: 
                            print "Lumina received: %s, %d"%(response["key"],response["key"])
                            if response["key"] in [0,1,2]:
                                print "matches"
                                theseKeys.append(str(response["key"]+1))
                else:
                    theseKeys = event.getKeys(keyList=['1', '2', '3'])

                if len(theseKeys) > 0:  # at least one key was pressed
                    stim_response.keys = theseKeys[-1]  # just the last key pressed
                    stim_response.rt = stim_response.clock.getTime()
                    # was this 'correct'?
                    if (stim_response.keys == str(target_correct)): stim_response.corr = 1
                    else: stim_response.corr=0
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if len(stim_response.keys) == 0:  # No response was made
           stim_response.keys=None
           # was no response the correct answer?!
           if str(target_correct).lower() == 'none': stim_response.corr = 1  # correct non-response
           else: stim_response.corr = 0  # failed to respond (incorrectly)
        # store data for target_loop (TrialHandler)
        target_loop.addData('stim_response.keys',stim_response.keys)
        target_loop.addData('stim_response.corr', stim_response.corr)
        if stim_response.keys != None:  # we had a response
            target_loop.addData('stim_response.rt', stim_response.rt)
        
        thisExp.nextEntry()
        
    # completed 24 repeats of 'target_loop'
    
    thisExp.nextEntry()
    
# completed 4 repeats of 'exp_loop'


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(30.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixationComponents = []
fixationComponents.append(fix_stim)
for thisComponent in fixationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "fixation"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_stim* updates
    if t >= 0.0 and fix_stim.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_stim.tStart = t  # underestimates by a little under one frame
        fix_stim.frameNStart = frameN  # exact frame index
        fix_stim.setAutoDraw(True)
    elif fix_stim.status == STARTED and t >= (0.0 + 30):
        fix_stim.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = []
ThanksComponents.append(thanks)
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Thanks"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanks* updates
    if t >= 0.0 and thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanks.tStart = t  # underestimates by a little under one frame
        thanks.frameNStart = frameN  # exact frame index
        thanks.setAutoDraw(True)
    elif thanks.status == STARTED and t >= (0.0 + 3):
        thanks.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


win.close()
core.quit()
