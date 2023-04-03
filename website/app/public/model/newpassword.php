<?php
use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Update as Update;
use ModulePHP\User as User;
use ModulePHP\Database\DB as DB;

class NewPassword
{
    private $User;
    private $cpf;
    private $code;
    private $password;
    public $success;
    public $error;
    public $status = 400;
    public $message = 'Não foi possível completar o seu pedido!';


    function __construct($username, $password, $code) {
        
        $this->User = new User;
        $username = DB::escape($username);
        $code = DB::escape($code);
        $password = DB::escape(password_hash($password, PASSWORD_DEFAULT));


        $select = new Select("Users");
        $select->column("1");
        $select->where("username", $username);
        
        $user = $select->result("SELECT 1 FROM Users WHERE username = '$username' AND recoverycode = '$code' LIMIT 1");

        $update = new Update("Users");
        
        if (!$user) {
            $this->success = false;
            $this->message = "Código de recuperação expirado!";

            return true;
        }
        
        if (!$update = $update->execute(
            "UPDATE Users
                SET password='$password'
                WHERE username='$username' AND
                recoverycode = '$code'"
        )) {
            $this->success = false;
            $this->message = "Sistema fora do ar, tente novamente mais tarde!";
            return false;
        }

        $this->success = true;
        $this->message = "Senha alterada com sucesso!";
        $this->status = 200; 
        return true;
    }
}