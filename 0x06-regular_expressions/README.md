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

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Para este proyecto, debes construir tu expresión regular usando Oniguruma, una biblioteca de expresiones regulares que es usada por Ruby por defecto. </font><font style="vertical-align: inherit;">Tenga en cuenta que otras bibliotecas de expresiones regulares a veces tienen propiedades diferentes.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Debido a que el enfoque de este ejercicio es jugar con expresiones regulares (regex), aquí está el código Ruby que debe usar, simplemente reemplace la parte regexp, es decir, el código entre </font></font><code>//</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">:</font></font></p>

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
<h3> Tasks</h3>
  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    0. Simplemente igualar a Holberton
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>


  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173713Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=87988cedb4e0e7169af3fe46e5db7124975efc4036992d50e394c99c1172f1e8" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">La expresión regular debe coincidir </font></font><code>Holberton</code></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo:</font></font></p>

<pre><code>sylvain@ubuntu$ ./0-simply_match_holberton.rb Holberton | cat -e<font></font>
Holberton$<font></font>
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School" | cat -e<font></font>
Holberton$<font></font>
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Holberton School Holberton" | cat -e<font></font>
HolbertonHolberton$<font></font>
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e<font></font>
$<font></font>
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>0-simply_match_holberton.rb</code></li>


    </div>

  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    1. Token de repetición n. ° 0
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173713Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=b73cde7449afd3dad911b65826dc0da283bb6b5da91ec24877f5508643409766" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Encuentre la expresión regular que coincidirá con los casos anteriores</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>1-repetition_token_0.rb</code></li>
</ul>


</div>


    </div>

  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    2. Token de repetición n. ° 1
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173713Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=814d8d477fa7ba23365242346b35fb1269b38ebb62841a1669964a735e36d105" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Encuentre la expresión regular que coincidirá con los casos anteriores</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>2-repetition_token_1.rb</code></li>
</ul>


  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    3. Token de repetición n. ° 2
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173713Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7c82ed1426354f7f00b6a4a60f825fd7032855887456fe609aecfdd7ee859c8a" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Encuentre la expresión regular que coincidirá con los casos anteriores</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>3-repetition_token_2.rb</code></li>
</ul>

  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    4. Token de repetición n. ° 3
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  



  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201109%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20201109T173713Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=211614aab1fa6a6f5b3ee9c776ad71184d29f67d832bbfcb82dd645e28706365" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Encuentre la expresión regular que coincidirá con los casos anteriores</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Su expresión regular no debe contener corchetes</font></font></li>
</ul>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>4-repetition_token_3.rb</code></li>
</ul>

  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    5. No del todo HBTN pero
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisitos:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">La expresión regular debe coincidir exactamente con una cadena que comienza con </font></font><code>h</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">termina con </font></font><code>n</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">y puede tener cualquier carácter en el medio</font></font></li>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Con las instrucciones del proyecto, cree un script Ruby que acepte un argumento y páselo a un método de coincidencia de expresión regular</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo:</font></font></p>

<pre><code>sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e<font></font>
$<font></font>
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e<font></font>
hbn$<font></font>
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e<font></font>
$<font></font>
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e<font></font>
h8n$<font></font>
sylvain@ubuntu$<font></font>
$<font></font>
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>5-beginning_and_end.rb</code></li>
</ul>


  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    6. Llámame quizás
       </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Esta tarea se la presenta la asesora profesional de Holberton, </font></font><a href="/rltoken/V4rEpseJEPRMMnfaZPbkgw" title="Neha Jain" target="_blank"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Neha Jain</font></font></a><font style="vertical-align: inherit;"><font style="vertical-align: inherit;"> , ingeniera de software senior en LinkedIn.</font></font></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisito:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">La expresión regular debe coincidir con un número de teléfono de 10 dígitos.</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo:</font></font></p>

<pre><code>sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e<font></font>
4155049898$<font></font>
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e<font></font>
$<font></font>
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e<font></font>
$<font></font>
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e<font></font>
$<font></font>
sylvain@ubuntu$<font></font>
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>6-phone_number.rb</code></li>
</ul>

  <h4 class="task"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
    7. Dios mío, ¿por qué estás gritando?
      </font></font><span class="alert alert-warning mandatory-optional"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">
        obligatorio
      </font></font></span>
  </h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p><img src="/images/contents/sysadmin/projects/78/shouting.jpg" alt="" style=""></p>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Requisito:</font></font></p>

<ul>
<li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">La expresión regular solo debe coincidir: letras mayúsculas</font></font></li>
</ul>

<p><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Ejemplo:</font></font></p>

<pre><code>sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e<font></font>
ILOVESYSADMIN$<font></font>
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e<font></font>
WHATSAY$<font></font>
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e<font></font>
$<font></font>
sylvain@ubuntu$<font></font>
</code></pre>


  <!-- Task URLs -->

  <!-- Github information -->
<p class="sm-gap"><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repo:</font></font></strong></p>
<ul>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Repositorio de GitHub: </font></font><code>holberton-system_engineering-devops</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Directorio: </font></font><code>0x06-regular_expressions</code></li>
    <li><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Archivo: </font></font><code>7-OMG_WHY_ARE_YOU_SHOUTING.rb</code></li>
</ul>
