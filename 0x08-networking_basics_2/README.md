<h1 class="gap">0x08. Networking basics #1</h1>

 <article id="description" class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png" alt="" style=""></p>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/yAdXy8r8At9LC7fz5uv8ew" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is localhost/127.0.0.1</li>
<li>What is 0.0.0.0</li>
<li>What is <code>/etc/hosts</code></li>
<li>How to display your machine’s active network interfaces</li>
</ul>

<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Localhost
  </h4>

<p>What is <code>localhost</code>?</p>

<ol>
<li>A hostname that means <em>this IP</em></li>
<li>A hostname that means <em>this computer</em></li>
<li>An IP attached to a computer</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x08-networking_basics_2</code></li>
    <li>File: <code>0-localhost</code></li>
</ul>

<br>
</br>

<h4 class="task">
    1. All IPs
</h4>
<p>What is <code>0.0.0.0</code>?</p>

<ol>
<li>All IPv4 addresses on the local machine</li>
<li>All the IPs</li>
<li>It means null in networking</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x08-networking_basics_2</code></li>
    <li>File: <code>1-wildcard</code></li>
</ul>

<br>
</br>
 <h4 class="task">
    2. Change your home IP
</h4>
<p>Write a Bash script that configures an Ubuntu server with the below requirements.</p>

<p>Requirements:</p>

<ul>
<li><code>localhost</code> resolves to <code>127.0.0.2</code></li>
<li> <code>facebook.com</code> resolves to <code>8.8.8.8</code>.</li>
<li> The checker is running on Docker, so make sure to read <a href="/rltoken/8PP1z09aHTqgTjyvET6-hg" title="this" target="_blank">this</a></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./2-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms
</code></pre>

<p>In this example we can see that:</p>

<ul>
<li>before running the script, <code>localhost</code> resolves to <code>127.0.0.1</code> and <code>facebook.com</code> resolves to <code>157.240.11.35</code></li>
<li>after running the script,  <code>localhost</code> resolves to <code>127.0.0.2</code> and <code>facebook.com</code> resolves to <code>8.8.8.8</code></li>
</ul>

<p>If you’re running this script on a machine that you’ll continue to use, be sure to revert <code>localhost</code> to <code>127.0.0.1</code>. Otherwise, a lot of things will stop working!</p>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x08-networking_basics_2</code></li>
    <li>File: <code>2-change_your_home_IP</code></li>
</ul>


<br>
</br>
<h4 class="task">
    3. Show attached IPs
</h4>
<p>Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.</p>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./3-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
</code></pre>

<p>Obviously, the IPs displayed may be different depending on which machine you are running the script on.</p>

<p>Note that we can see our <code>localhost</code> IP :)</p>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x08-networking_basics_2</code></li>
    <li>File: <code>3-show_attached_IPs</code></li>
</ul>

<br>
</br>