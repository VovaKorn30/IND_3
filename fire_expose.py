import utils
import fire

def main():
    """
    Fire-util to grant access to all utils methods via command line

    available methods:
        python ind_3\fire_expose.py great [name]
        python ind_3\fire_expose.py goodbye [name]
    """
    fire.Fire(utils)

if __name__ == '__main__':
    main()
