# 0x05. Processes and Signals

## Resources

Read or watch:

-   Linux PID
-   Linux Process
-   Linux Signal
-   Process Management in Linux

Man or help:

-   `ps`
-   `pgrep`
-   `pkill`
-   `kill`
-   `exit`
-   `trap`

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

-   **What is a PID?**
    
    -   PID stands for Process ID. It is a unique identifier assigned to each process in a Unix-like operating system. Understanding PIDs is crucial for managing and interacting with processes.
-   **What is a Process?**
    
    -   A process is a program in execution. It is an independent entity that runs in the system and performs a specific task. Knowing how to identify and manage processes is fundamental.
-   **How to Find a Process’ PID?**
    
    -   Various tools like `ps`, `pgrep`, and `pkill` can be used to find the PID of a process. Knowing these tools and their options is essential for process management.
-   **How to Kill a Process?**
    
    -   Killing a process is terminating its execution. The `kill` command is commonly used for this purpose. Understanding how to use it properly is crucial for managing processes.
-   **What is a Signal?**
    
    -   A signal is a software interrupt delivered to a process. It is a way for processes to communicate with each other. Understanding signals is vital for handling process behavior.
-   **What are the 2 Signals That Cannot Be Ignored?**
    
    -   SIGKILL (9) and SIGSTOP (19/17) are signals that cannot be ignored. SIGKILL forcefully terminates a process, and SIGSTOP pauses a process.

## Copyright - Plagiarism

You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

-   Allowed editors: vi, vim, emacs
-   All your files will be interpreted on Ubuntu 20.04 LTS
-   All your files should end with a new line
-   A README.md file, at the root of the folder of the project, is mandatory
-   All your Bash script files must be executable
-   Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error
-   The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
-   The second line of all your Bash scripts should be a comment explaining what is the script doing
