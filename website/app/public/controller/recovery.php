<?php
use ModulePHP\MVC as MVC;

//print_r($_POST);
$user = $_POST['user'];
$email = $_POST['email'];


MVC::Model("recovery");   
$result = new Recovery($user, $email);

$response['success'] = $result->success;
$response['error'] = $result->error2;
$response['status'] = $result->status;
$response['code'] = $result->code;


MVC::JsonResponse($response);
?>