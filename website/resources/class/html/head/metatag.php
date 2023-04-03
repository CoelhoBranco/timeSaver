<?php

namespace ModulePHP\HTML;

use ModulePHP\MVC;
use ModulePHP\Base;

class Metatag
{
    private $content = [];
    public $base;

    function __construct()
    {
        ob_start();

        MVC::Base("head/metatag");

        $this->pushContent(ob_get_contents());
        ob_end_clean();

        if (class_exists('ModulePHP\Base\Metatag')) {
            $this->base = new Base\Metatag;
        }
    }

    function pushContent($content)
    {
        array_push($this->content, $content);
    }

    function render()
    {
        if ($this->base) {
            $this->pushContent($this->base->render());
        }

        $html = "<!-- Metatags -->";
        foreach ($this->content as $content) {
            if (is_string($content)) {
                $html .= $content;
            }
        }

        return $html;
    }
}