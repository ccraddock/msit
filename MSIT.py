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
from psychopy import visual, core, data, event, logging, gui
from psychopy.constants import *  # things like STARTED, FINISHED
from numpy.random import randint, shuffle
import os  # handy system and path functions
import sys


############################
# Define                   #
############################

# Turn fullscreen off for testing on monitor that == not 1024x768
FULL_SCREEN=False

# CC here are some parameters that determine the behavior of the task
STIM_ISI_SECONDS = 1.75
NSTIM_BLOCK = 24
NBLOCK_ITER = 4
FIXATION_BUFFER_SECONDS = 30.0

# constants that define the blocks
CONTROL_BLOCK = 333
INTERFERENCE_BLOCK = 444

# constants that we will use to control the behavior
# of the LUMINA device

# Flag determining whether we wish to use the Lumina (will cause task to fail 
# if Lumina == not found).
LUMINA = 0

# Value returned by the Lumina when each of the buttons == pressed
LUMINA_BUTTON_1 = 0
LUMINA_BUTTON_2 = 1
LUMINA_BUTTON_3 = 2

# Value returned by the Lumina when a trigger (scanner) pulse == received
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
all_control_stim=['100','020','003']


# The possible stimuli for the interference condition
all_int_stim=['221','212','331','313','112','211','332','233','131','311',\
    '232','322']

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
           'Configuration': ['Task', 'Practice'], \
           'Starting Block': ['Control', 'Interference']}

dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

# if user pressed cancel, quit
if dlg.OK == False:
    core.quit()

# set a few more configuration parameters
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

print expInfo['Configuration']
if expInfo['Configuration'] == 'Practice':
    print "Configuration Practice"
elif expInfo['Configuration'] == 'Task':
    print "Configuration Task"


# if practice, reconfigure some aspects
if expInfo['Configuration'] == 'Practice':
    FIXATION_BUFFER_SECONDS = 3.0


# if interference first, swap stim
if expInfo['Starting Block'] == 'Interference':
    all_first_text=all_int_stim
    all_second_stim=all_control_stim
else:
    all_first_text=all_control_stim
    all_second_stim=all_int_stim

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
        print "Error: Lumina device == not a response device??"
        sys.exit(1)


####################################
# Set up output files and logging. #
####################################

# Setup files for saving
if not os.path.isdir('../data'+ os.path.sep + '%s' %(expInfo['expName']) ):
    # if this fails (e.g. permissions) we will get error
    os.makedirs('../data'+ os.path.sep + '%s' %(expInfo['expName']) )

filename = '../data' + os.path.sep + '%s' %(expInfo['expName']) \
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

