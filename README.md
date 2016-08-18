[![DOI](https://zenodo.org/badge/9342/ccraddock/msit.svg)](https://zenodo.org/badge/latestdoi/9342/ccraddock/msit)

# Multi-Source Interference Task

R. Cameron Craddock<sup>1,2,†</sup>

<sup>1</sup>Nathan S. Kline Institute for Psychiatric Research, Orangeburg, NY, <sup>2</sup>Child Mind Institute, New York, NY

<sup>†</sup>Contact [cameron.craddock@childmind.org](mailto:cameron.craddock@childmind.org) with any comments or questions.

## Task Description

This [PsychoPy](http://www.psychopy.org/) implementation of the Multi-source Interference Task (MSIT)
conforms to the implementation described in [Bush and Shin, 2006](http://www.nature.com/nprot/journal/v1/n1/full/nprot.2006.48.html):

Bush, G, Shin, LM **(2006)**. The Multi-Source Interference Task: an fMRI task that
reliably activates the cingulo-frontal-parietal cognitive/attention network.
*Nat Protoc*, 1, 1:308-13. [PMID: 17406250](http://www.ncbi.nlm.nih.gov/pubmed/17406250).

The MSIT was developed as an all-purpose task to provide robust single-participant level activation of cognitive control and attentional regions in the brain (Bush and Shin, 2006). Early work with the MSIT suggests robust activation of regions associated with top-down control  – regions that are often active when the DMN is inactive. The MSIT provided a basis for directly examining task-induced deactivation of the DMN.

![Fig. 1 Example of stimuli.](msit_stim2.png?raw=true "Fig. 1 Example of vignettes.")

*Figure 1. Examples of task stimuli. For congruent trials, the paired digits are zero and the position of the target digit corresponds to its location. For incongruent trials, the distractor digits are non-zero and the target digits location is not the same as its value.*

During the task, participants are presented with a series of stimuli consisting of three digits, two of which were identical and one that differed from the other two (see Fig. 1 for examples). Participants are instructed to indicate the value and not the position of the digit that differed from the other two (e.g., 1 in 100, 1 in 221). During control trials, distractor digits are 0s and the targets are presented in the same location as they appear on the response box (e.g., 1 in 100 is the first button on the button box and the first number in the sequence). During interference trials, distractors are other digits and target digits are incongruent with the corresponding location on the button box (e.g., 221 – 1 is the first button on the button box but was the third number in the sequence).

The task is presented as a block design with eight 42-second blocks that alternated between conditions, starting with a control block. Each block contains 24 randomly generated stimuli with an inter-stimulus interval of 1.75 seconds. The task begins and ends with a 30 second fixation period during which the participants passively view a white dot centered on a black background.

## Example fMRI Activations

A group-level analysis of 124 participants from the openly shared [Enhanced Nathan Kline Institute - Rockland Sample Neurofeedback study](http://fcon_1000.projects.nitrc.org/indi/enhanced/) resulted in the incongruent > congruent activation pattern depicted in Figure 2a (p<0.001 TFCE FWE-corrected). Figure 2b illustrates the overlap of individual level results, each of which were corrected at p<0.05, uncorrected.

![Fig. 2 Areas activated in the incongruent > congruent contrast.](task_results.png?raw=true "Fig. 2 Areas activated in the incongruent > congruent contrast.")

*Figure 2. Areas activated in the incongruent > congruent contrast. A. Results of group-level analysis, thresholded at p<0.001 TFCE FWE-corrected. B. Overlap of individual level results, each thresholded at p<0.05 uncorrected.*

## Usage Notes
This task requires that the [PsychoPy](http://www.psychopy.org/) ecosystem be installed either as python libraries, or as a standalone application (available for Mac OSX and Microsoft Windows). For Debian systems (including Ubuntu), PsychoPy can be easily installed via [NeuroDebian](http://neuro.debian.net/pkgs/psychopy.html?highlight=psychopy).

The task can work with a keyboard or a Lumina button box. Once started, the task will ask the user to input a participant ID, which will be used for naming the output files, and to indicate whether the task should begin with a block of congruent or incongruent trials. Bush et al. 2013 recommends a fixed order (control first) across subjects.

Keyboard mapping:

    any key: starts the task
    esc: ends the task at any time
    1 or left arrow: 1
    2 or up arrow: 2
    3 or right arrow: 3

Button box mapping:

    trigger (receive '4' from Lumina box): starts the task
    button 1 (receive '0' from Lumina box): 1
    button 2 (receive '1' from Lumina box): 2
    button 3 (receive '2' from Lumina box): 3


The task instructions are derived directly from Bush et al. 2006, and are copied here for completeness:

    Instruct subjects that sets of three numbers (1, 2, 3 or 0)
    will appear in the center of the screen every few seconds,
    and that one number will always be different from the
    other two (matching distractor) numbers.

    Instruct subjects to report, via button-press, the identity
    of the number that is different from the other two numbers.
    Inform subjects that during some (control) trials, the target
    number (1, 2 or 3) always matches its position on the button
    press (e.g., the number '1' would appear in the first (leftmost)
    position). Sample trials are, therefore, 100, 020 or 003. Also
    inform subjects that during other (interference) trials, in
    contrast, the target (1, 2 or 3) never matches its position on
    the button press, and the distractors are themselves potential
    targets (e.g., 233, correct answer is '2').

    Explicitly instruct subjects: (a) that the sets of numbers will
    change about every 2 s (actual interstimulus interval for healthy
    adults is 1,750 ms), and (b) to “answer as quickly as possible,
    but since getting the correct answer is important, do not
    sacrifice accuracy for speed.

    Inform subjects that tasks will begin and end with fixation of a
    white dot for 30 s, and that between these times there will be
    two trial types (some with zeros and some without) that will
    appear in blocks that alternate every 42 s.

The task will create a Data/ directory in the current directory to store participant responses. Responses will be stored in .csv and .log files whose names include the participant ID entered by the user and the data and time the task was started.

## Scoring Responses
Responses and response times can be extracted from the output .csv files using the ```parse_msit.py``` Python script. This script requires the [Pandas](http://pandas.pydata.org/) library.

## Acknowledgements
Salary support was provided by NIMH BRAINS R01MH101555 to RCC.
