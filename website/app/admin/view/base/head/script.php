<?php

namespace ModulePHP\Base;

class Script
{
    public function render()
    {
        $content = <<<content
            <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
        content;

        return $content;
    }
}
