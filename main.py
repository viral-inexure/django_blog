import os

if __name__ == '__main__':

    for x in os.environ:
        print(os.environ.get('EMAIL_USER'))
        print(os.environ.get('EMAIL_PASS'))
        # print((x, os.getenv(x)))