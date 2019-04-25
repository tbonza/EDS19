/* Queries used for Google Big Query 
 *  
 * GHTorrent is available on BigQuery so I ran a series of
 * queries to get the repositories of interest
 */


-- Find all Apache repos on GitHub

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/apache/";

-- Find all Google opensource org on GitHub

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/google/";

-- Find all Facebook opensource org on GitHub

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/facebook/";

-- Find all Microsoft opensource org on GitHub

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/Microsoft/";

-- Find all edX repos

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/edx/";

-- Find all tensorflow repos

SELECT url FROM [ghtorrent-bq:ght.projects] WHERE url CONTAINS "/tensorflow/";

/* We want to combine all these queries to output one table
 *
 */

SELECT url
FROM [ghtorrent-bq:ght.projects]
WHERE
   url CONTAINS "/apache/" OR
   url CONTAINS "/google/" OR
   url CONTAINS "/facebook/" OR
   url CONTAINS "/Microsoft/" OR
   url CONTAINS "/edx/" OR
   url CONTAINS "/tensorflow/";

