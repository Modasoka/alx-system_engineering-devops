# 0x10. HTTPS SSL

## Project Overview

In this project, we delve into the world of HTTPS (Hypertext Transfer Protocol Secure) and SSL (Secure Sockets Layer). We'll explore the fundamental concepts of these technologies and gain insights into securing web communications.

## Learning Objectives

### General Concepts

1.  **What is HTTPS SSL?**
    
    -   HTTPS (Hypertext Transfer Protocol Secure) is a secure version of HTTP, the protocol used for transferring data between a user's web browser and a website. SSL (Secure Sockets Layer) is the technology that provides a secure and encrypted connection between the user and the website.
2.  **Roles of HTTPS SSL:**
    
    -   Authentication: Verifying the identity of the website.
    -   Encryption: Protecting the data exchanged between the user and the website from unauthorized access.
3.  **Purpose of Encrypting Traffic:**
    
    -   To ensure that sensitive data, such as login credentials or personal information, remains confidential during transmission over the internet.
4.  **SSL Termination:**
    
    -   SSL termination refers to the process of decrypting encrypted SSL/TLS traffic at the load balancer or server before passing it to the backend servers. This allows for inspection and manipulation of the unencrypted traffic.

### Project-Specific Concepts

1.  **DNS (Domain Name System):**
    
    -   DNS is a system that translates human-readable domain names (like [www.example.com](http://www.example.com/)) into IP addresses. It plays a crucial role in routing traffic to the correct web servers.
2.  **Web Stack Debugging:**
    
    -   Web stack debugging involves identifying and fixing issues in the technology stack that powers a web application, including the web server, application server, and database.
3.  **HAProxy SSL Termination:**
    
    -   HAProxy is a load balancer that can handle SSL termination, offloading the SSL/TLS decryption process from the backend servers.
4.  **Bash Function:**
    
    -   A Bash function is a set of reusable code that performs a specific task. Functions enhance code modularity and maintainability.

## Resources

### Read or Watch

-   What is HTTPS?
-   What are the 2 main elements that SSL is providing
-   HAProxy SSL termination on Ubuntu 16.04
-   SSL termination

### man or help

-   `awk`: A versatile programming language for text processing.
-   `dig`: A command-line tool for querying DNS name servers.
-   `Shellcheck (version 0.3.7)`: A static analysis tool for shell scripts.

## Requirements

### General

-   **Allowed Editors:** vi, vim, emacs
-   **Operating System:** Ubuntu 16.04 LTS
-   **File Endings:** All files should end with a new line.
-   **README.md:** A mandatory README.md file at the root of the project folder.
-   **Executable Bash Scripts:** All Bash script files must be executable.
-   **Shellcheck:** Bash scripts must pass Shellcheck (version 0.3.7) without any errors.
-   **Script Headers:** The first line of all Bash scripts should be `#!/usr/bin/env bash`, and the second line should be a comment explaining the script's purpose.