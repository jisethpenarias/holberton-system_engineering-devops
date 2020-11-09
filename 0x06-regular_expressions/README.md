<h1 class="gap"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">0x06. </font><font style="vertical-align: inherit;">Expresión regular</font></font></h1>

 <div class="gap formatted-content">
      <p style="margin-bottom: 0"><em><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para este proyecto, se espera que los estudiantes observen este concepto:</font></font></em></p>
      <ul style="margin-top: 5px">
          <li>
            <em><a href="/concepts/29"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Expresión regular</font></font></a></em>
          </li>
      </ul>
    </div>

  <article id="description" class="gap formatted-content">
    <h2><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Contexto de fondo</font></font></h2>

<h2>Background Context</h2>

<p>For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.</p>

<p>Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the <code>//</code>:</p>

<pre><code>sylvain@ubuntu$ cat example.rb<font></font>
#!/usr/bin/env ruby<font></font>
puts ARGV[0].scan(/127.0.0.[0-9]/).join<font></font>
sylvain@ubuntu$<font></font>
sylvain@ubuntu$ ./example.rb 127.0.0.2<font></font>
127.0.0.2<font></font>
sylvain@ubuntu$ ./example.rb 127.0.0.1<font></font>
127.0.0.1<font></font>
sylvain@ubuntu$ ./example.rb 127.0.0.a<font></font>
</code></pre>


</div>
<h2> Tasks</h2>
<h3 class="task">
    0. Simply matching Holberton
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T212724Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=cbea0f70fbb08acf7b09970fb1a13877ebb87834c3661fd12ec5d321d565881e" alt="" style=""></p>

<p>Requirements:</p>

<ul>
<li>The regular expression must match <code>Holberton</code></li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e
Holberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e
HolbertonHolberton$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>0-simply_match_holberton.rb</code></li>
  </ul>
<br>

</br>


<h3 class="task">
    1. Repetition Token #0
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T212724Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=1b58b3ab3c4bf6a895798527e8fb632e96d6272f9aa405de1174c6f9da286364" alt="" style=""></p>

<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>


  <!-- Task URLs -->

<!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>1-repetition_token_0.rb</code></li>
  </ul>
<br>

</br>

<h3 class="task">
    2. Repetition Token #1
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T212724Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=6ac0569111a5af051541a680a402308c0f1bc762167d0d967c8048ed908b708a" alt="" style=""></p>

<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>2-repetition_token_1.rb</code></li>
  </ul>

<br>

</br>

<h3 class="task">
    3. Repetition Token #2
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T212724Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=fefb9af26f168ce738f6b7798ac6d6dcac787cdc67d589d3eb074d9ab7268ba8" alt="" style=""></p>

<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>3-repetition_token_2.rb</code></li>
  </ul>

<br>

</br>
<h3 class="task">
    4. Repetition Token #3
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T212724Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=90d3042e6c29fc3702fd7191e24e11e1f200dcf53dd58e5c1f97ed6c33d9fe39" alt="" style=""></p>

<p>Requirements:</p>

<ul>
<li>Find the regular expression that will match the above cases</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
<li>Your regex should not contain square brackets</li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>4-repetition_token_3.rb</code></li>
  </ul>

<br>

</br>

<h3 class="task">
    5. Not quite HBTN yet
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Requirements:</p>

<ul>
<li>The regular expression must be exactly matching a string that starts with <code>h</code> ends with <code>n</code> and can have any single character in between</li>
<li>Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>5-beginning_and_end.rb</code></li>
  </ul>


<br>

</br>
  <h3 class="task">
    6. Call me maybe
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>This task is brought to you by Holberton professional advisor <a href="/rltoken/V4rEpseJEPRMMnfaZPbkgw" title="Neha Jain" target="_blank">Neha Jain</a>, Senior Software Engineer at LinkedIn.</p>

<p>Requirement:</p>

<ul>
<li>The regular expression must match a 10 digit phone number</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>6-phone_number.rb</code></li>
  </ul>


<br>

</br>
  <h3 class="task">
    7. OMG WHY ARE YOU SHOUTING?
      <span class="alert alert-warning mandatory-optional">
        mandatory
      </span>
  </h3>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="/images/contents/sysadmin/projects/78/shouting.jpg" alt="" style=""></p>

<p>Requirement:</p>

<ul>
<li>The regular expression must be only matching: capital letters</li>
</ul>

<p>Example:</p>

<pre><code>sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
  <p class="sm-gap"><strong>Repo:</strong></p>
  <ul>
    <li>GitHub repository: <code>holberton-system_engineering-devops</code></li>
      <li>Directory: <code>0x06-regular_expressions</code></li>
      <li>File: <code>7-OMG_WHY_ARE_YOU_SHOUTING.rb</code></li>
  </ul>


<br>

</br>


