The Multi-Source Interference Task
==================================

This PsychoPy implementation of the Multi-source Interference Task (MSIT)
conforms to the implementation described in: 

Bush, G, Shin, LM **(2006)**. The Multi-Source Interference Task: an fMRI task that
reliably activates the cingulo-frontal-parietal cognitive/attention network.
*Nat Protoc*, 1, 1:308-13. [PMID: 17406250](http://www.ncbi.nlm.nih.gov/pubmed/17406250).

To use this task you must install [PsychoPy](http://www.PsychoPy.org/) which
can be installed as either a python library, or standalone. 

The code can be executed by loading and running "MSIT.py" in PsychoPy.  The
task can work with a keyboard or a Lumina button box. It can be started by
either pressing any key on the keyboard or by a trigger sent through the Lumina
box (for use during an fMRI).


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

Task performance is recorded in a .csv file and a .log file that can be found
in the data/ directory.

The stimuli used during the task are broken into blocks of control and
interference trials. The exact stimuli are randomized, and should be different
for every run. The order of control and interference blocks (i.e. which one
	comes first) can be specified at the beggining of the task, although Bush
	et al. 2013 recommends a fixed order (control first) across subjects. 


The task instructions are derived directly from Bush et al. 2006, and are
copied here for completeness:

    Instruct subjects that sets of three numbers (1, 2, 3 or 0) will appear in the
    center of the screen every few seconds, and that one number will always be
    different from the other two (matching distractor) numbers.

    Instruct subjects to report, via button-press, the identity of the number that
    is different from the other two numbers. Inform subjects that during some
    (control) trials, the target number (1, 2 or 3) always matches its position on
    the button press (e.g., the number '1' would appear in the first (leftmost)
    position). Sample trials are, therefore, 100, 020 or 003. Also inform subjects
    that during other (interference) trials, in contrast, the target (1, 2 or 3)
    never matches its position on the button press, and the distractors are
    themselves potential targets (e.g., 233, correct answer is '2').

    Explicitly instruct subjects: (a) that the sets of numbers will change about
    every 2 s (actual interstimulus interval for healthy adults is 1,750 ms), and
    (b) to “answer as quickly as possible, but since getting the correct answer is
    important, do not sacrifice accuracy for speed.”

    Inform subjects that tasks will begin and end with fixation of a white dot
    for 30 s, and that between these times there will be two trial types (some
    with zeros and some without) that will appear in blocks that
    alternate every 42 s. 
	    
