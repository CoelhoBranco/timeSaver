<?php
global $M;
$SITE = $M->Config->site;

echo <<<content
{
  "name": "$SITE->NAME",
  "short_name": "$SITE->NAME",
  "start_url": "/",
  "display": "standalone",
  "background_color": "$SITE->COLOR1",
  "theme_color": "$SITE->COLOR1",
  "description": "$SITE->DESCRIPTION",
  "icons": [
    {
      "src": "$SITE->LOGO",
      "sizes": "48x48",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "72x72",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "96x96",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "144x144",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "168x168",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "192x192",
      "type": "image/png",
      "purpose": "any maskable"
    },
    {
      "src": "$SITE->LOGO",
      "sizes": "512x512",
      "type": "image/png",
      "purpose": "any maskable"
    }
  ],
  "related_applications": [
    {
      "platform": "web",
      "url": "https://modulephp.com"
    },
    {
      "platform": "play",
      "url": "https://play.google.com/store/apps/details?id=duxtec.modulephp"
    }
    ]
  }
content;
