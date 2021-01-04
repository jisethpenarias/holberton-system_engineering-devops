<h1 class="gap">0x12. Web stack debugging #2</h1>


<h2 class="gap">Tasks</h2>


<h4 class="task">
    0. Run software as another user
</h4>


<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/eaeff07a715ff880b1ceb8e863a1d141a74a7f85.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210104%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210104T124020Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=c4e79039dba0012427d4cdd3fd1759d85a056f30ddb82cff8499c250413d2645" alt="" style=""></p>

<p>The user <code>root</code> is, on Linux, the “superuser”. It can do anything it wants, that’s a good and bad thing. A good practice is that one should never be logged in the <code>root</code> user, as if you fat finger a command and for example run <code>rm -rf /</code>, there is no comeback. That’s why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the <code>root</code> user can do, just need to use a specific command that you need to discover.</p>

<p>For the containers that you are given in this project as well as the checker, everything is run under the <code>root</code> user, which has the ability to run anything as another user.</p>

<p>Requirements:</p>

<ul>
<li>write a Bash script that accepts one argument</li>
<li>the script should run the <code>whoami</code> command under the user passed as an argument</li>
<li>make sure to try your script by passing different users</li>
</ul>

<p>Example:</p>

<pre><code>root@ubuntu:~# whoami
root
root@ubuntu:~# ./0-iamsomeoneelse www-data
www-data
root@ubuntu:~# whoami
root
root@ubuntu:~#
</code></pre>
