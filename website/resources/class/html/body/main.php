<?php

namespace ModulePHP\HTML;

use ModulePHP\MVC;
use ModulePHP\Base;

class Main
{
    public $base;

    function render()
    {
        global $M;

        ob_start();

        MVC::Base("body/main");

        if (class_exists('ModulePHP\Base\Main')) {
            $this->base = new Base\Main;
            $content = $this->base->render();
        } else {
            $content = ob_get_contents();
        }

        ob_end_clean();

        if (empty($content)) {
            $content = $M->Route->content;
            
        }

        $html = <<<content
        <main>
            $content
        </main>
        content;

        return $html;
    }
}