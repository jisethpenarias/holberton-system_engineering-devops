<h1 class="gap">0x07. Networking basics #0</h1>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/aVNeUbmv5XGxE2BXVPHOTg" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>OSI Model</h3>

<ul>
<li>What it is</li>
<li>How many layers it has</li>
<li>How it is organized</li>
</ul>

<h3>What is a LAN</h3>

<ul>
<li>Typical usage</li>
<li>Typical geographical size</li>
</ul>

<h3>What is a WAN</h3>

<ul>
<li>Typical usage</li>
<li>Typical geographical size</li>
</ul>

<h3>What is the Internet</h3>

<ul>
<li>What is an IP address</li>
<li>What are the 2 types of IP address</li>
<li>What is <code>localhost</code></li>
<li>What is a subnet</li>
<li>Why IPv6 was created</li>
</ul>

<h3>TCP/UDP</h3>

<ul>
<li>What are the 2 mainly used data transfer protocols for IP (transfer level on the OSI schema)</li>
<li>What is the main difference between TCP and UDP</li>
<li>What is a port</li>
<li>Memorize SSH, HTTP and HTTPS port numbers</li>
<li>What tool/protocol is often used to check if a device is connected to a network</li>
</ul>


<h2>More Info</h2>

<p>The second line of all your Bash scripts should be a comment explaining what is the script doing</p>

<p>For multiple choice question type tasks, just type the number of the correct answer in your answer file, add a new line for every new answer, example:</p>

<p>What is the most important position in a software company?</p>

<ol>
<li>Project manager</li>
<li>Backend developer</li>
<li>System administrator</li>
</ol>

<pre><code>sylvain@ubuntu$ cat foo_answer_file
3
sylvain@ubuntu$
</code></pre>

<p>Source for question 1 <a href="/rltoken/vQJ6bK8D0vme22Xst44Mqg" title="here" target="_blank">here</a></p>

<h2 class="gap">Tasks</h2>


 <h4 class="task">
    0. OSI model
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>OSI (Open Systems Interconnection) is an abstract model to describe layered communication and computer network design. The idea is to segregate the different parts of what make communication possible.</p>

<p>It is organized from the lowest level to the highest level:</p>

<ul>
<li>The lowest level: layer 1 which is for transmission on physical layers with electrical impulse, light or radio signal</li>
<li>The highest level: layer 7 which is for application specific communication like SNMP for emails, HTTP for your web browser, etc</li>
</ul>

<p>Keep in mind that the OSI model is a concept, it’s not even tangible. The OSI model doesn’t perform any functions in the networking process.
It is a conceptual framework so we can better understand complex interactions that are happening.
Most of the functionality in the OSI model exists in all communications systems.</p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/4e6a0ad87a65d7054248.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173805Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=a084d15d9581971694be6840e6d708bbbb06124bbdb727696583cf7e27751358" alt="" style=""></p>

<p>In this project we will mainly focus on:</p>

<ul>
<li>The Transport layer and especially TCP/UDP</li>
<li>On the Network layer with IP and ICMP</li>
</ul>

<p>The image bellow describes more concretely how you can relate to every level.</p>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/0fc96bd99faa7941b18bcae4c5f90c6acd11791d.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173805Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=dccc5f6348e32b74fcf5d27ffec9844ecb431189714f8e64841dd28fb5ee0587" alt="" style=""></p>

<p>Questions:</p>

<p>What is the OSI model?</p>

<ol>
<li>Set of specifications that network hardware manufacturers must respect</li>
<li>The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology</li>
<li>The OSI model is a model that characterizes the communication functions of a telecommunication system with a strong regard for their underlying internal structure and technology</li>
</ol>

<p>How is the OSI model organized?</p>

<ol>
<li> Alphabetically</li>
<li>From the lowest to the highest level</li>
<li>Randomly</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>0-OSI_model</code></li>
</ul>
<br>
</br>
 <h4 class="task">
    1. Types of network
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/4b995d4f8078b44afa968d68a98035d2bd7e8fac.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173805Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=71dea850348e1d9d98d91fea4078094112be63d8ae32ce261e13ddffae6ab7e0" alt="" style=""></p>

<p>LAN connect local devices together, WAN connects LANs together, and WANs are operating over the Internet.</p>

<p>Questions:</p>

<p>What type of network are Holberton iMacs connected to?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>

<p>What type of network could connect an office in one building to another office in a building a few streets away?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>

<p>What network do you use when you browse www.holbertonschool.com from your smartphone (not connected to the Wifi)?</p>

<ol>
<li>Internet</li>
<li>WAN</li>
<li>LAN</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>1-types_of_network</code></li>
</ul>

<br>
</br>
<h4 class="task">
    2. MAC and IP address
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/1e348ba3bcbb094b02922f821ffeb3d8c5438b7b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173805Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=19c50a0a1efa207e0d4f9b7830705467f4deed3a2862783ce8e0a6bab48d5e3a" alt="" style=""></p>

<p>Questions:</p>

<p>What is a MAC address?</p>

<ol>
<li>The name of a network interface</li>
<li>The unique identifier of a network interface</li>
<li>A network interface</li>
</ol>

<p>What is an IP address?</p>

<ol>
<li>Is to devices connected to a network what postal address is to houses</li>
<li>The unique identifier of a network interface</li>
<li>Is a number that network devices use to connect to networks</li>
</ol>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>2-MAC_and_IP_address</code></li>
</ul>
<br>
</br>
<h4 class="task">
    3. UDP and TCP
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3d92e3c4a470f8ecf4c73db511fcbbadaa002e1c.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173805Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=b8075eb19978f1d8aec041b4118129aadf39f12b82d9ff72337540bc03dc548a" alt="" style=""></p>

