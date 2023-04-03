<?php

use ModulePHP\MVC;

MVC::Model("profissionais");
/*
$_POST['user_dia'] = 1;
$_POST['user_total'] = 1;
$_POST['atendimento'] = 1;
*/

$_POST['name'] = 1;
$_POST['cpf'] = 1;
$_POST['conselho_id'] = 1;
$_POST['uf'] = 1;
$_POST['registro'] = 1;
$_POST['cbo'] = 1;
$_POST['cod_operadora'] = 1;

$profissionais = new Profissionais();

if ($profissionais->select_data()) {
    $response['status_code'] = 400;
    $response['message'] = 'O usuário já possui cadastro no banco!';
} else {
    if (isset($_POST['name'])) {
 
        $r = $profissionais->insert_data(
            $_POST['name'],
            $_POST['cpf'],
            $_POST['conselho_id'],
            $_POST['uf'],
            $_POST['registro'],
            $_POST['cbo'],
            $_POST['cod_operadora']
        );

        //print_r($atividade->response);
        $response = $profissionais->response;
    }
}



MVC::JsonResponse($response);
