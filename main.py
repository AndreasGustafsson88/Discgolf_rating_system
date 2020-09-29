from Classes.courses import Course


def main():
    ymergården = Course("YMERGÅRDEN", "BORÅS", "https://www.pdga.com/tour/event/46819")

    print(ymergården.rating)
if __name__ == "__main__":
    main()
