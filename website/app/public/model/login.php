<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\DB as DB;
use ModulePHP\User as User;

class Login  
{
    private $User;
    private $username;
    private $inputPW;
    public $success =  false;
    public $error;
    public $status;
    public $status_code;
    
    public function __construct($username=false, $password=false)
    {   
        
        $this->User = new User;
        
        $this->username = DB::escape($username);
        
        $this->inputPW = DB::escape($password);
        $select = new Select;

        if (!$result = $select->result("SELECT password FROM Users WHERE username = '$this->username' LIMIT 1")) {
            $this->success = false;
            $this->status = "Sistema Fora do ar!";
            $this->status_code = 200;
            
            return false;
        }
                
        if (!password_verify($this->inputPW, $result[0]["password"])) {
            $this->success = false;
            $this->status = "Senha incorreta!";
            $this->status_code = 203;
            
            return false;
        }

        if (!$this->User->login($this->username)) {
            $this->success = false;
            $this->status = "Erro ao efetuar login!";
            $this->status_code = 203;
            return false;
            
        }
        
        
        $this->success = true;
        $this->status_code = 202;
        $this->status = "Login efetuado com sucesso";
        
        return true;
    }

}
