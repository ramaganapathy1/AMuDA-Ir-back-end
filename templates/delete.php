
<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "ir";
session_start();
$num=$_SESSION['number'];
$read=$_SESSION['read'];
// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$id=filter_var($_GET['id'], FILTER_SANITIZE_STRING);

$sql = "DELETE FROM paper WHERE paperName='".$id."'";
//$sql1 = "UPDATE user SET read= $read+1 WHERE number=''".$num."'";

if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    header('Location: http://localhost:8000/dashboard.php?id=dsuccess');
} else {
    header('Location: http://localhost:8000/dashboard.php?id=error');
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
