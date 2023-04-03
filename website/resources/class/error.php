<?php

namespace ModulePHP;

use Monolog\Logger as Log;
use Monolog\Handler\StreamHandler;



class Logger
{
    static function emergency($message = false)
    {
        global $M;
        $message = $message ? $message : $M->Config->message->UNAVAILABLE;
        self::action($message, Log::EMERGENCY);
    }

    static function warning($message = false)
    {
        global $M;
        $message = $message ? $message : $M->Config->message->UNAVAILABLE;
        self::action($message, Log::WARNING);
    }

    static function action($message = false, $level = Log::DEBUG)
    {
        global $M;
        $message = $message ? $message : $M->Config->message->UNAVAILABLE;
        $log = new Log("Kernel");
        $datetime = date("Y-m-d");
        $log->pushHandler(new StreamHandler("../logs/$datetime.log", $level));
        $log->warning($message);

        if (!DEBUG) {
            $message = $M->Config->message->UNAVAILABLE;
        }

        global $M;

        if (isset($M->Route->type)) {
            switch ($M->Route->type) {
                case 'page':
                    echo "<h1>$message<h1>";
                    break;
                default:
                    $message = array(
                        'success' => false,
                        'status' => $message
                    );
                    MVC::JsonResponse($message);
            }
        } else {
            echo "<h1>$message<h1>";
        }
    }
}
