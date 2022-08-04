from Web_App import run_app


def main():
    """
    Main function acting as central point of execution
    :return:
    """
    data = run_app.run()
    display = run_app.DisplayDetails(data.temperature, data.forecast, data.humidity)
    display.__repr__()


if __name__ == '__main__':
    main()
