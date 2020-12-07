<h1 class="gap">0x0B. SSH</h1>

<h2>Background Context</h2>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/244/zPVRKhPsUP5lK.gif" alt="" style=""></p>

<p>Along with this project, you have been attributed an Ubuntu server, living in a datacenter far far away.  Like level 2 of the application process, you will connect using <code>ssh</code>. But contrary to level 2, you will not connect using a password but an RSA key. We’ve configured your server with the public key you created in the first task of <a href="/rltoken/LZ_8pMANOAmpn5-tiwqiJQ" title="a previous project" target="_blank">a previous project</a> shared in your <a href="/rltoken/l4Ao4ESbI_hMB6s4mjBKRw" title="intranet profile" target="_blank">intranet profile</a>.</p>

<p>You can access your server information in the <a href="/rltoken/owYhGMuyPTY4OyvSGJljGQ" title="my servers" target="_blank">my servers</a> section of the intranet, each line with contains the IP and username you should use to connect via <code>ssh</code>.</p>

<p><strong>Note:</strong> Your server is configured with an Ubuntu 16.04 LTS environment. You do <strong>not</strong> need to create a new virtual machine. If you decide you want to upgrade to Ubuntu 16.04, make sure to create a new VM. Do <strong>not</strong> attempt to upgrade your current Ubuntu 14.04 environment as that will inevitably be messy and can break things. Note that if you switch, none of your files and environment settings will be available and anything you need will have to be reinstalled or migrated.</p>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/PXE-o9DWronMp4ETwADOpg" title="What is a (physical) server - text" target="_blank">What is a (physical) server - text</a> </li>
<li><a href="/rltoken/IfLc3lxSs4w5xdsFlRDPWw" title="What is a (physical) server - video" target="_blank">What is a (physical) server - video</a> </li>
<li><a href="/rltoken/qKJi0RXLqaCLkHLCLhiYNA" title="SSH essentials" target="_blank">SSH essentials</a> </li>
<li><a href="/rltoken/DNiFD9w9Gx0mnQk5nXbtjg" title="SSH Config File" target="_blank">SSH Config File</a></li>
<li><a href="/rltoken/ZBYjVLcJ-ck-CFjndgSDBw" title="Public Key Authentication for SSH" target="_blank">Public Key Authentication for SSH</a></li>
<li><a href="/rltoken/SW2m2e0KMA2K1dXk_0M0CA" title="How Secure Shell Works" target="_blank">How Secure Shell Works</a></li>
<li><a href="/rltoken/8N-RlUma9lwGfyZp1_C-Wg" title="SSH Crash Course" target="_blank">SSH Crash Course</a> (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)</li>
</ul>

<p><strong>For reference:</strong></p>

<ul>
<li> <a href="/rltoken/6mtNBCxYkoBQJ2vJ6TcRYA" title="Understanding the SSH Encryption and Connection Process" target="_blank">Understanding the SSH Encryption and Connection Process</a></li>
<li><a href="/rltoken/c1Yj55AE6gGkDxpACdY1vg" title="Secure Shell Wiki" target="_blank">Secure Shell Wiki</a></li>
<li><a href="/rltoken/GXZWV9hhtZN1-WnRkRSoUg" title="IETF RFC 4251 (Description of the SSH Protocol)" target="_blank">IETF RFC 4251 (Description of the SSH Protocol)</a></li>
<li><a href="/rltoken/bH7JrEiKN4Q6-J58d9pAsw" title="Internet Engineering Task Force" target="_blank">Internet Engineering Task Force</a></li>
<li><a href="/rltoken/lDe2f7hVqQPPCNr5i2zE-g" title="Request for Comments" target="_blank">Request for Comments</a></li>
</ul>

<p><strong>man or help</strong>:</p>

<ul>
<li><code>ssh</code></li>
<li><code>ssh-keygen</code></li>
<li><code>env</code></li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/yrpqgxdgQKwr3vYfhBpA_w" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a server</li>
<li>Where servers usually live</li>
<li>What is SSH</li>
<li>How to create an SSH RSA key pair</li>
<li>How to connect to a remote host using an SSH RSA key pair</li>
<li>The advantage of using  <code>#!/usr/bin/env bash</code> instead of <code>/bin/bash</code> </li>
</ul>

<h2 class="gap">Tasks</h2>


  <h4 class="task">
    0. Use a private key
  </h4>


<p>Write a Bash script that uses <code>ssh</code> to connect to your server using the private key <code>~/.ssh/holberton</code> with the user <code>ubuntu</code>.</p>

<p>Requirements:</p>

<ul>
<li>Only use <code>ssh</code> single-character flags</li>
<li>You cannot use <code>-l</code></li>
<li>You do not need to handle the case of a private key protected by a passphrase</li>
</ul>

<pre><code>sylvain@ubuntu$ ./0-use_a_private_key
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

0 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Fri Feb  3 01:12:16 2017 from 104.7.14.91
ubuntu@server01:~$ logout
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 
</code></pre>


  <h4 class="task">
    1. Create an SSH key pair
  </h4>

<p>Write a Bash script that creates an RSA key pair.</p>

<p>Requirements:</p>

<ul>
<li>Name of the created private key must be <code>holberton</code></li>
<li>Number of bits in the created key to be created 4096</li>
<li>The created key must be protected by the passphrase <code>betty</code></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in holberton.
Your public key has been saved in holberton.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair holberton  holberton.pub
sylvain@ubuntu$ 
</code></pre>


 <h4 class="task">
    2. Client configuration file
</h4>

 <p>Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password.
Share your SSH client configuration in your answer file.</p>

<p>Requirements:</p>

<ul>
<li>Your SSH client configuration must be configured to use the private key <code>~/.ssh/holberton</code></li>
<li>Your SSH client configuration must be configured to refuse to authenticate using a password</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to 98.98.98.98 [98.98.98.98] port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/holberton type -1
debug1: identity file /home/sylvain/.ssh/holberton-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.7
debug1: Remote protocol version 2.0, remote software version OpenSSH_7.2p2 Ubuntu-4ubuntu2.1
debug1: match: OpenSSH_7.2p2 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server-&gt;client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client-&gt;server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/holberton
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
Welcome to Ubuntu 16.04.1 LTS (GNU/Linux 4.4.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

112 packages can be updated.
0 updates are security updates.


*** System restart required ***
Last login: Mon Feb 20 18:26:38 2017 from 104.7.14.91
ubuntu@magic-server:~$
</code></pre>

<p>In the example above, we can see that <code>ssh</code> tries to authenticate using <code>holberton</code> and does not try to authenticate using a password. You can replace <code>98.98.98.98</code> by the IP of your server for testing purposes.</p>

<h4 class="task">
    3. Let me in!
  </h4>

<p>Now that you have successfully connected to your server, we would also like to join the party.</p>

<p>Add the SSH public key below to your server so that we can connect using the <code>ubuntu</code> user.</p>

<pre><code>ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
</code></pre>
