<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Update as Update;
use ModulePHP\User as User;
use ModulePHP\Database\DB as DB;

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

class Recovery
{
    private $User;
    private $username;
    private $email;
    private $codigo;
    public $success = false;
    public $error2= false;
    public $status = false;

    public $code = false;

    function __construct($username, $email)
    {

        $this->username = DB::escape($username);
        $this->email = DB::escape($email);

        $select = new Select("Users");
        $select->column("1");
        $select->where("username", $username);

        $user = $select->result("SELECT 1 FROM Users WHERE username = '$this->username' AND email = '$this->email' LIMIT 1");

        $update = new Update("Users");

        if (!$user) {
            $this->success = false;
            $this->status = "Usuário inexistente!";
            $this->code = 400;


            return false;
        }

        $this->codigo = bin2hex(openssl_random_pseudo_bytes(32, $cstrong));

        if (!$update = $update->execute(
            "UPDATE Users
                SET recoverycode='$this->codigo'
                WHERE username='$this->username' AND
                email = '$this->email'"
        )) {
            $this->success = false;
            $this->status = "Sistema fora do ar, tente novamente mais tarde!";
            return false;
        }

        $message = <<<message
        <html>
        <head>
        <title>Nova senha de acesso.</title>
        </head>
        <body>
            <h1>Nova senha de acesso.</h1>
            <p>Use o link abaixo para gerar uma nova senha.</p>
            <a href="http://{$_SERVER['SERVER_NAME']}/newpassword?user=$this->username&code=$this->codigo">
            http://{$_SERVER['SERVER_NAME']}/newpassword?user=$this->username&code=$this->codigo
        </body>
        </html>
        message;

        $to = $this->email;
        $subject = "Pedido de recuperação de senha de acesso.";

        $headers[] = "MIME-Version: 1.0";
        $headers[] = "Content-type: text/html; charset=utf-8";
        $headers[] = "To: <$this->email>";
        $headers[] = "From: NoReply <noreply@{$_SERVER['SERVER_NAME']}>";

        if (!$this->sendMail($to, $subject, $message, implode("\r\n", $headers))) {
            $this->success = false;
            $this->error2 = implode("\r\n", $headers);
            $this->code = 400;
            $this->status = "Erro ao enviar o e-mail de recuperação, tente novamente mais tarde!";
            return false;
        }

        $this->success = true;
        $this->status = "E-mail de recuperação enviado com sucesso, verifique sua caixa de entrada!";
        $this->code = 200;
        return true;
    }


    function sendMail($to, $subject, $message, $headers){

        $mail = new PHPMailer(true);
        try {
            //Server settings
            //SMTP::DEBUG_OFF = off;
            $mail->SMTPDebug = SMTP::DEBUG_OFF;  
            $mail->CharSet = "UTF-8";                    //Enable verbose debug output
            $mail->isSMTP();                                            //Send using SMTP
            $mail->Host = 'mboxhosting.com';               //Set the SMTP server to send through
            $mail->SMTPAuth   = true;     
            $mail->SMTPSecure = 'tls';                              //Enable SMTP authentication
            $mail->Username   = 'noreply@timesaver.com.br';  
            //$mail->Username   = 'contato@timesaver.com.br';                     //SMTP username
            //$mail->Password   = 'P!mrMZKp38b~RB[i';     
            $mail->Password   = 'timesaverreply1';                              //SMTP password
            //$mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;            //Enable implicit TLS encryption
            $mail->Port       = 25;                                    //TCP port to connect to; use 587 if you have set `SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS`
            $mail->setLanguage('pt-bt');
            //Recipients
            $mail->setFrom('noreply@timesaver.com.br', 'Recuperação de Senha - TimeSaver');
            $mail->addAddress($to);     //Add a recipient
            
    
            //Attachments
           
            //Content
            $mail->isHTML(true);                                  //Set email format to HTML
            $mail->Subject = $subject;
            $mail->Body    = $message;
            
                    
            $mail->send();
            
            return True;
        } catch (Exception $e) {
            $this->status =  "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
        }
    }
}
