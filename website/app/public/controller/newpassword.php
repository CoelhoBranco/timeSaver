<?php
use ModulePHP\MVC as MVC;

//print_r($_POST);
$user = $_POST['user'];
$password = $_POST['password'];
$code = $_POST['code'];

MVC::Model("newpassword");   

$result = new NewPassword($user, $password, $code);

$response['success'] = $result->success;
$response['message'] = $result->message;
$response['status'] = $result->status;

MVC::JsonResponse($response);
?>