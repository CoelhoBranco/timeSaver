<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Insert;
use ModulePHP\Database\Update;

class Profissionais
{
    public $table = "Profissionais";
    public $status_code = 400;
    public $success;
    public $message;
    public $response;
    public $user_id;

    public function __construct() {
        global $M;

        $this->user_id = $M->User->id;
     

    }

    public function insert_data($name, $cpf, $conselho_id, $uf, $registro, $cbo, $cod_operadora) 
    {
        $in = new Insert;
        $query = <<<query
            INSERT INTO  $this->table (
                user_id, name, CPF, conselho_id, UF, registro, CBO, cod_operadora)
                VALUES ($this->user_id, '$name', '$cpf', '$conselho_id',
                '$uf', '$registro', '$cbo', '$cod_operadora'
            );
            query;

        //echo $query;
        $in->execute($query = $query);

        $this->response['success'] = true;
        $this->response['status_code'] = 201;
        $this->response['message'] = 'Dados inseridos com sucesso';
        
        return true;
    }

    public function select_data()
    {
        global $M;

        $user_id = $M->User->id;

        $select = new Select($this->table);

        $query = <<<query
        SELECT * FROM $this->table
        WHERE user_id = '$user_id'
        query;
        
        //echo $query;
        $data = $select->result($query);
        $this->response['data'] = $data[0];
        $this->response['success'] = true;
        $this->response['status_code'] = 200;
        $this->response['message'] = '';
        

        return $data;
    }

    


}