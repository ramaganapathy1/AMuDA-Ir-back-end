<?php
#$curl = curl_init("172.104.51.13:8080/form/update/");
$data = array();
$qa =array();
foreach ($_POST as $key=>$value){
    echo $key,"=>",$value;
    $data[$key]=(string)$value;
    $qa[$key]=(string)$value;
}
unset($data['addques']);
require ('../scripts/dbcon.php');
$sql = "INSERT INTO question(question,tcid,type,category) VALUES ('".$data['question']."',".$data['tcid'].",'". $data['answer']."','".$data['category']."')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
   header("Location:../send.php?id=success");
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
   header("Location:../send.php?id=error");
}

$conn->close();


#unset($data['question']);
#unset($data['answer']);
#unset($qa['tcid']);
#unset($qa['addques']);
#$data['tcid']=(int)$data['tcid'];
#$data['qa']=$qa;
#echo $data;

#$data['name'] = "";
#$$data = json_encode($data);
#echo $data;
/*
curl_setopt($curl, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($curl, CURLOPT_HEADER, false);
curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
curl_setopt($curl, CURLOPT_HTTPHEADER, array('Content-Type: application/json'));
curl_setopt($curl, CURLOPT_POSTFIELDS, $data);

// Make the REST call, returning the result
$response = curl_exec($curl);
if($response=="")
echo "done";
else
    echo $response;*/
?>