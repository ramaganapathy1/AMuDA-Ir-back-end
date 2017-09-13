<?PHP
if(!empty($_FILES['uploaded_file']))
{
    $servername = "localhost";
    $username = "root";
    $password = "root";
    $dbname = "ir";
    session_start();
    if(!isset($_SESSION['number']))
        die;

// Create connection
    $conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }



    $path = "docFolder/";
    $path = $path . basename( $_FILES['uploaded_file']['name']);
    $ext = pathinfo($_FILES['uploaded_file']['name'], PATHINFO_EXTENSION);
    if($ext=="pdf") {
        if (move_uploaded_file($_FILES['uploaded_file']['tmp_name'], $path)) {
            echo "The file " . basename($_FILES['uploaded_file']['name']) . " has been uploaded";
            $name1=filter_var($_POST['papername'], FILTER_SANITIZE_STRING);
            $domain=filter_var($_POST['domain'], FILTER_SANITIZE_STRING);
            $date1=date("Y/m/d");
            $sql = "INSERT INTO paper(paperName,fileName,date1,userId,domain) VALUES ('".$name1."','".$_FILES['uploaded_file']['name']."','"
                .$date1."','".$_SESSION['number']."','".$domain."')";
            $sql1="INSERT INTO recommendCon (paperName,fileName) values ('".$name1."','".$_FILES['uploaded_file']['name']."')";
            echo $sql;

            if ($conn->query($sql) === TRUE ) {
                if($conn->query($sql1) === TRUE ) {
                    echo "New record created successfully";
                    header('Location: http://localhost:8000/dashboard.php?id=usuccess');
                }
                else
                {
                    echo "<br><br> $sql1";
                    echo "error in";
                    echo "Error: " . $sql . "<br>" . $conn->error;
                }
            } else {
                echo "Error: " . $sql . "<br>" . $conn->error;
              # header('Location: http://localhost:8000/dashboard.php?id=uerror');

            }
        } else {
            echo "There was an error uploading the file, please try again!";
        }
    }
    else {
        echo "Type Error!";
    }
}
$conn->close();
?>