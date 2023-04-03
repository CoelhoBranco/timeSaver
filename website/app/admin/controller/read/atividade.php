<?php

use ModulePHP\MVC;

MVC::Model("atividade");



    //print_r($_POST);

    $atividade = new Atividade();
    $r = $atividade->select_data();
   
    //print_r($atividade->response);

MVC::JsonResponse($atividade->response);
/*

if (!isset($_POST['data'])) {
    $response['success'] = false;
    $response['status_code'] = 400;
    $response['message'] = 'Não foi passado nenhum parametro';
} else {
    $data = (json_decode($_POST['data'], true));

    //$empresas = isset($_POST['user']);
    $empresas = new Empresas($data['user'], $data['password'], $data['empresa']);

    if ($empresas) {
        $response['success'] = $empresas->success;
        $response['status_code'] = $empresas->status_code;
        $response['message'] = $empresas->message;
    } else {
        $response['success'] = false;
        $response['status_code'] = false;
        $response['message'] = "Não foi possivel concluir a ação!";
    }
}


MVC::JsonResponse($response);
*/