<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Insert;
use ModulePHP\Database\Update;

class Empresas
{
    public $table = "Empresas";
    public $status_code = false;
    public $success;
    public $message;
    public $user_id;
    public $empresa;
    public $result;

    public function __construct($user = false, $empresa = false)
    {


        $this->user_id = $user;
        $this->empresa = $empresa;

        $this->result = $this->select_data();
        $response['status_code'] = 200;

        return $response;
    }

   

    public function select_data()
    {
   

        $select = new Select($this->table);
        $this->success = true;
        $this->status_code = 200;

        $query = <<<query
        SELECT user, password FROM Empresas
        WHERE user_id = '$this->user_id'
        AND empresa_name = '$this->empresa'
        query;
        //echo $query;
        return $select->result($query);
    }
}
