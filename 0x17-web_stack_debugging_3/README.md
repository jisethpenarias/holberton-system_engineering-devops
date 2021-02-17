<h1 class="gap">0x17. Web stack debugging #3</h1>


 <h2>Background Context</h2>

<p><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png" alt="" style=""></p>

<p>When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)</p>

<p>Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites… It <a href="/rltoken/Ah9_LmUi191dqxT-Zx7uhg" title="actually powers 26% of the web" target="_blank">actually powers 26% of the web</a>, so there is a fair chance that you will end up working with it at some point in your career.</p>

<p>Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools. </p>

<p>The web stack you are debugging today is a Wordpress website running on a LAMP stack.</p>


<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Strace is your friend
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><a href="https://youtu.be/uHEzt1QuASo" target="_blank"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/f5af5167e65bd3101f76.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210217%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210217T151045Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7d2d438fe72e9763d52b6d0834d072f9bac2b1e42ba03237bf44dbfe07a380fb" alt="" style=""></a></p>

<p>Using <code>strace</code>, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).</p>

<p>Hint:</p>

<ul>
<li><code>strace</code> can attach to a current running process</li>
<li>You can use <a href="/rltoken/4KkxME6-3aY9fgfok6HNFA" title="tmux" target="_blank">tmux</a> to run <a href="/rltoken/OUc10nTtuZG65adFVbkYag" title="strace" target="_blank">strace</a> in one window and <code>curl</code> in another one</li>
</ul>

<p>Requirements:</p>

<ul>
<li>Your <code>0-strace_is_your_friend.pp</code> file must contain Puppet code</li>
<li>You can use whatever Puppet resource type you want for you fix</li>
</ul>

<p>Example:</p>

<pre><code>root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: &lt;http://127.0.0.1/?rest_route=/&gt;; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
&lt;title&gt;Holberton &amp;#8211; Just another WordPress site&lt;/title&gt;
&lt;link rel="alternate" type="application/rss+xml" title="Holberton &amp;raquo; Feed" href="http://127.0.0.1/?feed=rss2" /&gt;
&lt;link rel="alternate" type="application/rss+xml" title="Holberton &amp;raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" /&gt;
        &lt;div id="wp-custom-header" class="wp-custom-header"&gt;&lt;img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /&gt;&lt;/div&gt;  &lt;/div&gt;
                            &lt;h1 class="site-title"&gt;&lt;a href="http://127.0.0.1/" rel="home"&gt;Holberton&lt;/a&gt;&lt;/h1&gt;
        &lt;p&gt;Yet another bug by a Holberton student&lt;/p&gt;
root@e514b399d69d:~#
</code></pre>
