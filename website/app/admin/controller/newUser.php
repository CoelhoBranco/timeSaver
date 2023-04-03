<?php
use ModulePHP\MVC as MVC;


$user = $_POST['nomeCad'];
$cpf = $_POST['cpfCad'];
$email = $_POST['emailCad'];
$telefone = $_POST['telefoneCad'];


MVC::Model("users");   

$result = new User($user, $cpf, $email, $telefone);

$response['success'] = $result->success;
$response['message'] = $result->message;
$response['status'] = $result->status;


MVC::JsonResponse($response);
?>