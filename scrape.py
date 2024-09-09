from urllib import request
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

def scrape():
    dr = webdriver.Chrome()

    url = "https://leetcode.com/problemset/"
    dr.get(url)
    time.sleep(5)
    soup = BeautifulSoup(dr.page_source,"html.parser")
    # with open('data.txt', 'w', encoding="utf-8") as file:
    #     file.write(dr.page_source)

    # with open('data.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()
    # soup = BeautifulSoup(content, 'html.parser')

    daily = soup.find("a", class_ = "h-5 hover:text-blue-s dark:hover:text-dark-blue-s")
    base = "https://leetcode.com"
    path = daily.get("href")

    # print(base + path)

    url = base + path
    dr.get(url)
    time.sleep(5)
    soup = BeautifulSoup(dr.page_source,"html.parser")
    # with open('data2.txt', 'w', encoding="utf-8") as file:
    #     file.write(dr.page_source)

    # with open('data2.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()
    # soup = BeautifulSoup(content, 'html.parser')

    title_elem = soup.find('a', class_ = 'no-underline hover:text-blue-s dark:hover:text-dark-blue-s truncate cursor-text whitespace-normal hover:!text-[inherit]')
    difficulty = soup.find('div', class_ = 'relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-difficulty-medium dark:text-difficulty-medium').text
    
    return f"*Today's LeetCode Daily*\n{title_elem.text}\nLink: {url}\nDifficulty: {difficulty}"
