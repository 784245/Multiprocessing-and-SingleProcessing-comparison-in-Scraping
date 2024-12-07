# Multiprocessing-and-SingleProcessing-comparison-in-Scraping

The field of data scraping is growing day by day, and the demand for data to feed these giant AI algorithms is increasing rapidly. Additionally, there is a rising demand for data in the analytics domain, where companies need large datasets to stay ahead of their competitors. As a result, the need for data scrapers to extract publicly available data has also increased.

Today, I am going to discuss a technique that can speed up the process of data scraping, as speed matters when extracting large chunks of data. The technique I will discuss is Multiprocessing.

Multiprocessing refers to the execution of multiple concurrent processes in a system, with each process running on a separate CPU or core, as opposed to a single process running at any one time. This technique is useful for CPU-bound tasks, as it enables parallel execution of different parts of a program, improving efficiency and utilizing the processor to its full extent. By using this technique, one can significantly reduce the time needed to complete a task compared to a single-process approach.

In Python, the Global Interpreter Lock (GIL)—famous as the Python lock—limits the execution of threads to one at a time within a single process, even on multi-core machines. Multiprocessing bypasses this limitation because each process runs independently. In Multiprocessing, each process gets its own interpreter and GIL.

I compared two scripts: one with single-processing and the other with multiprocessing. The URLs I am using are for 50 products from Aben and Cole. Thanks to Open Price Engine for providing these URLs. The script will scrape the price of each product using Requests and BeautifulSoup, and then print the time taken to scrape all 50 URLs.

I used Python's multiprocessing.Pool to scrape URLs in parallel:

multiprocessing.Pool(processes=8): Creates a pool of 8 worker processes to handle tasks concurrently.
pool.map(scrape_url, urls): Distributes the scrape_url function across the pool, applying it to each URL in the urls list. The results (URL-price pairs) are collected into a list.
for url, price in results:: Iterates through the results and prints each URL with its corresponding scraped price.
The Results:
Time taken in Single Processing: 2.45 minutes
Time taken in Multiprocessing: 0.40 minutes
Well, multiprocessing saved me two precious minutes for scraping just 50 URLs. Imagine how much time it would save if the URLs were in the hundreds or thousands!


