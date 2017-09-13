<?php
session_start();
if(!isset($_SESSION['name']))
{
    header('Location: http://localhost:8000/index.php?id=error');
}
else
{
    $name=$_SESSION['name'];
    $num=$_SESSION['number'];
    ?><html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title><?php echo "$name"; ?>'s IR - Amrita</title>
    <!-- Tell the browser to be responsive to screen width -->
    <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
    <link rel="stylesheet" href="dist/sweetalert-master/dist/sweetalert.css">
    <!-- Bootstrap 3.3.6 -->
    <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="plugins/datatables/dataTables.bootstrap.css">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.5.0/css/font-awesome.min.css">
    <!-- Ionicons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/ionicons/2.0.1/css/ionicons.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="dist/css/AdminLTE.min.css">
    <link rel="stylesheet" href="dist/css/skins/_all-skins.min.css">
    <!-- iCheck -->
    <link rel="stylesheet" href="plugins/iCheck/flat/blue.css">
    <!-- Morris chart -->
    <link rel="stylesheet" href="plugins/morris/morris.css">
    <!-- jvectormap -->
    <link rel="stylesheet" href="plugins/jvectormap/jquery-jvectormap-1.2.2.css">
    <!-- Date Picker -->
    <link rel="stylesheet" href="plugins/datepicker/datepicker3.css">
    <link rel="stylesheet" href="dist/css/custom/custom.css">
    <!-- Daterange picker -->
    <link rel="stylesheet" href="plugins/daterangepicker/daterangepicker.css">
    <!-- bootstrap wysihtml5 - text editor -->
    <link rel="stylesheet" href="plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.min.css">
    <link href="https://fonts.googleapis.com/css?family=Baloo+Bhaina|Catamaran:100|Exo:100|Lato|Quicksand:300" rel="stylesheet">
    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
</head>
<body  id="main" class="img-responsive success">
<nav class="navbar navbar-fixed-top navbar-default " style="background:#004c96;">
    <div class="container-fluid">
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" style="color: #f4ffea;" href="index.php"><b><?php echo strtoupper($name);?>'s &nbsp; I</b>R - <b>A</b>MuDA </a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav navbar-nav">
                <li class="active"><a href="dashboard.php">Home</a></li>
                <li><a href="about.php">About</a></li>
                <li><a href="#">Contact</a></li>

            </ul>

        </div>
        <!--/.nav-collapse -->
    </div><!--/.container-fluid -->
</nav>
<br><br>
<div class="row">
    <div class="col-lg-3 ">
        <div class="callout callout">
            <H1><?php echo $_GET['id'] ?></H1>
        </div>
        <div class="col-lg-10 ">
            <div class="callout callout-danger">
                <h3><?php echo "Hi! , ".strtoupper( $_SESSION['name']);?></a></h3>

                <p><i class="fa fa-sign-out" aria-hidden="true"> <a href="logout.php">Logout?</i></a> </p>
            </div>


        </div>
    </div>
    <div class="col-lg-9">
        <div class="row">
            <a class="btn btn-app" data-toggle="modal" data-target="#myModal">

                <i class="fa fa-plus" ></i> Add
            </a>
        </div>
        <div class="row">

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
            $id=$_GET['id'];
            echo "<h1>$id - Paper Recommendations</h1>";
            $sql = "SELECT * FROM recommendCon where paperName='$id'" ;

            $result = $conn->query($sql);
            $name="";

            $conn=array();
            $f="callout-success";
            $f1="callout-warning";
            echo "<br><h2>Read Next!</h2>";
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "<div class=\"col-md-3 \">
                            <div id='".$row['paper1']."' class=\"callout callout-success \">
                                <h2>".$row['paper1']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-3 \">
                            <div id='".$row['paper2']."' class=\"callout $f \">
                                <h2>".$row['paper2']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-3 \">
                            <div id='".$row['paper3']."' class=\"callout $f \">
                                <h2>".$row['paper3']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-3 \">
                            <div id='".$row['paper4']."' class=\"callout $f \">
                                <h2>".$row['paper4']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    array_push($conn,$row['paperName'],$row['paper1'],$row['paper2'],$row['paper3'],$row['paper4'],$row['paper5']);
                }
            }
            else
            {
                echo "Error 2";
                #header('Location: http://localhost:8000/index.php?id=error');
            }

            echo"<h3>Total Paper(s) ".(int)$result->num_rows."</h3>";

            $sql = "SELECT * FROM recommendEla where paperName='$id'" ;

            $result = $conn->query($sql);
            $name="";

            echo "<br><h2>Doubt Full ? - Read these</h2>";
            if ($result->num_rows > 0) {
                while($row = $result->fetch_assoc()) {
                    echo "<div class=\"col-md-6 \">
                            <div id='".$row['paper1']."' class=\"callout $f1 \">
                                <h2>".$row['paper1']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-6 \">
                            <div id='".$row['paper2']."' class=\"callout $f1 \">
                                <h2>".$row['paper2']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-6 \">
                            <div id='".$row['paper3']."' class=\"callout $f1 \">
                                <h2>".$row['paper3']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";
                    echo "<div class=\"col-md-6 \">
                            <div id='".$row['paper4']."' class=\"callout $f1 \">
                                <h2>".$row['paper4']." <a  href=''><i style='color:black;' class=\"fa fa-paperclip \" ></i></a></h2>
                                    <p>".$row['date1']."</p></div> </p>
                     </div>";

                    $f="";
                    $f2="";
                }
            }
            else
            {
                echo "Error 2";
                #header('Location: http://localhost:8000/index.php?id=error');
            }

            echo"<h3>Total Paper(s) ".(int)$result->num_rows."</h3>";

            $conn->close();
            ?>
        </div>

    </div>

