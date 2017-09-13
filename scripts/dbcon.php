<?php
$servername = "172.104.51.13:3306";
$username = "smh2017";
$password = "smh2017bro";

// Create connection
$conn = new mysqli($servername, $username, $password,"SMH");
if($conn)
{
 #   echo "true";
}
else
{
    echo mysqli_error($conn);
}
?>