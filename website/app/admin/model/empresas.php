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
    public function __construct($user = false, $password = false, $empresa = false)
    {

        global $M;

        $user_id = $M->User->id;
        $result = $this->select_data();
        $response['status_code'] = false;

        if (!$result) {
            #update 
            $this->success = $this->insert_data(
                $user_id,
                $empresa,
                $user,
                $password
            );
            $this->status_code = 200;
            $this->message = 'Registro criado com sucesso!';

        } else {
            $user = $result[0]['user'];
            //print_r($user);
            $this->success = $this->update_data($user, $user_id, $password);
            $this->status_code = 200;
            $this->message = 'Registro atualizado com sucesso!';
        }

        return $response;
    }

    public function insert_data($user_id, $empresa, $user, $password)
    {
        # code...
        $in = new Insert();

        $query = <<<query
            INSERT INTO Empresas (
                user_id, empresa_name, user, password)
                VALUES ($user_id, '$empresa', '$user', '$password');
            query;

        //echo $query;
        $in->execute($query = $query);

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
        return true;
    }

    public function select_data()
    {
        global $M;

        $user_id = $M->User->id;

        $select = new Select($this->table);

        $query = <<<query
        SELECT * FROM Empresas
        WHERE user_id = '$user_id'
        query;
        //echo $query;
        return $select->result($query);
    }
}