# Initialize components for Routine "first"
firstClock = core.Clock()
first_text = visual.TextStim(win=win,
    ori=0, name='first_text',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "second"
secondClock = core.Clock()
second_text = visual.TextStim(win=win, ori=0, name='second_text',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# text to indicate whether the answer was correct or incorrect
if expInfo['Configuration'] == 'Practice':
    response_text = visual.TextStim(win=win, ori=0, name='response_text',
        text='nonsense',    font='Arial',
        pos=[0, 0.3], height=0.08, wrapWidth=None,
        color='white', colorSpace='rgb', opacity=1,
        depth=0.0)

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
thanks = visual.TextStim(win=win, ori=0, name='thanks',
    text='Thank you for your participation!',    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)


########################
# Start the experiment #
########################

# Initialize timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------ Routine "Instruct" -------
#---------------------------------
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

# set every component to not started
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED


#-------Start Routine "instruct"-------
continueRoutine = True
while continueRoutine:

    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 == the first frame)

    # update/draw components on each frame
    for thisComponent in instructComponents:
        if hasattr(thisComponent, 'status'):
            # *instruct_text* updates
            if t >= 0.0 and thisComponent.status == NOT_STARTED:
            # keep track of start time/frame for later
                thisComponent.tStart = t  # underestimates by a little under
                                          # one frame
                thisComponent.frameNStart = frameN  # exact frame index
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(True)

    # --- framewise state machine
    if t >= 0.0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t  # underestimates by a little under one frame
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED

        # start keyboard / LUMINA checking by first 
        # clearing all previous events
        #
        # clear the keyboard events
        event.clearEvents()

        # clear Lumina events
        if LUMINA == 1:
            lumina_dev.clear_response_queue()

    if ready.status == STARTED:

        # returns key presses, we are looking for all keys (keyList=None)
        theseKeys = event.getKeys(keyList=None)
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False

        # check for a LUMINA_TRIGGER from the Lumina box
        if LUMINA == 1:
            lumina_dev.poll_for_response()
            while lumina_dev.response_queue_size() > 0:
                response = lumina_dev.get_next_response()
                if response["pressed"]:
                    # LUMINA debug statement
                    print "Lumina received: %s, %d"%(response["key"],\
                        response["key"])
                    # if we receive a TRIGGER enable the task
                    if response["key"] == LUMINA_TRIGGER:
                        continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset() # if we abort early the non-slip timer needs reset
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
    if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------ Routine "Fixation" -------
#---------------------------------

# get things going
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(FIXATION_BUFFER_SECONDS)

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
    frameN = frameN + 1  # number of completed frames (so 0 == the first frame)
    # update/draw components on each frame
    #
    # *fix_stim* updates
    if t >= 0.0 and fix_stim.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_stim.tStart = t  # underestimates by a little under one frame
        fix_stim.frameNStart = frameN  # exact frame index
        fix_stim.setAutoDraw(True)
    elif fix_stim.status == STARTED and t >= (0.0 + FIXATION_BUFFER_SECONDS):
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
    if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
        win.flip()

#-------Ending Routine "fixation"-------
for thisComponent in fixationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

#------ Experiment loop ----------
#---------------------------------

# set up handler to look after randomisation of conditions etc
exp_loop = data.TrialHandler(nReps=NBLOCK_ITER, method='random', 
    extraInfo=expInfo, originPath=u'MSIT.psyexp',
    trialList=[None],
    seed=None, name='exp_loop')

thisExp.addLoop(exp_loop)  # add the loop to the experiment
thisExp_loop = exp_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisExp_loop.rgb)
if thisExp_loop != None:
    for paramName in thisExp_loop.keys():
        exec(paramName + '= thisExp_loop.' + paramName)

# calculate performance statistics
first_block_rt=0
first_block_err=0
first_block_nstim=0
first_total_rt=0
first_total_err=0
first_total_nstim=0

second_block_rt=0
second_block_err=0
second_block_nstim=0
second_total_rt=0
second_total_err=0
second_total_nstim=0

