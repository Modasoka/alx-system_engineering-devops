# 0x13. Firewall

## Resources

Read or watch:

-   [What is a firewall](https://intranet.alxswe.com/rltoken/vjB4LyHRdtEImzZcuD89ZQ)

## More Info

### Introduction

In the realm of computer security, a firewall acts as a barrier between a trusted network (like your server) and untrusted networks (like the internet). It monitors and controls incoming and outgoing network traffic based on predetermined security rules.

### Testing with Telnet

`Telnet` is a tool that helps check if sockets are open and can be used for debugging. When you `telnet` to a specific IP and port, it attempts to establish a connection. The provided examples show successful and unsuccessful attempts.

### Note on School Network

The school network filters outgoing connections through a network-based firewall. This means that testing outside certain ports on servers outside the school network may not work. To test your work on `web-01`, perform the test from outside the school network, such as from your `web-02` server.

### Warning!

Be extremely cautious when configuring firewall rules. For instance, blocking port 22/TCP (SSH) without considering the consequences may lead to being unable to reconnect to the server. When installing UFW (Uncomplicated Firewall), port 22 is blocked by default, so ensure to unblock it immediately before logging out of your server.

## Installing UFW and Setting Rules

### Steps

Follow these steps on your `web-01` server (or other relevant servers):

1.  **Install UFW:**
    
    bashCopy code
   ``` 
   sudo apt-get update
   sudo apt-get install -y ufw
   ```
    
2.  **Configure UFW to Block All Incoming Traffic:**
    
    ```
    sudo ufw default deny incoming
    ```
3.  **Allow Incoming Traffic on Specific Ports:**
    
    ```
    sudo ufw allow 22  # SSH
    sudo ufw allow 443  # HTTPS SSL
    sudo ufw allow 80  # HTTP
    ```
4.  **Enable UFW:**
    ```
    sudo ufw enable 
    ```
	Confirm with 'y' when prompted.
    
5.  **Verify UFW Status:**
    
    ```    
    sudo ufw status
    ```
    
    The output should show allowed ports (SSH, HTTPS, HTTP).
## N.B

Remember, firewall rules are crucial for securing your server, so make sure to understand the implications of the rules you set.