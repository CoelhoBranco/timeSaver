<?php

namespace ModulePHP\Base;

class Main
{
    public function render()
    {
        global $M;
        return $M->Route->content;
    }
}
