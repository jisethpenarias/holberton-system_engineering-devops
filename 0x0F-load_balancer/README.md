<h1 class="gap">0x0F. Load balancer</h1>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png" alt="" style=""></p>

<h2>Background Context</h2>

<p>You have been given 2 additional servers:</p>

<ul>
<li>gc-[STUDENT_ID]-web-02-XXXXXXXXXX</li>
<li>gc-[STUDENT_ID]-lb-01-XXXXXXXXXX</li>
</ul>

<p>Let’s improve our web stack so that there is <a href="/rltoken/QiOC_I-8BeV4aNExIucC9Q" title="redundancy" target="_blank">redundancy</a> for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.</p>

<p>For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.</p>

<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Double the number of webservers
  </h4>

<p>In this first task you need to configure <code>web-02</code> to be identical to <code>web-01</code>. Fortunately, you built a Bash script during your <a href="/rltoken/YygI112jB085j-4C3dRX2A" title="web server project" target="_blank">web server project</a>, and they’ll now come in handy to easily configure <code>web-02</code>. Remember, always try to automate your work!</p>

<p>Since we’re placing our web servers behind a load balancer for this project, we want to add a custom Nginx response header. The goal here is to be able to track which web server is answering our HTTP requests, to understand and track the way a load balancer works. More in the coming tasks.</p>

<p>Requirements:</p>

<ul>
<li>Configure Nginx so that its HTTP response contains a custom header (on <code>web-01</code> and <code>web-02</code>)

<ul>
<li>The name of the custom HTTP header must be <code>X-Served-By</code></li>
<li>The value of the custom HTTP header must be the hostname of the server Nginx is running on</li>
</ul></li>
<li>Write <code>0-custom_http_response_header</code> so that it configures a brand new Ubuntu machine to the requirements asked in this task

<ul>
<li><a href="/rltoken/3AOvROMUNUrzxEWhli4GTw" title="Ignore" target="_blank">Ignore</a> <a href="/rltoken/i5f8DYX_rRYFz4hfbG_GJg" title="SC2154" target="_blank">SC2154</a> for <code>shellcheck</code></li>
</ul></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI 34.198.248.145 | grep X-Served-By
X-Served-By: 03-web-01
sylvain@ubuntu$ curl -sI 54.89.38.100 | grep X-Served-By
X-Served-By: 03-web-02
sylvain@ubuntu$
</code></pre>

<p>If your server’s hostnames are not properly configured (<code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>.), follow this <a href="/rltoken/h3tE_15RKe2QYWzPsjqNDA" title="tutorial" target="_blank">tutorial</a>.</p>


<h4 class="task">
    1. Install your load balancer
</h4>

<!-- Task Body -->
  <p>Install and configure HAproxy on your <code>lb-01</code> server.</p>

<p>Requirements:</p>

<ul>
<li>Configure HAproxy with version equal or greater than 1.5 so that it send traffic to <code>web-01</code> and <code>web-02</code></li>
<li>Distribute requests using a roundrobin algorithm</li>
<li>Make sure that HAproxy can be managed via an init script</li>
<li>Make sure that your servers are configured with the right hostnames: <code>[STUDENT_ID]-web-01</code> and <code>[STUDENT_ID]-web-02</code>. If not, follow this <a href="/rltoken/Tb9qeqRrtrO_b2uFpet9rw" title="tutorial" target="_blank">tutorial</a>.</li>
<li>For your answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:17 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes

sylvain@ubuntu$ curl -Is 54.210.47.110
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Mon, 27 Feb 2017 06:12:19 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
X-Served-By: 03-web-02
Accept-Ranges: bytes

sylvain@ubuntu$
</code></pre>
