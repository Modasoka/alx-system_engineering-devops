# 0x0D. Web Stack Debugging #0

## Concepts

For this project, we explore the following concepts:

-   **Network Basics**: Understanding fundamental networking principles is essential for troubleshooting web stack issues, as many web applications rely heavily on network communication.
-   **Docker**: Docker is a popular containerization platform used for building, deploying, and managing applications. Understanding Docker is crucial for working with containerized environments.
-   **Web Stack Debugging**: Debugging web stacks involves identifying and resolving issues within the software components that make up a web application. It requires a deep understanding of web servers, databases, and other components.

## Background Context

The Web Stack Debugging series focuses on mastering the art of debugging. Debugging is a critical skill for Full-Stack Software Engineers, as it involves diagnosing and fixing issues in complex web applications.

In this debugging series, we are presented with broken or bugged web stacks and tasked with bringing them to a working state. The ultimate goal is to develop a Bash script that, when executed, resolves the issues automatically. However, before writing the Bash script, we must first diagnose the problems manually.

To illustrate this process, let's consider a simple example: a server that must have a copy of the `/etc/passwd` file in `/tmp` and a file named `/tmp/isworking` containing the string "OK." Without these elements, the web application cannot function properly.

## Installation of Docker

Docker provides a containerized environment that facilitates debugging tasks. If you want to experiment locally or solve the problem on your own machine, you can install Docker using the following instructions:

-   Mac OS
-   Windows
-   Ubuntu 14.04
-   Ubuntu 16.04

## Resources

**Man or Help:**

-   **curl**: A command-line tool for transferring data with URLs. Useful for testing web server responses and debugging network-related issues.

## Requirements

-   **Allowed Editors:** vi, vim, emacs
-   **Interpreted on:** Ubuntu 14.04 LTS
-   **File Endings:** All files should end with a new line
-   **README.md:** A mandatory file providing project overview and instructions
-   **Executable Scripts:** All Bash script files must be executable
-   **Shellcheck:** Bash scripts must pass Shellcheck without any errors
-   **Script Execution:** Bash scripts must run without error
-   **Script Header:** The first line of all Bash scripts should be `#!/usr/bin/env bash`
-   **Script Comments:** The second line of all Bash scripts should be a comment explaining the script's purpose

## Background context
The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let’s start with a very simple example. My server must:

-   have a copy of the  `/etc/passwd`  file in  `/tmp`
-   have a file named  `/tmp/isworking`  containing the string  `OK`

Let’s pretend that without these 2 elements, my web application cannot work.

Let’s go through this example and fix the server.
```
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
```
Then my answer file would contain:
```
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
```
Note that as you cannot use interactive software such as `emacs` or `vi` in your Bash script, everything needs to be done from the command line (including file edition).