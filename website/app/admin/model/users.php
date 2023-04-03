<?php

use ModulePHP\Database\Select as Select;
use ModulePHP\Database\Insert as Insert;
use ModulePHP\User as UserResource;

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;


class User
{
    public $status;
    public $success;
    public $message;


    public function __construct($name, $cpf, $email, $telefone)
    {
        $db = new Insert("Users");

        $query = <<<query
        INSERT INTO Users (
            name,
            username,
            email,
            telefone
            )
            VALUES ('$name', '$cpf', '$email', '$telefone')
        query;
       
        $db->execute($query);
        
        $this->success = true;
        $this->message = 'Usuário criado com sucesso';
        $this->status = 201;
        $subject = 'Usuário criado com sucesso';
        $message = <<<message
        <html>
        <head>
        <title>Usuário criado</title>
        </head>
        <body>
            <h1>Um novo usuário foi criado com o seu endereço de email.</h1>
            <p>Para gerar a sua senha, basta clicar nesse link:</p>
            <a href="https://{$_SERVER['SERVER_NAME']}/recovery>
            https://{$_SERVER['SERVER_NAME']}/recovery
        </body>
        </html>
        message;

        $this->sendMail($email, $subject, $message);


       
    }


    

    function sendMail($to, $subject, $message){

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
            $mail->setFrom('noreply@timesaver.com.br', 'Criação de Usuário - TimeSaver');
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
    
    static public function recovery($username, $email)
    {
    }

    static public function newPassword($username, $password, $code)
    {
    }
}
