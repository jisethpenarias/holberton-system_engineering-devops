<h1 class="gap">Project 0x04. Loops, conditions and parsing</h1>

<h2>Learning Objectives</h2>
<h3>General</h3>

<ul>
<li>How to create SSH keys</li>
<li>What is the advantage of using  <code>#!/usr/bin/env bash</code> over <code>#!/bin/bash</code></li>
<li>How to use <code>while</code>, <code>until</code> and <code>for</code> loops</li>
<li>How to use <code>if</code>, <code>else</code>, <code>elif</code> and <code>case</code> condition statements</li>
<li>How to use the <code>cut</code> command</li>
<li>What are files and other comparison operators, and how to use them</li>
</ul>

<h2>Requirements</h2>

<h3>General</h3>

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>You are not allowed to use <code>awk</code></li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

<h2>More Info</h2>

<h3>Shellcheck</h3>

<p><a href="https://github.com/koalaman/shellcheck" title="Shellcheck" target="_blank">Shellcheck</a> is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. <code>Shellcheck</code> is your friend! <strong>All your Bash scripts must pass <code>Shellcheck</code> without any error or you will not get any points on the task</strong>.</p>



      <h2 class="gap">Tasks</h2>
<h4 class="task">
    0. Create a SSH RSA key pair
</h4>
<p>Read for this task:</p>

<ul>
<li><a href="https://askubuntu.com/questions/61557/how-do-i-set-up-ssh-authentication-keys" title="Linux and Mac OS users" target="_blank">Linux and Mac OS users</a></li>
<li><a href="https://docs.rackspace.com/support/how-to/generating-rsa-keys-with-ssh-puttygen/" title="Windows users" target="_blank">Windows users</a></li>
</ul>

<p>man: <code>ssh-keygen</code></p>

<p>You will soon have to manage your own <strong>servers</strong> concept page hosted on remote <a href="/rltoken/e4-Q5Ebz_iidUZAkvrPyEA" title="data centers" target="_blank">data centers</a>. We need to set them up with your RSA public key so that you can access them via SSH.</p>

<p>Create a RSA key pair.</p>

<p>Requirements:</p>

<ul>
<li>Share your <strong>public key</strong> in your answer file <code>0-RSA_public_key.pub</code></li>
<li>Fill the <code>SSH public key</code> field of your <a href="/rltoken/Oxtupmk95xGx7_FFQ3WTbA" title="intranet profile" target="_blank">intranet profile</a> with the public key you just generated</li>
<li><strong>Keep the private key to yourself in a secure location</strong>, you will use it later to connect to your servers using SSH. Some storing ideas are Dropbox, Google Drive, password manager, USB key. Failing to do so will prevent you to access your servers, which will prevent you from doing your projects</li>
<li>If you decide to add a passphrase to your key, make sure to save this passphrase in a secure location, you will not be able to use your keys without the passphrase</li>
</ul>

<p>SSH and RSA keys will be covered in depth in a later project.</p>

<h4 class="task">
    1. For Holberton School loop
</h4>
<p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirement:</p>

<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
</ul>
<p>Note that: </p>

<ul>
<li>The first line of my Bash script starts with <code>#!/usr/bin/env bash</code></li>
<li>The second line of my Bash scripts is a comment explaining what it is doing</li>
</ul>

<h4 class="task">
    2. While Holberton School loop
</h4>
 <p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>

 <h4 class="task">
    3. Until Holberton School loop
</h4>
<p>Write a Bash script that displays <code>Holberton School</code> 10 times.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>until</code> loop (<code>for</code> and <code>while</code> are forbidden)</li>
</ul>

<h4 class="task">
    4. If 9, say Hi!
</h4>
<p>Write a Bash script that displays <code>Holberton School</code> 10 times, but for the 9th iteration, displays <code>Holberton School</code> <em>and then</em> <code>Hi</code> on a new line.</p>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code> statement</li>
</ul>

  <h4 class="task">
    5. 4 bad luck, 8 is your chance
</h4>
<p>Write a Bash script that loops from 1 to 10 and:</p>

<ul>
<li>displays <code>bad luck</code> for the 4th loop iteration</li>
<li>displays <code>good luck</code> for the 8th loop iteration</li>
<li>displays <code>Holberton School</code> for the other iterations</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>if</code>, <code>elif</code> and <code>else</code> statements</li>
</ul>

 <h4 class="task">
    6. Superstitious numbers
</h4>
<p>Write a Bash script that displays numbers from 1 to 20 and:</p>

<ul>
<li>displays <code>4</code> <em>and then</em> <code>bad luck from China</code> for the 4th loop iteration</li>
<li>displays <code>9</code> <em>and then</em> <code>bad luck from Japan</code> for the 9th loop iteration</li>
<li>displays <code>17</code> <em>and then</em> <code>bad luck from Italy</code> for the 17th loop iteration</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
<li>You must use the <code>case</code> statement</li>
</ul>


 <h4 class="task">
    7. Clock
</h4>
<p>Write a Bash script that displays the time for 12 hours and 59 minutes:</p>

<ul>
<li>display hours from 0 to 12</li>
<li>display minutes from 1 to 59</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>while</code> loop (<code>for</code> and <code>until</code> are forbidden)</li>
</ul>

<p>Note that in this example, we only display the first 70 lines using the <code>head</code> command.</p>

 <h4 class="task">
    8. For ls
</h4>
<p>Write a Bash script that displays:</p>

<ul>
<li>The content of the current directory</li>
<li>In a list format</li>
<li>Where only the part of the name after the first dash is displayed (refer to the example)</li>
</ul>

<p>Requirements:</p>

<ul>
<li>You must use the <code>for</code> loop (<code>while</code> and <code>until</code> are forbidden)</li>
<li>Do not display hidden files</li>
</ul>


 <h4 class="task">
    9. To file, or not to file
</h4>
<p>Write a Bash script that gives you information about the <code>holbertonschool</code> file.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>if</code> and, <code>else</code> (<code>case</code> is forbidden)</li>
<li>Your Bash script should check if the file exists and print:

<ul>
<li>if the file exists: <code>holbertonschool file exists</code></li>
<li>if the file does not exist: <code>holbertonschool file does not exist</code></li>
</ul></li>
<li>If the file exists, print:

<ul>
<li>if the file is empty: <code>holbertonschool file is empty</code></li>
<li>if the file is not empty: <code>holbertonschool file is not empty</code></li>
<li>if the file is a regular file: <code>holbertonschool is a regular file</code></li>
<li>if the file is not a regular file: (nothing)</li>
</ul></li>
</ul>


<h4 class="task">
    10. FizzBuzz
</h4>
<p>Write a Bash script that displays numbers from 1 to 100.</p>

<p>Requirements:</p>

<ul>
<li>Displays <code>FizzBuzz</code> when the number is a multiple of 3 and 5</li>
<li>Displays <code>Fizz</code> when the number is multiple of 3</li>
<li>Displays <code>Buzz</code> when the number is a multiple of 5</li>
<li>Otherwise, displays the number</li>
<li>In a list format</li>
</ul>

<p> Plus some advanced task </p>