<?php

namespace ModulePHP\HTML;

use ModulePHP\MVC;

class Html
{
    public $head;
    public $body;
    public $title;

    public function __construct()
    {
        global $M;
        $this->site = $M->Config->site;

        //Importing head modules
        $this->head = new Head();

        //Importing body modules
        $this->body = new Body();
    }

    public function render()
    {
        global $M;

        $head = $this->head->render();
        $body = $this->body->render();

        $html = <<<html
        <!DOCTYPE html>
        <html lang="{$this->site->LANG}" dir="ltr">
            $head
            $body
        </html>
        html;

        return $html;
    }
}

class Head
{
    public $style;
    public $script;
    public $metatag;
    public $favicon;
    public $other;
    public $sw = "";

    public function __construct()
    {
        global $M;
        $this->style = new Style();
        $this->script = new Script();
        $this->metatag = new Metatag();
        $this->favicon = new Favicon();
        $this->other = new Other();

        if ($M->Config->system->PWA) {
            $this->pwa = <<<content
            <link rel="manifest" href="/manifest">
            <script>
                /* Only register a service worker if it's supported */
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('/sw');
                }
            </script>
            content;
        }
    }

    public function render()
    {

        $html = <<<html
<head>
        {$this->style->render()}
        {$this->script->render()}
        {$this->metatag->render()}
        {$this->favicon->render()}
        {$this->other->render()}
        {$this->pwa}
    </head>
html;

        return $html;
    }
}

class Body
{
    public $header;
    public $aside;
    public $main;
    public $footer;

    public function __construct()
    {
        $this->header = new Header();
        $this->aside = new Aside();
        $this->main = new Main();
        $this->footer = new Footer();
    }

    public function render()
    {
        $html = <<<html
<body>
        {$this->header->render()}
        {$this->aside->render()}
        {$this->main->render()}
        {$this->footer->render()}
    </body>
html;

        return $html;
    }
}

class Block
{
    public $classname;
    private $tagname;
    private $content;
    private $type;
    public $base;

    function __construct($type = "body")
    {
        $this->type = $type;
        ob_start();
        $classname = explode('\\', get_class($this));
        $this->classname = ucfirst(end($classname));
        $this->tagname = strtolower($this->classname);

        MVC::Base("$type/$this->tagname");

        if (class_exists("ModulePHP\Base\\$this->classname")) {
            $this->base = new ("ModulePHP\Base\\$this->classname");
            $this->content = $this->base->render();
        } else {
            $this->content = ob_get_contents();
        }

        ob_end_clean();
    }

    function render()
    {
        if ($this->classname == "Main") {
            self::__construct();
        }
        if ($this->type == "head") {
            return <<<content
<!-- $this->tagname -->
        $this->content
content;
        }

        return <<<content
<{$this->tagname}>
            $this->content
        </{$this->tagname}>
content;
    }
}

$bodyblocks = [
    "aside",
    "footer",
    "header",
    "main"
];

$headblocks = [
    "favicon",
    "metatag",
    "other",
    "script",
    "style"
];

foreach ($bodyblocks as $class) {
    eval("
        namespace ModulePHP\HTML;
        class $class extends Block {
            function __construct() {
                parent::__construct();
            }
        }
    ");
}

foreach ($headblocks as $class) {
    $class = ucfirst($class);
    eval("
        namespace ModulePHP\HTML;
        class $class extends Block {
            function __construct() {
                parent::__construct('head');
            }
        }
    ");
}