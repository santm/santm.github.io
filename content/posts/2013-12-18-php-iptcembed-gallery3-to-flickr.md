+++
title = "PHP iptcembed Gallery3 to Flickr"
slug = "2013-12-18-php-iptcembed-gallery3-to-flickr"
published = 2013-12-18T18:37:00+05:30
author = "Santanu Misra"
tags = [ "iptc", "hosting", "gallery 3", "PHP", "flickr",]
+++
A journey of sharing photo only got me into having a website of my own.
When digital camera came out with decent mega pixel was an early adapter
of the same. But soon realized sharing Pictures on email was not an
option and  hosted pictures  on Tripod. Oh! they used to give 10MB of
free hosting :) now Flicker gives one 1TB free. So long  story small
after the managing own gallyery app writen initally with csv and php ,
later mysql and php and lastly Gallery for almost 10 years. found
gallery development is kind of not that active it used to be. So thought
of moving into Flickr which was big no in-between as they had
restriction on free accounts. But now those restriction gone managing
7000+ picture and importing them with proper details remained a BIG
challenage. At last came up with **iptcembed ** where all the details
where written into  JPEG file itself and imported those image as set to
Flickr.And all your details, tag, captions are set properly.

  
Here is how I did it  
  
1. Copy Gallery's items table to temp table so we do not mess with live
data  
2. Add a new column to the temp table  

