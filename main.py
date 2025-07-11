import requests
from bs4 import BeautifulSoup
import re
import os

def checkin():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'Origin': 'https://ikuuu.one',
        'Referer': 'https://ikuuu.one/user',
        'Cookie': cookie_data
    }
    url = "https://ikuuu.one/user/checkin"
    response = requests.post(url, headers=headers)
    data = response.json()
    print(f"签到结果: {data['msg']}")

def get_user_traffic():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
        'Origin': 'https://ikuuu.one',
        'Referer': 'https://ikuuu.one/user/code',
        'Cookie': cookie_data
    }
    url = "https://ikuuu.one/user"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找剩余流量信息
    traffic_cards = soup.find_all('div', class_='card-statistic-2')
    
    for card in traffic_cards:
        header = card.find('h4')
        if header and '剩余流量' in header.text:
            # 提取剩余流量数值
            body = card.find('div', class_='card-body')
            if body:
                remaining_traffic = re.sub(r'\s+', ' ', body.get_text(strip=True))
                print(f"剩余流量: {remaining_traffic}")
            
            # 提取今日已用流量
            stats = card.find('div', class_='card-stats-title')
            if stats:
                today_used_text = re.sub(r'\s+', ' ', stats.get_text(strip=True))
                # 提取冒号后的数值部分
                match = re.search(r':\s*(.+)', today_used_text)
                if match:
                    today_used = match.group(1).strip()
                    print(f"今日已用: {today_used}")
                else:
                    print(f"今日使用情况: {today_used_text}")
    
    return soup

cookie_data = os.getenv('COOKIE_DATA', '默认Cookie')

if __name__ == "__main__":
    checkin()
    get_user_traffic()