<p>Let’s fill the empty parts in the drawing above.</p>

<p>Questions:</p>

<ul>
<li>Which statement is correct for the TCP box:

<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the UDP box:

<ol>
<li><code>It is a protocol that is transferring data in a slow way but surely</code></li>
<li><code>It is a protocol that is transferring data in a fast way and might loss data along in the process</code></li>
</ol></li>
<li>Which statement is correct for the TCP worker:

<ol>
<li><code>Have you received boxes x, y, z?</code></li>
<li><code>May I increase the rate at which I am sending you boxes?</code></li>
</ol></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>3-UDP_and_TCP</code></li>
</ul>


<br>
</br>
 <h4 class="task">
    4. TCP and UDP ports
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Once packets have been sent to the right network device using IP using either UDP or TCP as a mode of transportation, it needs to actually enter the network device.</p>

<p>If we continue the comparison of a network device to your house, where IP address is like your postal address, UDP and TCP ports are like the windows and doors of your place. A TCP/UDP network device has 65535 ports. Some of them are officially reserved for a specific usage, some of them are known to be used for a specific usage (but nothing is officially declared) and the rest are free of use.</p>

<p>While the full list of ports should not be memorized, it is important to know the most used ports, let’s start by remembering 3 of them:</p>

<ul>
<li><strong>22</strong> for SSH</li>
<li><strong>80</strong> for HTTP</li>
<li><strong>443</strong> for HTTPS</li>
</ul>

<p>Note that a specific <a href="/rltoken/T47UYz3XOQCXsOPxlMDrXw" title="IP + port = socket" target="_blank">IP + port = socket</a>.</p>

<p>Write a Bash script that displays listening ports:</p>

<ul>
<li>That only shows listening sockets</li>
<li>That shows the PID and name of the program to which each socket belongs</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ sudo ./4-TCP_and_UDP_ports
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 *:sunrpc                *:*                     LISTEN      518/rpcbind
tcp        0      0 *:ssh                   *:*                     LISTEN      1240/sshd
tcp        0      0 *:32938                 *:*                     LISTEN      547/rpc.statd
tcp6       0      0 [::]:sunrpc             [::]:*                  LISTEN      518/rpcbind
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN      1240/sshd
tcp6       0      0 [::]:33737              [::]:*                  LISTEN      547/rpc.statd
udp        0      0 *:sunrpc                *:*                                 518/rpcbind
udp        0      0 *:691                   *:*                                 518/rpcbind
udp        0      0 localhost:723           *:*                                 547/rpc.statd
udp        0      0 *:60129                 *:*                                 547/rpc.statd
udp        0      0 *:3845                  *:*                                 562/dhclient
udp        0      0 *:bootpc                *:*                                 562/dhclient
udp6       0      0 [::]:47444              [::]:*                              547/rpc.statd
udp6       0      0 [::]:sunrpc             [::]:*                              518/rpcbind
udp6       0      0 [::]:50038              [::]:*                              562/dhclient
udp6       0      0 [::]:691                [::]:*                              518/rpcbind
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name    Path
unix  2      [ ACC ]     STREAM     LISTENING     7724     518/rpcbind         /run/rpcbind.sock
unix  2      [ ACC ]     STREAM     LISTENING     6525     1/init              @/com/ubuntu/upstart
unix  2      [ ACC ]     STREAM     LISTENING     8559     835/dbus-daemon     /var/run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     9190     1087/acpid          /var/run/acpid.socket
unix  2      [ ACC ]     SEQPACKET  LISTENING     7156     378/systemd-udevd   /run/udev/control
sylvain@ubuntu$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>4-TCP_and_UDP_ports</code></li>
</ul>

<br>
</br>
 <h4 class="task">
    5. Is the host on the network
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://media.giphy.com/media/uDxkJAVSU7GY8/giphy.gif" alt="" style=""></p>

<p>The Internet Control Message Protocol (ICMP) is a protocol in the Internet protocol suite. It is used by network devices, to check if other network devices are available on the network. The command <code>ping</code> uses ICMP to make sure that a network device remains online or to troubleshoot issues on the network. </p>

<p>Write a Bash script that pings an IP address passed as an argument.</p>

<p>Requirements: </p>

<ul>
<li>Accepts a string as an argument</li>
<li>Displays <code>Usage: 5-is_the_host_on_the_network {IP_ADDRESS}</code> if no argument passed</li>
<li>Ping the IP 5 times</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./5-is_the_host_on_the_network 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=12.9 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=13.6 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=7.83 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=11.3 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=63 time=7.57 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 7.570/10.682/13.679/2.546 ms
sylvain@ubuntu$
sylvain@ubuntu$ ./5-is_the_host_on_the_network
Usage: 5-is_the_host_on_the_network {IP_ADDRESS}
sylvain@ubuntu$ 
</code></pre>

<p>It is interesting to look at the <code>time</code> value, which is the time that it took for the ICMP request to go to the <code>8.8.8.8</code> IP and come back to my host. The IP <code>8.8.8.8</code> is owned by Google, and the quickest roundtrip between my computer and Google was 7.57 ms which is pretty fast, which is a sign that the network path between my computer and Google’s datacenter is in good shape. A slow ping would indicate a slow network.</p>

<p>Next time you feel that your connection is slow, try the <code>ping</code> command to see what is going on!</p>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong>Repo:</strong></p>
<ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
    <li>Directory: <code>0x07-networking_basics</code></li>
    <li>File: <code>5-is_the_host_on_the_network</code></li>
</ul>
