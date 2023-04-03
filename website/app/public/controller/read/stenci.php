<?php

use ModulePHP\MVC;

MVC::Model("bots");

if (!isset($_GET['id'])) {
    $response['success'] = false;
    $response['status_code'] = 400;
    $response['result'] = 'Não foi passado nenhum parametro';
} else {
    //$empresas = isset($_POST['user']);
    $empresas = new Empresas($_GET['id'],  'Stenci');

    if ($empresas) {
        $response['success'] = $empresas->success;
        $response['status_code'] = $empresas->status_code;
        $response['result'] = $empresas->result;
    } else {
        $response['success'] = false;
        $response['status_code'] = false;
        $response['result'] = "Não foi possivel concluir a ação!";
    }
}


MVC::JsonResponse($response);
