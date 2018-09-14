#!/usr/bin/python3
import subprocess
import time
import os

NODE_NAMESPACE="yoga"
SESSION_NAME="stack"

# Printout
print("Launching stack in a tmux session.")
print("This tmux session uses:")
print("Modifier: C-a")
print("Horizontal split: \"")
print("Vertical split: %")
print("Launching...")

# Find local directory
PATH=os.path.dirname(os.path.realpath(__file__))
print("PATH={}".format(PATH))

def start_new_tmux_session():
    command = "tmux new -s " + SESSION_NAME + " -d"
    subprocess.run(command, shell=True)

def launch_tmux_window(window_name):
    command = ("tmux new-window -t "
               + SESSION_NAME 
               + " -n " 
               + window_name)
    subprocess.run(command, shell=True)

def run_command_in_window(window_name, window_command, pane_number=0):
    command = ("tmux send -t " 
               + SESSION_NAME 
               + ":" 
               + window_name 
               + "."
               + str(pane_number)
               + " \""
               + window_command
               +"\" Enter")
    subprocess.run(command, shell=True)

def split_window(window_name, dimension, pane_number=0):
    """ Dimension is either -v for vertical or -h for horizontal """
    command = ("tmux split-window -t "
               + SESSION_NAME 
               + ":" 
               + window_name 
               + "."
               + str(pane_number)
               + " -d "
               + dimension)
    subprocess.run(command, shell=True)

def quarter_window(window_name):
    split_window(window_name, '-h', 0)
    split_window(window_name, '-v', 0)
    split_window(window_name, '-v', 2)

# Cleanly create pipes
subprocess.run("cd " + PATH + "; ../scripts/make_pipes.bash", shell=True);

# Create new tmux session
start_new_tmux_session()

## Launch PpRx 
window_name = "PpRx"
launch_tmux_window(window_name)
quarter_window(window_name)
window_command = "cd " + PATH + "; pprx -f snapon_pprx.opt"
run_command_in_window(window_name, window_command, 0)
# Connect the pipes
window_command = ("cd " + PATH+"; echo 'Piping...'; < pprx_write tee ppengine_read pprx.gbx > /dev/null")
run_command_in_window(window_name, window_command, 2)

## Launch PpEngine 
window_name = "PpEngine"
launch_tmux_window(window_name)
window_command = ("ppengine -f snapon_ppengine.opt")
run_command_in_window(window_name, window_command)

## Launch ROS core and nodes
window_name = "ROS"
launch_tmux_window(window_name)
quarter_window(window_name)
run_command_in_window(window_name, "roscore", 0)
time.sleep(2.5)
window_command = ("rostopic echo /" + NODE_NAMESPACE + "/local_odom")
#run_command_in_window(window_name, window_command, 1)
window_command = ("rosrun gbx2ros gbx2ros_node" +
    " --in " + PATH + "/ppengine_write" + 
    " --out " + NODE_NAMESPACE)
run_command_in_window(window_name, window_command, 2)
# Launch the visualizer
window_command = ("roslaunch gnss_visualization gnss.launch")
run_command_in_window(window_name, window_command, 3)

# Select window number 2 and attach to the tmux session
subprocess.run("tmux selectw -t 2", shell=True)
subprocess.run("tmux attach -t " + SESSION_NAME, shell=True)

