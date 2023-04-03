<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Insert;
use ModulePHP\Database\Update;

class Atividade
{

    public $response;
    public $table = 'Atividade_diaria';

    public function __construct()
    {
        global $M;
        $this->user_id = $M->User->id;
       
    }

    public function insert_data($user_dia, $user_total, $atendimento)
    {
        $data = $this->select_data();
        //print_r($data);
        if ($data) {
            $this->response['success'] = true;
            $this->response['status_code'] = 401;
            $this->response['message'] = 'Os dados já existem. Atualize usando a rota controller/update/atividade';
            $this->response['data'] = '';
            return $data;
        }

        $in = new Insert();
        
        $query = <<<query
            INSERT INTO  $this->table (
                user_id, user_dia, user_total, atendimento)
                VALUES ($this->user_id, '$user_dia', '$user_total', '$atendimento');
            query;

        //echo $query;
        $in->execute($query = $query);

        $this->response['success'] = true;
        $this->response['status_code'] = 201;
        $this->response['message'] = 'Dados inseridos com sucesso';
        $this->response['data'] = '';
        return true;
    }

    public function update_data($user, $user_id, $password)
    {

        $query = <<<query
                UPDATE $this->table
                SET password = '$password', 
                user = '$user'
                WHERE user_id = '$user_id'
            query;
        #query de update
        //print_r($query);
        $up = new Update();
        $up->execute($query);

        $this->response['success'] = true;
        $this->response['status_code'] = 200;
        $this->response['message'] = 'Dados atualizados com sucesso';
        $this->response['data'] = '';

        return true;
    }

    public function select_data()
    {
        global $M;

        $user_id = $M->User->id;

        $select = new Select($this->table);

        $query = <<<query
        SELECT (atendimento_contador) FROM Atividade_diaria

        WHERE user_id = '$user_id'
        AND registration_date > curdate();
        query;

        //echo $query;
        $data = $select->result($query);
      
        if (!$data) {
            $this->response['data'] = array("atendimento_contador" => 0, "user_total" => 0, "atendimento" => 0);
            $data[0] = [];
        }

        $query = <<<query
        SELECT  SUM(atendimento_contador) AS user_total , SUM(atendimento_contador)  as atendimento FROM $this->table

        
        WHERE user_id = '$user_id'
                      

        query;

        //print_r($data);
        $data1 = $select->result($query);
        $data[0] = $data[0] + $data1[0];
    
        


        $this->response['data'] = $data[0];
        $this->response['success'] = true;
        $this->response['status_code'] = 200;
        $this->response['message'] = '';


        return $data;
    }
}
