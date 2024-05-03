# web_crawler

A python script retrieve all the "href" value where the attribute is &lt;a>. This works well if you use sitemap as the url. Because each company website should have a sitemap which contains all the links. 

It is suggested that you need to configure the function of "append_domain", it will add the "domain url" if the href is not start with "http" or "https".

Notice: This script intends to keep the href value even it is empty. It helps us to understand why it is not mapped to the excel.

The result will output as an excel file in CSV format.

Sample Output: 
https://github.com/rizh09/web_crawler/blob/develop/scraped_data.csv
