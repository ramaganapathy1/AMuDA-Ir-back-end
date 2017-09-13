
<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "ir";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$password1=filter_var($_POST['password'], FILTER_SANITIZE_STRING);
$number=filter_var($_POST['number'], FILTER_SANITIZE_STRING);

$sql = "SELECT * FROM user where number ='$number' and password = '$password1'" ;
$result = $conn->query($sql);
$name="";
$id="";
$read="";
if ($result->num_rows > 0) {
    echo "check";
    session_start();
    while($row = $result->fetch_assoc()) {
        $name=$row['name'];
        $id=$row['number'];
     #   $read=$row['read'];
    }
    $_SESSION['name']=$name;
    $_SESSION['number']=$id;
    #$_SESSION['read']=$read;
    header('Location: http://localhost:8000/dashboard.php?id=success');
}
else
    {
            echo "Error 2";
            header('Location: http://localhost:8000/index.php?id=error');
    }



$conn->close();
?>