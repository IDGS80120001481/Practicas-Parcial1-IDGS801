class Piramide:
    def __init__(self, num):
        self.num = num

    def build_piramide(self): 
        asteriscos = ""
        for x in range(self.num):
            asteriscos += "*"
            print(asteriscos)

def main():
    num = int(input())
    piramide = Piramide(num)
    piramide.build_piramide()

if __name__ == "__main__":
    main()