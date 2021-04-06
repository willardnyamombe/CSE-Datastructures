python
class browser:
    def __init__(self):
        self.website = []
        self.page_visited = None
    def push(self, page_visited):
        return self.website.append(page_visited)
    def pop(self):
        return self.website.pop()
    def check(self):
        return self.website

browser = browser()
#Test 1 is adding the first web page to the website list
print()
print("========Test One========")
browser.push("www.byui.edu")
print()
print(browser.check())
print()
#Test 2 is adding the 2nd web page to the website list
print("========Test Two========")
print()
browser.push("www.facebook.com")
print(browser.check())
print()
#Test 3 is adding the 3rd web page to the website list
print("========Test Three========")
print()
browser.push("www.instagram.com")
print(browser.check())
print()
#Test 4 is removing the last web page visited from the website list
print("========Test Four========")
print()
browser.pop()
print(browser.check())
print()
