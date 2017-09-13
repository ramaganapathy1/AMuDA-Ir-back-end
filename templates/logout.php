<?php
/**
 * Created by PhpStorm.
 * User: ramaganapathy1
 * Date: 7/9/17
 * Time: 3:52 PM
 */
session_start();
session_unset();
session_destroy();
header('Location: http://localhost:8000/index.php?id=success');
?>