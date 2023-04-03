<?php

namespace ModulePHP\Base;

class Style
{
    public function render()
    {
        $content = <<<content
        <link rel="stylesheet" href="assets/css/style.css">
        <link rel="stylesheet" href="https://cdn.es.gov.br/fonts/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="assets/css/menu.css">
        content;

        return $content;
    }
}
