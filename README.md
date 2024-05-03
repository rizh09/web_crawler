# web_crawler

A python script retrieve all the "href" value where the attribute is &lt;a>. This works well if you use sitemap as the url. Because each company website should have a sitemap which contains all the links. 

It is suggested that you need to configure the function of "append_domain", it will add the "domain url" if the href is not start with "http" or "https".

The result will output as an excel file in CSV format.