block_num = 0
for thisExp_loop in exp_loop:

    # counter keeps track of the current block number
    block_num += 1

    currentLoop = exp_loop
    # abbreviate parameter names if possible (e.g. rgb = thisExp_loop.rgb)
    if thisExp_loop != None:
        for paramName in thisExp_loop.keys():
            exec(paramName + '= thisExp_loop.' + paramName)

    # set up handler to look after randomisation of conditions etc
    first_loop = data.TrialHandler(nReps=NSTIM_BLOCK, method='random',
        extraInfo=expInfo, originPath=u'MSIT.psyexp',
        trialList=[None],
        seed=None, name='first_loop')
    thisExp.addLoop(first_loop)  # add the loop to the experiment
    thisFirst_loop = first_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisFirst_loop.rgb)
    if thisFirst_loop != None:
        for paramName in thisFirst_loop.keys():
            exec(paramName + '= thisFirst_loop.' + paramName)


    #reset the block statistics
    first_block_rt=0
    first_block_err=0
    first_block_nstim=0

    prev_first_text_str=None

    #---- first inner loop ----
    for thisFirst_loop in first_loop:

        # select the stimuli
        if prev_first_text_str == None:
            first_text_str=all_first_text[randint(len(all_first_text))]
        else:
            # set next stimulus
            set_diff=[x for x in all_first_text if x != prev_first_text_str]
            shuffle(set_diff)
            first_text_str=set_diff[0]

        # set the previous stimulus
        prev_first_text_str=first_text_str

        # calculate the correct answer
        for i in first_text_str:
            if first_text_str.count(i) == 1:
                first_correct_str=i
                break
        #print first_text_str

        currentLoop = first_loop
        # abbreviate parameter names if possible (e.g. rgb = thisFirst_loop.rgb)
        if thisFirst_loop != None:
            for paramName in thisFirst_loop.keys():
                exec(paramName + '= thisFirst_loop.' + paramName)

        #------Prepare to start Routine "first inner loop"-------
        t = 0
        firstClock.reset()  # clock 
        frameN = -1
        routineTimer.add(STIM_ISI_SECONDS)
        # update component parameters for each repeat
        first_text.setText(first_text_str)
        first_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
        first_resp.status = NOT_STARTED
        # CC begin routine


        # logging
        first_loop.addData('first_text_str',first_text_str)
        first_loop.addData('first_correct_str',first_correct_str)
        # keep track of which components have finished
        controlComponents = []
        controlComponents.append(first_text)
        if expInfo['Configuration'] == 'Practice':
            controlComponents.append(response_text)
        controlComponents.append(first_resp)
        for thisComponent in controlComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "second"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = firstClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 == the first frame)
            # update/draw components on each frame

            # *first_text* updates
            if t >= 0.0 and first_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_text.tStart = t  # underestimates by a little under one frame
                first_text.frameNStart = frameN  # exact frame index
                first_text.setAutoDraw(True)
                if expInfo['Configuration'] == 'Practice':
                    response_text.setText('')
                    response_text.setAutoDraw(True)
            elif first_text.status == STARTED and t >= (0.0 + STIM_ISI_SECONDS):
                first_text.setAutoDraw(False)
                if expInfo['Configuration'] == 'Practice':
                    response_text.setAutoDraw(False)

            # *first_resp* updates
            if t >= 0.0 and first_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                first_resp.tStart = t  # underestimates by a little under one frame
                first_resp.frameNStart = frameN  # exact frame index
                first_resp.status = STARTED
                # keyboard checking == just starting
                first_resp.clock.reset()  # now t=0
                event.clearEvents()
                # clear Lumina events
                if LUMINA == 1:
                    lumina_dev.clear_response_queue()
            elif first_resp.status == STARTED and t >= (0.0 + STIM_ISI_SECONDS):
                first_resp.status = STOPPED

            if first_resp.status == STARTED:
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
                    theseKeys = event.getKeys(keyList=['1', '2', '3', 'left',\
                        'down','right'])

                if len(theseKeys) > 0:  # at least one key was pressed
                    first_resp.keys = theseKeys[-1]  # just the last key pressed
                    first_resp.rt = first_resp.clock.getTime()
                    if first_resp.keys == 'left':
                        first_resp.keys = '1'
                    elif first_resp.keys == 'down':
                        first_resp.keys = '2'
                    elif first_resp.keys == 'right':
                        first_resp.keys = '3'

                    # was this 'correct'?
                    if (first_resp.keys == str(first_correct_str)):
                        first_resp.corr = 1
                        if expInfo['Configuration'] == 'Practice':
                            response_text.setText("%s is correct"%(first_resp.keys))
                            response_text.setColor('white')
                    else:
                        first_resp.corr=0
                        if expInfo['Configuration'] == 'Practice':
                            response_text.setText("%s is incorrect"%(first_resp.keys))
                            response_text.setColor('red')

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
            if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "control"-------
        for thisComponent in controlComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if len(first_resp.keys) == 0:  # No response was made
           first_resp.keys=None
           # was no response the correct answer?!
           if str(first_correct_str).lower() == 'none': first_resp.corr = 1  # correct non-response
           else: first_resp.corr = 0  # failed to respond (incorrectly)
        # store data for first_loop (TrialHandler)
        first_loop.addData('first_resp.keys',first_resp.keys)
        first_loop.addData('first_resp.corr', first_resp.corr)
        if first_resp.keys != None:  # we had a response
            first_loop.addData('first_resp.rt', first_resp.rt)

        # update running performance statistics
        # only include reaction time for correct responses
        # count missing responses as errors
        if first_resp.corr == 1:
            first_block_rt += first_resp.rt
        else:
            first_block_err += 1

        thisExp.nextEntry()

    # completed NSTIM_BLOCK repeats of 'first_loop'
    # update total statistics
    first_total_rt+=first_block_rt
    first_total_err+=first_block_err
    first_total_nstim+=NSTIM_BLOCK

    if NSTIM_BLOCK > first_block_err:
        print "%s block #%d: errors %d, rt %3.2f sec"%(\
            expInfo['Starting Block'],block_num,\
            first_block_err,\
            first_block_rt / float(NSTIM_BLOCK - first_block_err))
    else:
        print "%s block #%d: errors %d, rt nan"%(\
            expInfo['Starting Block'],block_num,\
            first_block_err)

    # set up handler to look after randomisation of conditions etc
    second_loop = data.TrialHandler(nReps=NSTIM_BLOCK, method='random',
        extraInfo=expInfo, originPath=u'MSIT.psyexp',
        trialList=[None],
        seed=None, name='second_loop')
    thisExp.addLoop(second_loop)  # add the loop to the experiment
    thisSecond_loop = second_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisSecond_loop.rgb)
    if thisSecond_loop != None:
        for paramName in thisSecond_loop.keys():
            exec(paramName + '= thisSecond_loop.' + paramName)


    #reset statistics
    second_block_rt=0
    second_block_err=0
    second_block_nstim=0

    prev_second_stim_str = None
    #---- second inner loop ----
    for thisSecond_loop in second_loop:
        currentLoop = second_loop
        # abbreviate parameter names if possible (e.g. rgb = thisSecond_loop.rgb)
        if thisSecond_loop != None:
            for paramName in thisSecond_loop.keys():
                exec(paramName + '= thisSecond_loop.' + paramName)

        #------Prepare to start Routine "trial"-------
        # set next stimulus
        if not prev_second_stim_str:
            second_stim_str=all_second_stim[randint(len(all_second_stim))]
        else:
            set_diff=[x for x in all_second_stim if x != prev_second_stim_str]
            shuffle(set_diff)
            second_stim_str=set_diff[0]

        # keep track of the previous stim
        prev_second_stim_str=second_stim_str

        # determine the correct answer
        for i in second_stim_str:
           if second_stim_str.count(i) == 1:
              second_correct_str=i
              break

        t = 0
        secondClock.reset()  # clock 
        frameN = -1
        routineTimer.add(STIM_ISI_SECONDS)
        # update component parameters for each repeat
        second_text.setColor('white', colorSpace='rgb')
        second_response = event.BuilderKeyResponse()  # create an object of type KeyResponse
        second_response.status = NOT_STARTED

        # logging
        second_loop.addData('second_stim_str',second_stim_str)
        second_loop.addData('second_correct_str',second_correct_str)
        # keep track of which components have finished
        trialComponents = []
        trialComponents.append(second_text)
        if expInfo['Configuration'] == 'Practice':
            trialComponents.append(response_text)
        trialComponents.append(second_response)
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED

        #-------Start Routine "trial"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = secondClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 == the first frame)
            # update/draw components on each frame
            #
            # *second_text* updates
            if t >= 0.0 and second_text.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_text.tStart = t  # underestimates by a little under one frame
                second_text.frameNStart = frameN  # exact frame index
                second_text.setAutoDraw(True)
                if expInfo['Configuration'] == 'Practice':
                    response_text.setText('')
                    response_text.setAutoDraw(True)
            elif second_text.status == STARTED and t >= (0.0 + STIM_ISI_SECONDS):
                second_text.setAutoDraw(False)
                if expInfo['Configuration'] == 'Practice':
                    response_text.setText('')
                    response_text.setAutoDraw(False)
            if second_text.status == STARTED:  # only update if being drawn
                second_text.setText(second_stim_str, log=False)

            # *second_response* updates
            if t >= 0 and second_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                second_response.tStart = t  # underestimates by a little under one frame
                second_response.frameNStart = frameN  # exact frame index
                second_response.status = STARTED
                # keyboard checking == just starting
                second_response.clock.reset()  # now t=0
                event.clearEvents()
                # clear Lumina events
                if LUMINA == 1:
                    lumina_dev.clear_response_queue()
            elif second_response.status == STARTED and t >= (0 + STIM_ISI_SECONDS):
                second_response.status = STOPPED

            if second_response.status == STARTED:
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
                    theseKeys = event.getKeys(keyList=['1', '2', '3','left',\
                        'down','right'])

                if len(theseKeys) > 0:  # at least one key was pressed
                    second_response.keys = theseKeys[-1]  # just the last key pressed
                    second_response.rt = second_response.clock.getTime()
                    if second_response.keys == 'left':
                        second_response.keys = '1'
                    elif second_response.keys == 'down':
                        second_response.keys = '2'
                    elif second_response.keys == 'right':
                        second_response.keys = '3'
                    # was this 'correct'?
                    if (second_response.keys == str(second_correct_str)):
                        if expInfo['Configuration'] == 'Practice':
                            response_text.setText("%s is correct"%(second_response.keys))
                            response_text.setColor('white')
                        second_response.corr = 1
                    else:
                        if expInfo['Configuration'] == 'Practice':
                            response_text.setText("%s is incorrect"%(second_response.keys))
                            response_text.setColor('red')
                        second_response.corr=0


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
            if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
                win.flip()

        #-------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if len(second_response.keys) == 0:  # No response was made
           second_response.keys=None
           # was no response the correct answer?!
           if str(second_correct_str).lower() == 'none': second_response.corr = 1  # correct non-response
           else: second_response.corr = 0  # failed to respond (incorrectly)
        # store data for second_loop (TrialHandler)
        second_loop.addData('second_response.keys',second_response.keys)
        second_loop.addData('second_response.corr', second_response.corr)
        if second_response.keys != None:  # we had a response
            second_loop.addData('second_response.rt', second_response.rt)

        if second_response.corr == 1:
            second_block_rt+=second_response.rt
        else:
            second_block_err+=1

        thisExp.nextEntry()

    # completed NSTIM_BLOCK repeats of 'second_loop'
    # update total statistics
    second_total_rt+=second_block_rt
    second_total_err+=second_block_err
    second_total_nstim+=NSTIM_BLOCK

    if expInfo['Starting Block'] == 'Interference':
        t_str = "Control"
    else:
        t_str = "Interference"

    if NSTIM_BLOCK > second_block_err:
        print "%s block #%d: errors %d, rt %3.2f sec"%(t_str,block_num,\
            second_block_err, second_block_rt / float(NSTIM_BLOCK-second_block_err))
    else:
        print "%s block #%d: errors %d, rt nan"%(t_str,block_num,\
            second_block_err )

    thisExp.nextEntry()

