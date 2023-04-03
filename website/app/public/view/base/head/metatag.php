<?php

namespace ModulePHP\Base;

class Metatag
{
    public function render()
    {
        global $M;
        $SITE = $M->Config->site;

        $content = <<<content
        <title>$SITE->NAME</title>
        <meta name="description" content="$SITE->DESCRIPTION ">
        <meta name="theme-color" content="$SITE->COLOR1"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="apple-touch-icon" href="$SITE->LOGO">
        content;

        return $content;
    }
}
