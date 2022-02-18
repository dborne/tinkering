import argparse
import textwrap

def cleanup_file(filename):
    with open(filename) as f:
        words = sorted(list(set(f.read().split())))
        words = [word for word in words if len(word)>2]
        words = ' '.join(words)
        words = textwrap.wrap(words, width=70, break_long_words=False, break_on_hyphens=False)
        return words

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='cleanup language files')
    parser.add_argument('filename', help='Language sample data text file name.')
        
    args = parser.parse_args()
    
    for line in cleanup_file(args.filename):
        print (line)
