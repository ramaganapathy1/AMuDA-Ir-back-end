<?php
$data = array();
foreach ($_POST as $key=>$value)
{
    echo $key,$value;
    $data[$key]=(string)$value;
}
unset($data['subject']);
unset($data['send']);
$curl = curl_init("172.104.51.13:8080/notif/send");
print_r($data);
#$data['name'] = "";
$data = json_encode($data);
echo $data;
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

// Make the REST call, returning the result
$response = curl_exec($curl);
if (!$response) {
    header("Location:../index.php?id=success");
}
else {
    echo "<br>success</br>";
    $response = json_decode($response);
    print_r($response);
    header("Location:../index.php?id=success");
}
?>