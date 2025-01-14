# rename file thorugh by module

# import os

# directory = r'C:\Users\SUSANTA RAUT\OneDrive\Desktop\python'

# for filename in os.listdir(directory):
#     if filename.endswith('.txt'):
#         new_name = filename.replace('old', 'new')
#         os.rename(os.path.join(directory, filename), os.path.join(directory,new_name))



# remove file through by module

# import os 
# import datetime

# directory = r'C:\Users\SUSANTA RAUT\OneDrive\Desktop\python'
# threshold_date = datetime.datetime(2025 , 1 , 1)

# for filename in os.listdir(directory):
#     filepath = os.path.join(directory,filename)
#     if os.path.isfile(filepath) and os.path.getmtime(filepath) < threshold_date.timestamp():
#         os.remove(filepath)
        

        
# this is the webscraping

# import requests
# from bs4 import BeautifulSoup # type: ignore

# url = 'https://www.netflix.com/in/'
# response = requests.get(url)
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     links = [link['href'] for link in soup.find_all('a')]
#     print(links)

# else:
#     print(f"faild to fetch the url. status code :{response.staus_code}")

    
    
    
import schedule
import time

def job():
    print("This is a scheduled task.")

# Schedule the job to run at 5:51 AM daily
schedule.every().day.at("05:51").do(job)

# Keep the script running to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)



#system shutdown 


# import os

# os.system("shutdown /s /t 0")
# # don't execute the code otherwise system will shutdown



