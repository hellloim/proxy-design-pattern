from abc import ABCMeta, abstractmethod

#subject interface
class subject(metaclass=ABCMeta):
    @abstractmethod
    def request(self):
        pass

#riktiga subject
class RealSubject(subject):
    def request(self):
        print("RealSubject: Handling wallah")

# Proxy
class Proxy(subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        print("proxy: kollar efter permissions")
        self.real_subject.request()

if __name__ == "__main__":
    # gör en proxy 
    proxy = Proxy()

    #client tar emot requests av proxy 
    proxy.request()

    #gör en proxy
    another_proxy = Proxy()

    #client interacts with the second proxy
    another_proxy.request()

    # väntar (väntar på ssl input)
    input("Press Enter To Exit")

# farmoronlyfans easy abstrachtmethod proxy desgin pattern in python. 
