<?php

namespace ModulePHP;

class Config
{
    public function __construct()
    {
        $path = dirname(dirname(dirname(__FILE__))) . "/config";
        $dir = dir($path);
        while ($arquivo = $dir->read()) {
            $ext = pathinfo($arquivo, PATHINFO_EXTENSION);
            if ($ext == "env") {
                $name = pathinfo($arquivo, PATHINFO_FILENAME);
                $this->{$name} = (object) parse_ini_file("$path/$arquivo");
            }
        }
    }
}