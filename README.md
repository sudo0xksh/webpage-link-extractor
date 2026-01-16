# 🔗🔥 Webpage Link Extractor 🔥🔗

Webpage Link Extractor is a simple Python CLI tool that fetches a webpage
and extracts all the links (`<a href="">`) from it using BeautifulSoup 🧠🍲

If a page has links, this tool will find them.
No scrolling. No viewing source. No pain.

---

## 👀 Overview

Every webpage is full of links.
Some are useful.
Some are hidden.
Some lead to interesting places 👀🌐

This tool takes a webpage URL, parses the HTML,
and prints every link it can find directly to the terminal.

Clean extraction.
No filtering.
No judgement.

---

## 🚀 Features

- Fetches any HTTP or HTTPS webpage 🌍  
- Parses HTML using BeautifulSoup 🍜  
- Extracts all anchor tag links 🔗  
- Prints results directly to terminal 🖥️  
- Simple, fast, and beginner-friendly ⚡  

---

## ⚙️ How It Works

The tool sends an HTTP request to the target page,
parses the HTML response,
and scans for all `<a>` tags.

For each anchor tag, it extracts the `href` value
and prints it as-is.

If it’s a link, it shows up.
If it’s not, it gets ignored.

---

## 🧪 Usage

Run the program  
python webpage_linkext.py

Enter the webpage URL when prompted  
(make sure it starts with http or https)

The tool will then print all extracted links instantly 😎

---

## 📤 Example Output

https://example.com/login  
https://example.com/register  
https://cdn.example.com/assets/app.js  

Extraction Completed!

---

## 📦 Requirements

- Python 3.x  
- requests library  
- beautifulsoup4 library  

Install dependencies if needed  
pip install requests beautifulsoup4

---

## 🧠 What You Learn From This Project

- HTML parsing basics  
- How link extraction works  
- Using BeautifulSoup for scraping  
- Why links are important in recon  
- How webpages are interconnected  

---

## 🗿 Final Words

Webpages hide paths.
Links reveal them.

If you can extract links fast,
you can explore faster 🔥🔗
