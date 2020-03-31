+++
title = "Create Banner with mirror effect by ImageMagick"
slug = "2005-11-18-create-banner-with-mirror-effect-by-imagemagick"
published = 2005-11-18T09:11:00+05:30
author = "Santanu Misra"
tags = [ "Imagemagick", "mirror effect", "Tech Notes",]
+++
[![](../images/thumbnails/2005-11-18-create-banner-with-mirror-effect-by-imagemagick-Banner-Mirror-Imagemagick.jpg)](../images/2005-11-18-create-banner-with-mirror-effect-by-imagemagick-Banner-Mirror-Imagemagick.jpg)

  

A simple way to create a text image which will have mirror effects. The
best part of this you do not have to use any fancy imging software and
it takes only few seconds to create the same. The code a single line to
make it easier for Windows

> *<span
> style="background-color: #999999; font-family: Verdana, sans-serif;">convert
> -size 460x130 xc:white -font forte -pointsize 72 -fill "\#cccccc"
> -annotate 0x180+12+80 "Banner Mirror" -gaussian 0x2 -stroke black
> -strokewidth 1 -fill "\#80904F" -stroke black -strokewidth 1 -annotate
> 0x0+12+55 "Banner Mirror" -draw "line 0,68 430,68"
> Banner-Mirror-Imagemagick.jpg</span>*
