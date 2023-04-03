<?php

namespace ModulePHP;

use stdClass;
use ErrorException;
use Error;

//Sets the default include path.
set_include_path("../");

//Load composer dependencies.
require_once("vendor/autoload.php");

//Load the MVC architecture class.
require_once("resources/class/mvc.php");

//Load system settings.
require_once("config/global.php");
MVC::Resource("config");
$M = new stdClass;
$M->Config = new Config;

//Load pré actions.
require_once("resources/class/preactions.php");

try {
    //Loads system resources.
    MVC::Resource("error");
    MVC::Resource("database/db");
    MVC::Resource("database/select");
    MVC::Resource("database/insert");
    MVC::Resource("database/update");
    MVC::Resource("database/delete");
    MVC::Resource("ldap");
    MVC::Resource("user");
    MVC::Resource("route");
    MVC::Resource("html/html");

    //Starts Kernel execution.
    //Checks if the user is logged in and the validity of the session.
    $M->User = User::auth();

    //Stores the user id and level.
    define("USERID", $M->User->id);
    define("USERLEVEL", $M->User->userlevel);

    //Start the router
    $M->Route = new Route();

    //Starts the HTML renderer.
    $M->HTML = new HTML\Html();

    //Opens the requested route.
    $M->Route->open();

    //Abre a página ou arquivo requisitado.
    try {
        //echo $M->Route->type;
        switch ($M->Route->type) {
            case 'page':
                //echo 
                //print_r($M->HTML->render());
                //print_r($M->Route->content);
                echo $M->HTML->render();
                //echo $M->Route->content;
                break;

            default:
                //echo $M->Route;
                echo $M->Route->content;
                
                break;
        }
    } catch (ErrorException $e) {
        Logger::warning("{$e->getMessage()} IN {$e->getFile()} IN line {$e->getLine()}");
    }
} catch (ErrorException $e) {
    Logger::warning("{$e->getMessage()} IN {$e->getFile()} IN line {$e->getLine()}");
} catch (Error $e) {
    Logger::emergency("{$e->getMessage()} IN {$e->getFile()} IN line {$e->getLine()}");
}