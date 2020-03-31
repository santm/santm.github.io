+++
title = "Google Page Test, CloudFlare and W3 total Cache"
slug = "2013-07-03-google-page-test-cloudflare-and-w3-total-cache"
published = 2013-07-03T17:32:00+05:30
author = "Santanu Misra"
tags = [ "Technology/Internet", "wordpress", "dns", "CloudFlare", "Tech Notes", "cdn", "w3TotalCache",]
+++
Installed all these three on pamela.santm.com and blog.santm.com which
are running on wordpress 3.6 trunk. moved the dns details to cloudflare.
While Pamela's hobby site did very well Google page test result our blog
result was not great. Looks like the culprit is inbuilt gallery of
wordpress which is re-sizing images and seving them on fly causing high
server time. the command that helped me a lot is "mogrify -strip \*.jpg"
which is part of imagemagick tool kit and removes exif data from
images.  
  
  

[![](../images/thumbnails/2013-07-03-google-page-test-cloudflare-and-w3-total-cache-2013-07-03_1112.png)](../images/2013-07-03-google-page-test-cloudflare-and-w3-total-cache-2013-07-03_1112.png)
