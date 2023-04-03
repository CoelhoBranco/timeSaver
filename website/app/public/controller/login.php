<?php

use ModulePHP\MVC;
//print_r($_POST);
MVC::Model("login");
//$_POST['user'] = '17434838728';
//$_POST['pw'] = 'teste';

$login = isset($_POST['user']);

if ($login){
    $login = new Login($_POST['user'], $_POST['pw']);
    //print_r($login);
    $response['success'] = $login->success;
    $response['status'] = $login->status;
    $response['status_code'] = $login->status_code;
}
MVC::JsonResponse($response);