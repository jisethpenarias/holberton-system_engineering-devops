<h1 class="gap">0x0C. Web server</h1>

<h2>Background Context</h2>

<p><a href="https://www.youtube.com/watch?v=AZg4uJkEa-4&amp;feature=youtu.be&amp;hd=1" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/Screenshot+2017-07-06+19.24.05.png" alt="" style=""></a></p>

<p>In this project, some of the tasks will be graded on 2 aspects:</p>

<ol>
<li>Is your <code>web-01</code> server configured according to requirements</li>
<li>Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)</li>
</ol>

<p>For example, if I need to create a file <code>/tmp/test</code> containing the string <code>hello world</code> and modify the configuration of Nginx to listen on port <code>8080</code> instead of <code>80</code>, I can use <code>emacs</code> on my server to create the file and to modify the Nginx configuration file <code>/etc/nginx/sites-enabled/default</code>.</p>

<p>But my answer file would contain:</p>

<pre><code>sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world &gt; /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
</code></pre>

<p>As you can tell, I am not using <code>emacs</code> to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an <a href="/rltoken/Hjv9yJQtW6X7VRa2ByMeEg" title="SRE" target="_blank">SRE</a>, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the <code>root</code> user, you do not need to use the <code>sudo</code> command.</p>

<p>A good Software Engineer is a <a href="/rltoken/y1MX-uAX-0a4bgXfH3uweQ" title="lazy Software Engineer" target="_blank">lazy Software Engineer</a>.
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" alt="" style=""></p>

<p>Tips: to test your answer Bash script, feel free to reproduce the checker environment: </p>

<ul>
<li>start an <code>ubuntu:16.04</code> Docker container</li>
<li>run your script on it</li>
<li>see how it behaves</li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/lGyY_30FRBmgKhisGmKd1A" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is the main role of a web server</li>
<li>What is a child process</li>
<li>Why web servers usually have a parent process and child processes</li>
<li>What are the main HTTP requests</li>
</ul>

<h3>DNS</h3>

<ul>
<li>What DNS stands for</li>
<li>What is DNS main role</li>
</ul>

<h3>DNS Record Types</h3>

<ul>
<li><code>A</code></li>
<li><code>CNAME</code></li>
<li><code>TXT</code></li>
<li><code>MX</code></li>
</ul>


   0. Transfer a file to your server
  </h4>

<p>Write a Bash script that transfers a file from our client to a server:</p>

<p>Requirements:</p>

<ul>
<li>Accepts 4 parameters

<ol>
<li>The path to the file to be transferred</li>
<li>The IP of the server we want to transfer the file to</li>
<li>The username <code>scp</code> connects with</li>
<li>The path to the SSH private key that <code>scp</code> uses</li>
</ol></li>
<li>Display <code>Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY</code> if less than 3 parameters passed</li>
<li><code>scp</code> must transfer the file to the user home directory <code>~/</code></li>
<li>Strict host key checking must be disabled when using <code>scp</code> </li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
</code></pre>

<p>In this example, I:</p>

<ul>
<li>remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see what <code>~/</code> contains</li>
<li>create a file named <code>some_page.html</code></li>
<li>execute my <code>0-transfer_file</code> script</li>
<li> remotely execute the <code>ls ~/</code> command via <code>ssh</code> to see that the file <code>some_page.html</code> has been successfully transferred</li>
</ul>

<p>That is one way of publishing your website pages to your server.</p>

  <h4 class="task">
    1. Install nginx web server
  </h4>


<p>Web servers are the piece of software generating and serving HTML pages, let’s install one!</p>

<p>Requirements:</p>

<ul>
<li>Install <code>nginx</code> on your <code>web-01</code> server</li>
<li>Nginx should be listening on port 80</li>
<li>When querying Nginx at its root <code>/</code> with a GET request (requesting a page)  using <code>curl</code>, it must return a page that contains the string <code>Holberton School</code></li>
<li>As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)</li>
<li>You can’t use <code>systemctl</code> for restarting <code>nginx</code></li>
</ul>

<p>Server terminal:</p>

<pre><code>root@sy-web-01$ ./1-install_nginx_web_server &gt; /dev/null 2&gt;&amp;1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Holberton School for the win!
root@sy-web-01$ 
</code></pre>

<p>Local terminal:</p>

<pre><code>sylvain@ubuntu$ curl 34.198.248.145/
Holberton School for the win!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>

<p>In this example <code>34.198.248.145</code> is the IP of my <code>web-01</code> server. If you want to query the Nginx that is locally installed on your server, you can use <code>curl 127.0.0.1</code>.</p>

<p>If things are not going as expected, make sure to check out Nginx logs, they can be found in <code>/var/log/</code>.</p>


  <h4 class="task">
    2. Setup a domain name
  </h4>

<p><a href="/rltoken/yRrwiHrS15iQQZku72p0aQ" title=".TECH Domains" target="_blank">.TECH Domains</a> is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. Holberton School partnered with .TECH Domains so that you can learn about DNS.</p>

<p>.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your <a href="/rltoken/b-Y81kiPBFJ_6wxJaSmBgQ" title="tools space" target="_blank">tools space</a>. Feel free to drop a thank you tweet for <a href="/rltoken/d9XjYlM-CqTRHJEcaKpcVQ" title=".TECH Domains" target="_blank">.TECH Domains</a>.</p>

<p>Provide the domain name in your answer file.</p>

<p>Requirement:</p>

<ul>
<li>provide the domain name only (example: <code>foobar.tech</code>), no subdomain (example: <code>www.foobar.tech</code>)</li>
<li>configure your DNS records with an A entry so that your root domain points to your <code>web-01</code> IP address <strong>Warning: the propagation of your records can take time (~1-2 hours)</strong></li>
<li>go to <a href="/rltoken/7s2XnwohTKBNE8c_ibAt4g" title="your profile" target="_blank">your profile</a> and enter your domain in the <code>Project website url</code> field</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ cat 2-setup_a_domain_name
holbertonschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig holbertonschool.tech

; &lt;&lt;&gt;&gt; DiG 9.10.6 &lt;&lt;&gt;&gt; holbertonschool.tech
;; global options: +cmd
;; Got answer:
;; -&gt;&gt;HEADER&lt;&lt;- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;holbertonschool.tech.      IN  A

;; ANSWER SECTION:
holbertonschool.tech.   7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
</code></pre>

<p>When your domain name is setup, please verify the Registrar here: <a href="/rltoken/s8vsjayVUHJza59GXtuzpw" title="https://whois.whoisxmlapi.com/" target="_blank">https://whois.whoisxmlapi.com/</a>  and you must see in the JSON response: <code>"registrarName": "Dotserve Inc"</code></p>


  <h4 class="task">
    3. Redirection
  </h4>


<p>Configure your Nginx server so that <code>/redirect_me</code> is redirecting to another page.</p>

<p>Requirements:</p>

<ul>
<li>The redirection must be a “301 Moved Permanently”</li>
<li>You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements</li>
<li>Using what you did with <code>1-install_nginx_web_server</code>, write <code>3-redirection</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
</code></pre>


  <h4 class="task">
    4. Not found page 404
  </h4>


<p>Configure your Nginx server to have a custom 404 page that contains the string <code>Ceci n'est pas une page</code>.</p>

<p>Requirements:</p>

<ul>
<li>The page must return an HTTP 404 error code</li>
<li>The page must contain the string <code>Ceci n'est pas une page</code></li>
<li>Using what you did with <code>3-redirection</code>, write <code>4-not_found_page_404</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
</code></pre>
