<h1 class="gap">0x0E. Web stack debugging #1</h1>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg" alt="" style=""></p>


<h2 class="gap">Tasks</h2>


<h4 class="task">
    0. Nginx likes port 80
</h4>

<p>Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port <code>80</code>. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.</p>

<p>Requirements:</p>

<ul>
<li>Nginx must be running, and listening on port <code>80</code> of all the server’s active IPv4 IPs </li>
<li>Write a Bash script that configures a server to the above requirements</li>
</ul>

<pre><code>root@966c5664b21f:/# curl 0:80
curl: (7) Failed to connect to 0 port 80: Connection refused
root@966c5664b21f:/#
root@966c5664b21f:/# ./0-nginx_likes_port_80 &gt; /dev/null 2&amp;&gt;1
root@966c5664b21f:/#
root@966c5664b21f:/# curl 0:80
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
&lt;title&gt;Welcome to nginx!&lt;/title&gt;
&lt;style&gt;
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
&lt;h1&gt;Welcome to nginx!&lt;/h1&gt;
&lt;p&gt;If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.&lt;/p&gt;

&lt;p&gt;For online documentation and support please refer to
&lt;a href="http://nginx.org/"&gt;nginx.org&lt;/a&gt;.&lt;br/&gt;
Commercial support is available at
&lt;a href="http://nginx.com/"&gt;nginx.com&lt;/a&gt;.&lt;/p&gt;

&lt;p&gt;&lt;em&gt;Thank you for using nginx.&lt;/em&gt;&lt;/p&gt;
&lt;/body&gt;
&lt;/html&gt;
root@966c5664b21f:/#
</code></pre>
