import subprocess


def crawl_nse_site():
    print "* Crawling NSE site... *\n"
    subprocess.call(["scrapy", "crawl", "companies", "-o", "test.jl"])
    print "\n\n * Done Crawling *\n\n"

if __name__ == '__main__':
    crawl_nse_site()