</div>
        <div class="row">
            <div id="wordtree_basic" style="width: 900px; height: 500px"></div>
        </div>

</body>
<script src="plugins/jQuery/jquery-2.2.3.min.js"></script>
<!-- Bootstrap 3.3.6 -->
<script src="bootstrap/js/bootstrap.min.js"></script>
<!-- DataTables -->
<script src="plugins/datatables/jquery.dataTables.min.js"></script>
<script src="plugins/datatables/dataTables.bootstrap.min.js"></script>
<!-- SlimScroll -->
<script src="plugins/slimScroll/jquery.slimscroll.min.js"></script>
<!-- FastClick -->
<script src="plugins/fastclick/fastclick.js"></script>
<!-- AdminLTE App -->
<script src="dist/js/app.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="dist/js/demo.js"></script>
<!-- page script -->
<script>
    $(function () {
        $("#tableList").DataTable({
            "paging": true,
            "lengthChange": false,
            "searching": false,
            "ordering": true,
            "info": true,
            "autoWidth": false
        });
    });
</script>
<script src="plugins/datatables/dataTables.bootstrap.min.js"></script>
<script src="plugins/datatables/jquery.dataTables.min.js"></script>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>


<script src="plugins/jQuery/jquery-2.2.3.min.js"></script>
<script src="https://code.jquery.com/ui/1.11.4/jquery-ui.min.js"></script>
<script>
    $.widget.bridge('uibutton', $.ui.button);
</script>
<script type='text/javascript' src='https://www.gstatic.com/charts/loader.js'></script>
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAuiWaDmr6ky8kGCIousEjixrcMQv-TH0U&callback=initMap"
        type="text/javascript"></script>

</script>
<script src="dist/sweetalert-master/dist/sweetalert-dev.js"></script>
<?php
if(isset($_SESSION['name']) and $_GET['id']=="success")
{
    echo "<script>swal(\"Hi! ".$_SESSION['name']."\", \"Login Success!\", \"success\")</script>";
}
?>
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript">
    google.charts.load('current', {packages:['wordtree']});
    google.charts.setOnLoadCallback(drawChart);

    function drawChart() {
        var data = google.visualization.arrayToDataTable(
            [ ['Phrases'],
                ['<?php echo "$conn[0] con $conn[1]"; ?>'],
                ['<?php echo "$conn[0] con $conn[2]"; ?>'],
                ['<?php echo "$conn[0] con $conn[3]"; ?>'],
                ['<?php echo "$conn[0] con $conn[4]"; ?>'],
                ['<?php echo "$conn[0] con $conn[5]"; ?>']
            ]
        );

        var options = {
            wordtree: {
                format: 'implicit',
                word: '<?php echo $conn[0]; ?>'
            }
        };

        var chart = new google.visualization.WordTree(document.getElementById('wordtree_basic'));
        chart.draw(data, options);
    }
</script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="plugins/morris/morris.min.js"></script>
<script src="plugins/sparkline/jquery.sparkline.min.js"></script>
<script src="plugins/jvectormap/jquery-jvectormap-1.2.2.min.js"></script>
<script src="plugins/jvectormap/jquery-jvectormap-world-mill-en.js"></script>
<script src="plugins/knob/jquery.knob.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.11.2/moment.min.js"></script>
<script src="plugins/daterangepicker/daterangepicker.js"></script>
<script src="plugins/datepicker/bootstrap-datepicker.js"></script>
<script src="plugins/bootstrap-wysihtml5/bootstrap3-wysihtml5.all.min.js"></script>
<script src="plugins/slimScroll/jquery.slimscroll.min.js"></script>
<script src="plugins/fastclick/fastclick.js"></script>
<script src="dist/js/app.min.js"></script>
<script src="dist/js/pages/dashboard.js"></script>

<script src="dist/js/demo.js"></script>
    </html>

<?php }?>