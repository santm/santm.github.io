+++
title = "Another weekend"
slug = "2007-01-13-another-weekend"
published = 2007-01-13T08:25:00+05:30
author = "Santanu Misra"
tags = [ "wordpress", "parking", "picture", "nap", "drive", "car", "weekend", "Tech Notes", "rain",]
+++
Well another day! Some techie note ; upgraded the web site to the latest
beta release of Wordpress. And I found some strange behaviour. This is
what I put forward to the mailing list. But with few minute of research
found the root cause.

<span id="more"></span>

WP is adding \[code\]

\[/code\] as extra inside in my \[code\]  

\[/code\]This was one example.\[code\]  
  
\[/code\]

  

It was happening due to **"wp-include/formatting.php".** I use plain
text mode while doing copy-paste between text-editor from my PC to
Wordpress Editor. There are

\[code\]"\\n\\r"(newline)\[/code\]  

Iand those newlines gets formatted as an extra \[code\]

\[/code\]  

I did a quick search and replace on on wp-posts table dump and
re-imported the same to fix the problem was fixed.Well like to change
the header image on the top as well, set a personal one. The image is
from HP Diary(2007) that I got at work. It looked perfect for an Indian
Blog ;) what you say. Well another BBS – Beg Borrow Steal just kidding.
but there is some problem with IE as it does not like it having some
blank between the top black part and the header. Stupid IE

Recently took some pictures of my new car; a small car with diesel I
only drive to the railway station to catch train. The sunset looked like
a perfect time to snap.
