<h1 class="gap">0x13. Firewall</h1>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/284/V1HjQ1Y.png" alt="" style=""></p>


<h2>Background Context</h2>

<h3>Your servers without a firewall…</h3>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/155/holbertonschool-firewall.gif" alt="" style=""></p>

<h2 class="gap">Tasks</h2>


<h4 class="task">
    0. Firewall ABC
  </h4>


<p>Pick one answer for every question.</p>

<p>What is a firewall?</p>

<ol>
<li>A hardware security system</li>
<li>A hardware or software security system</li>
<li>A software security system</li>
</ol>

<p>What are the 2 types of firewall:</p>

<ol>
<li>Soft and hard firewall</li>
<li>Incoming and outgoing firewall</li>
<li>Network and host-based firewall</li>
</ol>

<p>What is the main function of a firewall?</p>

<ol>
<li>To filter incoming and outgoing network traffic</li>
<li>To filter  incoming and outgoing TCP traffic</li>
<li>To  filter outgoing traffic</li>
</ol>


  <h4 class="task">
    1. Block all incoming traffic but
  </h4>

<p>Let’s install the <code>ufw</code> firewall and setup a few rules on <code>web-01</code>.</p>

<p>Requirements:</p>

<ul>
<li>The requirements below must be applied to <code>web-01</code> (feel free to do it on <code>lb-01</code> and <code>web-02</code>, but it won’t be checked)</li>
<li>Configure <code>ufw</code> so that it blocks all incoming traffic, except the following TCP ports:

<ul>
<li><code>22</code> (SSH)</li>
<li><code>443</code> (HTTPS SSL)</li>
<li><code>80</code> (HTTP)</li>
</ul></li>
<li>Share the <code>ufw</code> commands that you used in your answer file</li>
</ul>