> <span class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-decoration: none; text-transform: uppercase; text-underline: none;">ALTER</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #235a81; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-decoration: none; text-underline: none;"> </span></span><span
> class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-decoration: none; text-transform: uppercase; text-underline: none;">TABLE</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxquote"><span
> style="background: #E5E5E5; color: green; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;">\`Yours\_G3\_items-new\`</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-transform: uppercase;">ADD</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxquote"><span
> style="background: #E5E5E5; color: green; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;">\`album\_name\`</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxalpha"><span
> style="background: #E5E5E5; color: #ff9900; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-transform: uppercase;">TEXT</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-decoration: none; text-transform: uppercase; text-underline: none;">NOT</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-transform: uppercase;">NULL</span><span
> style="color: #990099; text-transform: uppercase;"></span>**</span>

3\. Find out the parent album id of each items and add that data in the
new column.  

> <span class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-decoration: none; text-transform: uppercase; text-underline: none;">UPDATE</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background: #E5E5E5; color: magenta; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items-new</span>,</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items</span>  </span></span><span
> class="syntaxalpha">**<span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; color: #990099; font-family: Arial, sans-serif; font-size: 10.5pt; text-transform: uppercase;">SET</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background: #E5E5E5; color: magenta; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items-new</span>.</span></span><span
> class="syntaxalpha"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; font-family: Arial, sans-serif; font-size: 10.5pt;">album\_name</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; color: magenta; font-family: Arial, sans-serif; font-size: 10.5pt;">=</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background: #E5E5E5; color: magenta; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items</span>.</span></span><span
> class="syntaxalpha"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; font-family: Arial, sans-serif; font-size: 10.5pt;">title</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxalpha">**<span
> style="background: #E5E5E5; color: #990099; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt; text-transform: uppercase;">WHERE</span>**</span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background: #E5E5E5; color: magenta; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items-new</span>.</span></span><span
> class="syntaxalpha"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; font-family: Arial, sans-serif; font-size: 10.5pt;">parent\_id</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; color: magenta; font-family: Arial, sans-serif; font-size: 10.5pt;">=</span></span><span
> class="apple-converted-space"><span
> style="background: #E5E5E5; color: #444444; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"> </span></span><span
> class="syntaxpunct"><span
> style="background: #E5E5E5; color: magenta; font-family: &quot;Arial&quot;,&quot;sans-serif&quot;; font-size: 10.5pt;"><span
> style="color: green; font-family: Arial, sans-serif;">Yours\_G3\_items</span>.</span></span><span
> class="syntaxalpha"><span
> style="background-color: #e5e5e5; background-position: initial initial; background-repeat: initial initial; font-family: Arial, sans-serif; font-size: 10.5pt;">id</span></span>

4\. Export the new table with "|" as separator and "" as enclosed.  
  
Now the PHP script  

> <span style="background-color: #cccccc; color: #741b47;">&lt;?  
> //File to be opened  
> $file="/tmp/csv.txt";  
> $gallery\_album\_base = ..../gallery3/var/albums";  
> $new\_gallery\_album\_base = &lt;new location&gt;/albums" ;  
> //  
> $handle = fopen($file, 'r') or die ("Fail to open input file \\n\\r")
> ;  
> $ln= 0 ;  
> // Some Functions Start  
> function csv\_explode($delim='|', $str, $enclose='"',
> $preserve=false){  
> $resArr = array();  
> $n = 0;  
> $expEncArr = explode($enclose, $str);  
> foreach($expEncArr as $EncItem){  
> if($n++%2){  
> array\_push($resArr, array\_pop($resArr) . ($preserve?$enclose:'') .
> $EncItem.($preserve?$enclose:''));  
> }else{  
> $expDelArr = explode($delim, $EncItem);  
> array\_push($resArr, array\_pop($resArr) .
> array\_shift($expDelArr));  
> $resArr = array\_merge($resArr, $expDelArr);  
> }  
> }  
> return $resArr;  
> }  
>   
> // iptc\_make\_tag() function by Thies C. Arntzen  
> function iptc\_make\_tag($rec, $data, $value)  
> {  
> $length = strlen($value);  
> $retval = chr(0x1C) . chr($rec) . chr($data);  
> if($length &lt; 0x8000)  
> {  
> $retval .= chr($length &gt;&gt; 8) . chr($length & 0xFF);  
> }  
> else  
> {  
> $retval .= chr(0x80) .  
> chr(0x04) .  
> chr(($length &gt;&gt; 24) & 0xFF) .  
> chr(($length &gt;&gt; 16) & 0xFF) .  
> chr(($length &gt;&gt; 8) & 0xFF) .  
> chr($length & 0xFF);  
> }  
> return $retval . $value;  
> }  
> // Some Functions End  
> while ($line = fgets ($handle)){  
> $line = str\_ireplace("\\x0D", "", $line);  
> $line = urldecode ($line);  
> ++$ln;  
> print ("just line : $ln \\n");  
> if ($line===FALSE) print ("FALSE\\n");  
> else {  
> //print ("I am $ln \\n");  
> //print ($line) ;  
> $variables = csv\_explode ("|", $line);  
> //print\_r ($variables);  
> //26(album or photo) 25(title), 13(image\_path),
> 4(details),33(album\_name/tag)  
>   
> if ( $variables\[26\] == photo ){  
> //Path new and old path  
> $old\_path = $gallery\_album\_base . '/' . $variables\[13\];  
> $image\_name\_new = $new\_gallery\_album\_base . '/' .
> $variables\[13\];  
> $path\_parts = pathinfo ($image\_name\_new);  
> if (!file\_exists($path\_parts\['dirname'\])) {  
> print ("makeing directory {$path\_parts\['dirname'\]} \\n") ;  
> mkdir ($path\_parts\['dirname'\], 0777,true);  
> }  
>   
> // Set the IPTC tags  
> $iptc = array(  
> '2\#120' =&gt; "$variables\[4\]",  
> '2\#105' =&gt; "$variables\[25\]",  
> '2\#005' =&gt; "$variables\[25\]",  
> '2\#015' =&gt; "$variables\[33\]",  
> '2\#116' =&gt; 'Copyright, www santm com'  
> );  
> // Convert the IPTC tags into binary code  
> $data = '';  
> foreach($iptc as $tag =&gt; $string)  
> {  
> $tag = substr($tag, 2);  
> $data .= iptc\_make\_tag(2, $tag, $string);  
> }  
> // Embed the IPTC data  
> $content = iptcembed($data, $old\_path);  
> // Write the new image data out to the file.  
> $fp = fopen($image\_name\_new, "wb");  
> fwrite($fp, $content);  
> fclose($fp);  
> print ("working on $image\_name\_new \\n");  
> //$size = getimagesize($image\_name\_new, $info);  
> //if(isset($info\['APP13'\]))  
> //{  
> // $iptc = iptcparse($info\['APP13'\]);  
> // var\_dump($iptc);  
> //}  
> } //end of if photo loop  
> } // end of else loop  
> } // end of while loop  
> \# Close the File.  
> fclose($handle);  
> ?&gt;</span>

I Wish there was API where I could import the image from my old hosting
company to Flickr directly instead of uploading them via their PC
up-loader.  
  
More here on major phpfunction  
  
http://www.php.net/function.iptcembed  
http://www.php.net/function.pathinfo  
http://php.net/manual/fr/function.explode.php
