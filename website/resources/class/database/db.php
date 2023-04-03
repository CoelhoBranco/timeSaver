<?php

namespace ModulePHP\Database;

use mysqli;
use Exception;

class Con extends mysqli
{
    function __construct()
    {
        global $M;
        $this->config = $M->Config->database;
        if (
            $this->config->HOST &&
            $this->config->USER &&
            $this->config->PW &&
            $this->config->NAME
        ) {
            parent::__construct(
                $this->config->HOST,
                $this->config->USER,
                $this->config->PW,
                $this->config->NAME,
                $this->config->PORT
            );
            if ($this->connect_error) {
                throw new Exception("Database connection error");
            } else {
                $this->set_charset("utf8");
            }
        } else {
            throw new Exception("Database not defined");
        }
    }
}

class DB
{
    public $status;

    static function escape($string)
    {
        $con = new Con();
        $string = $string === true ? "True" : ($string === false ? "False" : $string);
        $string = $con->real_escape_string($string);
        $con->close();
        return $string;
    }

    static function query($query)
    {
        $con = new Con();
        $return = $con->query($query);
        $con->close();
        if ($return === false) {
            throw new Exception($con->error);
        }
        return $return;
    }
}
