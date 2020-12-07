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

