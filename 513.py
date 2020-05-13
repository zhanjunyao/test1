import argparse

parser = argparse.ArgumentParser(description = 'TEST')
parser.add_argument ('--start-epoch', default = 0, type = int, help = 'please input number')

def main():
    global args
    args = parser.parse_args()

    print(args)
    print(args.start_epoch)

if __name__ == '__main__':
    # main()
    from pathlib import Path
    p=Path(r'F:/test/tt.txt')
    print(p.parent)
