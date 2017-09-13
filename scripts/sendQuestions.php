<?php
    $id=array();
    $i=0;
    foreach($_POST as $key=>$value)
    {
        if($value=="true")
        {
            $id[$i]=(int)$key;
            $i++;
        }
    }
    $list['tcid']=(int)$_POST['tcid'];
    $list['list'] = $id;
    $list = json_encode($list);
    print_r($list);
$curl = curl_init("172.104.51.13:8080/form/sendform");
$data = array();
#$data['name'] = "";
$data = json_encode($data);
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($curl, CURLOPT_POSTFIELDS, $id);

// Make the REST call, returning the result
$response = curl_exec($curl);
if (!$response) {
    die("Connection Failure.n");
}
else {
    echo "<br>success</br>";
    $response = json_decode($response);
    print_r($response);
    header("Location:../send.php?id=success");
}
?>