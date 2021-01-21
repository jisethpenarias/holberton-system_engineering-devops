<h1 class="gap">0x14. MySQL</h1>


<h3>General</h3>

<ul>
<li>What is the main role of a database</li>
<li>What is a database replica</li>
<li>What is the purpose of a database replica</li>
<li>Why database backups need to be stored in different physical locations</li>
<li>What operation should you regularly perform to make sure that your database backup strategy actually works</li>
</ul>

<h2 class="gap">Tasks</h2>



<h4 class="task">
0. Install MySQL
</h4>

<!-- Task Body -->
  <p>First things first, let’s get MySQL installed on <strong>both</strong> your web-01 and web-02 servers.</p>

<ul>
<li>MySQL distribution must be 5.7.x</li>
<li>Make sure that <a href="/rltoken/CVSfIO2NRl-P3ukLvKE4Fw" title="task #3" target="_blank">task #3</a> of your <a href="/rltoken/haLXhL5svnmrgskFpFHmyA" title="SSH project" target="_blank">SSH project</a> is completed for <code>web-01</code> and <code>web-02</code>.  The checker will connect to your servers to check MySQL status</li>
<li>Please make sure you have your <code>README.md</code> pushed to Github.</li>
</ul>

<p>Example:</p>

<pre><code>ubuntu@229-web-01:~$ mysql --version
mysql  Ver 14.14 Distrib 5.7.25, for Linux (x86_64) using  EditLine wrapper
ubuntu@229-web-01:~$
</code></pre>

  <h4 class="task">
    1. Let us in!
  </h4>

   <p>In order for us to verify that your servers are properly configured, we need you to create a user and password for <strong>both</strong> MySQL databases which will allow the checker access to them.</p>

<ul>
<li>Create a MySQL user named <code>holberton_user</code>  on both <code>web-01</code> and <code>web-02</code> with the host name set to <code>localhost</code> and the password <code>projectcorrection280hbtn</code>. This will allow us to access the replication status on both servers.</li>
<li>Make sure that <code>holberton_user</code> has permission to check the primary/replica status of your databases.</li>
<li>In addition to that, make sure that <a href="/rltoken/CVSfIO2NRl-P3ukLvKE4Fw" title="task #3" target="_blank">task #3</a> of your <a href="/rltoken/haLXhL5svnmrgskFpFHmyA" title="SSH project" target="_blank">SSH project</a> is completed for <code>web-01</code> and <code>web-02</code>.  <strong>You will likely need to add the public key to web-02 as you only added it to web-01 for this project.</strong> The checker will connect to your servers to check MySQL status</li>
</ul>

<p>Example:</p>

<pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
Enter password:
+-----------------------------------------------------------------+
| Grants for holberton_user@localhost                             |
+-----------------------------------------------------------------+
| GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
+-----------------------------------------------------------------+
ubuntu@229-web-01:~$
</code></pre>


 <h4 class="task">
    2. If only you could see what I've seen with your eyes
  </h4>

<p>In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.</p>

<ul>
<li>Create a database named <code>tyrell_corp</code>.</li>
<li>Within the <code>tyrell_corp</code> database create a table named <code>nexus6</code> and add at least one entry to it.</li>
<li>Make sure that <code>holberton_user</code> has <code>SELECT</code> permissions on your table so that we can check that the table exists and is not empty.</li>
</ul>

<pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
Enter password:
+----+-------+
| id | name  |
+----+-------+
|  1 | Leon  |
+----+-------+
ubuntu@229-web-01:~$
</code></pre>


  <h4 class="task">
    3. Quite an experience to live in fear, isn't it?
  </h4>

 <!-- Task Body -->
  <p>Before you get started with your primary-replica synchronization, you need one more thing in place. On your <strong>primary</strong> MySQL server (web-01), create a new user for the replica server.</p>

<ul>
<li>The name of the new user should be <code>replica_user</code>, with the host name set to <code>%</code>, and can have whatever password you’d like.</li>
<li><code>replica_user</code> must have the appropriate permissions to replicate your primary MySQL server.</li>
<li><code>holberton_user</code> will need SELECT privileges on the <code>mysql.user</code> table in order to check that <code>replica_user</code> was created with the correct permissions.</li>
</ul>