# completed NBLOCK_ITER repeats of 'exp_loop'
if expInfo['Starting Block'] == 'Interference':
    print "Control total: errors %d, rt %3.2f sec"%( \
        second_total_err, second_total_rt / float(second_total_nstim))
    print "Interference total: errors %d, rt %3.2f sec"%( \
        first_total_err, first_total_rt / float(first_total_nstim))
else:
    print "Control total: errors %d, rt %3.2f sec"%( \
        first_total_err, first_total_rt / float(first_total_nstim))
    print "Interference total: errors %d, rt %3.2f sec"%( \
        second_total_err, second_total_rt / float(second_total_nstim))


#------Prepare to start Routine "fixation"-------
t = 0
fixationClock.reset()  # clock 
frameN = -1
routineTimer.add(FIXATION_BUFFER_SECONDS)
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
    frameN = frameN + 1  # number of completed frames (so 0 == the first frame)
    # update/draw components on each frame

    # *fix_stim* updates
    if t >= 0.0 and fix_stim.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_stim.tStart = t  # underestimates by a little under one frame
        fix_stim.frameNStart = frameN  # exact frame index
        fix_stim.setAutoDraw(True)
    elif fix_stim.status == STARTED and t >= (0.0 + FIXATION_BUFFER_SECONDS):
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
    if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
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
    frameN = frameN + 1  # number of completed frames (so 0 == the first frame)
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
    if continueRoutine:  # don't flip if this routine == over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


win.close()
core.quit()
