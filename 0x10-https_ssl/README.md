<h1 class="gap">0x10. HTTPS SSL</h1>
    <p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png" alt="" style=""></p>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/g3QKIYYal8LdrwZdp_PHxw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is HTTPS SSL 2 main roles</li>
<li>What is the purpose encrypting traffic</li>
<li>What SSL termination means</li>

<h2 class="gap">Tasks</h2>

 <h4 class="task">
    0. HTTPS ABC
  </h4>

  <p>As for project <a href="/rltoken/yZFuXOcQDP7ceusbLCr3Dw" title="0x07" target="_blank">0x07</a>, use numbers in your answer file.</p>

<p>What is HTTPS?</p>

<ol>
<li>A secure version of HTTP</li>
<li>A faster version of HTTP</li>
<li>A superior version of HTTP</li>
</ol>

<p>Why do you need HTTPS?</p>

<ol>
<li>To encrypt credit card and social security number information going between the client and the website servers</li>
<li>To encrypt all communication between the client and the website servers</li>
<li>To accelerate the communication between the client and the website servers</li>
</ol>

<p>You want to setup HTTPS on your website, where shall you place the certificate?</p>

<ol>
<li>In a secure location where nobody can access it</li>
<li>You can host it anywhere but you have to share the link to it on your website</li>
<li>On your website web server(s)</li>
</ol>


<h4 class="task">
    1. World wide web
  </h4>

<p>Configure your domain zone so that the subdomain <code>www</code> points to your load-balancer IP (<code>lb-01</code>).
Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</p>

<p>Requirements:</p>

<ul>
<li>Add the subdomain <code>www</code> to your domain, point it to your <code>lb-01</code> IP (your domain name might  be configured with default subdomains, feel free to remove them)</li>
<li>Add the subdomain <code>lb-01</code> to your domain, point it to your <code>lb-01</code> IP</li>
<li>Add the subdomain <code>web-01</code> to your domain, point it to your <code>web-01</code> IP</li>
<li>Add the subdomain <code>web-02</code> to your domain, point it to your <code>web-02</code> IP</li>
<li>Your Bash script must accept 2 arguments:

<ol>
<li><code>domain</code>:

<ul>
<li> type: string</li>
<li> what: domain name to audit</li>
<li>mandatory: yes</li>
</ul></li>
<li><code>subdomain</code>:

<ul>
<li>type: string</li>
<li>what: specific subdomain to audit</li>
<li>mandatory: no</li>
</ul></li>
</ol></li>
<li>Output:  <code>The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]</code></li>
<li>When only the parameter <code>domain</code> is provided, display information for its subdomains <code>www</code>, <code>lb-01</code>, <code>web-01</code> and <code>web-02</code> - in this specific order</li>
<li>When passing <code>domain</code> and <code>subdomain</code> parameters, display information for the specified subdomain</li>
<li>Ignore <code>shellcheck</code> case <code>SC2086</code></li>
<li>Must use: 

<ul>
<li><code>awk</code></li>
<li>at least one Bash function</li>
</ul></li>
<li>You do not need to handle edge cases such as:

<ul>
<li>Empty parameters </li>
<li>Nonexistent domain names</li>
<li>Nonexistent subdomains</li>
</ul></li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./1-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
</code></pre>

 <h4 class="task">
    2. HAproxy SSL termination
  </h4>

<p>“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.</p>

<p>Create a certificate using <code>certbot</code> and configure <code>HAproxy</code> to accept encrypted traffic for your subdomain <code>www.</code>.</p>

<p>Requirements:</p>

<ul>
<li>HAproxy must be listening on port TCP 443</li>
<li>HAproxy must be accepting SSL traffic</li>
<li>HAproxy must serve encrypted traffic that will return the <code>/</code> of your web server</li>
<li>When querying the root of your domain name, the page returned must contain <code>Holberton School</code></li>
<li>Share your HAproxy config as an answer file (<code>/etc/haproxy/haproxy.cfg</code>)</li>
</ul>

<p>The file <code>2-haproxy_ssl_termination</code> must be your HAproxy configuration file</p>

<p>Make sure to install HAproxy 1.5 or higher, <a href="/rltoken/VFq2MQ9qHXw2Nb11tnWF6Q" title="SSL termination" target="_blank">SSL termination</a> is not available before v1.5.</p>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
</code></pre>
