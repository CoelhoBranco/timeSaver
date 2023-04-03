<?php

namespace ModulePHP\HTML;

use ModulePHP\MVC;
use ModulePHP\Base;

$filename = ucfirst(basename(__FILE__, ".php"));

$newClass = new class
{
}; //create an anonymous class
$newClassName = get_class($newClass);
class_alias($newClassName, $classname);

$newClass = new class extends block
{
    private $classname;
    private $tagname;
    private $content;
    public $base;

    function __construct()
    {
        ob_start();

        $this->classname = get_class($this);
        $this->tagname = strtolower($this->classname);

        MVC::Base("body/$this->tagname");

        if (class_exists("ModulePHP\Base\{$this->classname}")) {
            $this->base = new ("ModulePHP\Base\{$this->classname}");
            $this->content = $this->base->render();
        } else {
            $this->content = ob_get_contents();
        }

        ob_end_clean();
    }

    function render()
    {
        $html = <<<content
        <{$this->tagname}>
            $this->content;
        </{$this->tagname}>
        content;

        return $html;
    }
};