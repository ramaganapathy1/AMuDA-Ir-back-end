
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
$name1=filter_var($_POST['name'], FILTER_SANITIZE_STRING);
$password1=filter_var($_POST['password'], FILTER_SANITIZE_STRING);
$email=filter_var($_POST['email'], FILTER_SANITIZE_STRING);
$number=filter_var($_POST['number'], FILTER_SANITIZE_STRING);

$sql = "INSERT INTO user VALUES ('".$name1."','".$email."','".$number."','".$password1."')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
    header('Location: http://localhost:8000/index.php?id=success');
} else {
    header('Location: http://localhost:8000/index.php?id=error');
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