<pre><code>ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
+------------------+-----------------+
| user             | Repl_slave_priv |
+------------------+-----------------+
| root             | Y               |
| mysql.session    | N               |
| mysql.sys        | N               |
| debian-sys-maint | Y               |
| holberton_user   | N               |
| replica_user     | Y               |
+------------------+-----------------+
ubuntu@229-web-01:~$
</code></pre>


  <h4 class="task">
    4. Setup a Primary-Replica infrastructure using MySQL
  </h4>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/09e83e914f0d6865ce320a47f2f14837a5b190b6.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210121%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210121T130854Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7e1ee190965ad19da1b5f66e9e272e72867772562e9c1ad430014f0e380882bb" alt="" style=""></p>

<p>Having a replica member on for your MySQL database has 2 advantages:</p>

<ul>
<li>Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data</li>
<li>Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed</li>
</ul>

<h3>Requirements:</h3>

<ul>
<li>MySQL primary must be hosted on <code>web-01</code> - do not use the <code>bind-address</code>,  just comment out this parameter</li>
<li>MySQL replica must be hosted on <code>web-02</code></li>
<li>Setup replication for the MySQL database named <code>tyrell_corp</code></li>
<li>Provide your MySQL primary configuration as answer file(<code>my.cnf</code> or <code>mysqld.cnf</code>) with the name <code>4-mysql_configuration_primary</code></li>
<li>Provide your MySQL replica configuration as an answer file with the name <code>4-mysql_configuration_replica</code></li>
</ul>

<h3>Tips:</h3>

<ul>
<li>Once MySQL replication is setup, add a new record in your table via MySQL on <code>web-01</code> and check if the record has been replicated in MySQL <code>web-02</code>. If you see it, it means your replication is working!</li>
<li><strong>Make sure that UFW is allowing connections on port 3306 (default MySQL port) otherwise replication will not work</strong>.</li>
</ul>

<p>Example:</p>

<h2><code>web-01</code></h2>

<pre><code>ubuntu@web-01:~$ mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1467
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt; show master status;
+------------------+----------+--------------------+------------------+
| File             | Position | Binlog_Do_DB       | Binlog_Ignore_DB |
+------------------+----------+--------------------+------------------+
| mysql-bin.000009 |      107 | tyrell_corp          |                  |
+------------------+----------+--------------------+------------------+
1 row in set (0.00 sec)

mysql&gt; 
</code></pre>

<h2><code>web-02</code></h2>

<pre><code>root@web-02:/home/ubuntu# mysql -uholberton_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 53
Server version: 5.5.49-0ubuntu0.14.04.1-log (Ubuntu)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql&gt; show slave status\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 158.69.68.78
                  Master_User: replica_user
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000009
          Read_Master_Log_Pos: 107
               Relay_Log_File: mysql-relay-bin.000022
                Relay_Log_Pos: 253
        Relay_Master_Log_File: mysql-bin.000009
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 107
              Relay_Log_Space: 452
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 1
1 row in set (0.00 sec)

mysql&gt; 

</code></pre>



  <h4 class="task">
    5. MySQL backup
  </h4>

<!-- Task Body -->
  <p><a href="https://www.youtube.com/watch?v=ANU-oSE5_hU" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/280/Bbpsgif.jpg" alt="" style=""></a></p>

<p>What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.</p>

<p>Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</p>

<p>Requirements:</p>

<ul>
<li>The MySQL dump must contain all your MySQL databases</li>
<li> The MySQL dump must be named <code>backup.sql</code></li>
<li>The MySQL dump file has to be compressed to a <code>tar.gz</code> archive</li>
<li>This archive must have the following name format: <code>day-month-year.tar.gz</code></li>
<li>The user to connect to the MySQL database must be <code>root</code></li>
<li>The Bash script accepts one argument that is the password used to connect to the MySQL database</li>
</ul>

<p>Example:</p>

<pre><code>ubuntu@03-web-01:~$ ls
5-mysql_backup
ubuntu@03-web-01:~$ ./5-mysql_backup mydummypassword
backup.sql
ubuntu@03-web-01:~$ ls
01-03-2017.tar.gz  5-mysql_backup  backup.sql
ubuntu@03-web-01:~$ more backup.sql
-- MySQL dump 10.13  Distrib 5.7.25, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database:
-- ------------------------------------------------------
-- Server version   5.7.25-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `tyrell_corp`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tyrell_corp` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tyrell_corp`;

--
-- Table structure for table `nexus6`
--

DROP TABLE IF EXISTS `nexus6`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nexus6` (
  `id` int(6) unsigned NOT NULL AUTO_INCREMENT,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `reg_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
ubuntu@03-web-01:~$
ubuntu@03-web-01:~$ file 01-03-2017.tar.gz
01-03-2017.tar.gz: gzip compressed data, from Unix, last modified: Wed Mar  1 23:38:09 2017
ubuntu@03-web-01:~$
</code></pre>
