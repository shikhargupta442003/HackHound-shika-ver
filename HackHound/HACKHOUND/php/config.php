<?php

$databaseHost = '65.0.131.249';//or localhost
$databaseName = 'new_hope'; // your db_name
$databaseUsername = 'root'; // root by default for localhost 
$databasePassword = '273209';  // by defualt empty for localhost

$mysqli = mysqli_connect($databaseHost, $databaseUsername, $databasePassword, $databaseName);
 
?>