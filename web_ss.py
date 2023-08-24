from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

options = Options()
options.headless = True
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(options=options)


def screenshot(url, r_id):
    sentences = []
    driver.get(url)

    try:
        read_more = driver.find_element(By.ID, f"t3_{r_id}-read-more-button")
        read_more.click()
    except Exception:
        print("did not click")

    ctr = 0

    post_title = driver.find_elements(By.CLASS_NAME, "text-neutral-content-strong")[1]
    try:
        os.makedirs(f"screenshots/{r_id}")
    except FileExistsError:
        pass
    post_title.screenshot(f"screenshots/{r_id}/{ctr}.png")

    body = driver.find_elements(By.CLASS_NAME, "text-neutral-content")[2]
    speeches = body.find_elements(By.TAG_NAME, "p")

    if len(speeches) < 30:
        for speech in speeches:
            ctr += 1
            print("-"*50)
            print(speech.text)
            try:
                speech.screenshot(f"screenshots/{r_id}/{ctr}.png")
                sentences.append(speech.text)
            except Exception as e:
                ctr -= 1
                print(e)
        # driver.quit()

        return sentences
    return None


if __name__ == "__main__":
    driver.get("https://www.reddit.com/r/AntiworkPH/comments/15lemcn/dahil_sa_work/")
    body = driver.find_elements(By.CLASS_NAME, "text-neutral-content")[2]

    speeches = body.find_elements(By.TAG_NAME, "p")

    img = driver.find_element(By.ID, "post-image")
    print(img.get_attribute("src"))

    for speech in speeches:
        print("text:", speech.text)

    # body = driver.find_elements(By.CLASS_NAME, "text-neutral-content")[2]
    # speeches = body.find_elements(By.TAG_NAME, "p")

    # paragraph = driver.find_elements(By.CLASS_NAME, "text-neutral-content-strong")
    # print(paragraph[1].text)
    # driver.quit()

    print("end...")
