import argparse
import random

# lc -- language confluxer (http://www.ruf.rice.edu/~pound/revised-lc)
#
# - Written by Christopher Pound (pound@rice.edu), July 1993.
# - Loren Miller suggested I make sure lc starts by picking a
#   letter pair that was at the beginning of a data word, Oct 95.
# - Cleaned it up a little bit, March 95; more, September 01
#
# The datafile should be a bunch of words from some language
# with minimal punctuation or garbage.  Try 
# mixing and matching words from different languages to get just 
# the balance you like.  The output of course needs some editing.
#
# Ported to python by David Borne 02.15.2022

def lc(file, ignore_case=False):
    with open(file) as f:
        data = ''.join([x.strip()+' ' for x in f.readlines()])

    if ignore_case: data = data.lower()
    
    hash = {}
    start_pairs = set()
    while len(data) > 2:
        (first, second, third) = data[0:3]
        if first == ' ': 
            start_pairs.add(second+third)
        elif second != ' ':
            hash.setdefault(first+second, set()).add(third)
        data = data[1:]
    
    # sets to lists for more efficient random.choice-ing
    hash = {k:list(v) for (k,v) in hash.items()}
    start_pairs = list(start_pairs)
    
    #print ([(key,hash[key]) for key in sorted(hash.keys())])
    #for key in sorted(hash.keys()):
    #    print (key,hash[key])
    return (hash, start_pairs)

def new_word(hash, start_pairs, min_length, max_length):
    word = random.choice(start_pairs)
    done = False
    while not done:
        pair = word[-2:]
        letter = random.choice(hash[pair])
        if letter == ' ':
            if len(word) >= min_length:
                done = True
            elif len(hash[pair]) == 1:
                while (len(hash[word[-2:]]) == 1) and len(word)>2:
                    word = word[:-1]
                if len(word) == 2:
                    word = random.choice(start_pairs)
        else :
            word += letter
            if len(word) >= max_length:
                while (' ' not in hash[word[-2:]] and len(word)>min_length):
                    word = word[:-1]
                if len(word) >= min_length:
                    done = True
                
    return word

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Language Confluxer: Create artificial words from language samples.')
    parser.add_argument('file', metavar='filename',
        help='Language sample data text file name.')
    parser.add_argument('-n', '--number', metavar='N', type=int,
        help='Number of words to generate (default: 25).', default=25)
    parser.add_argument('-m', '--min_length', metavar='min', type=int,
        help='Minimum length of generated words.'
             'Note: if there are words in the dataset shorter than min_length,'
             'this may loop forever. (default: 3)', default=3)
    parser.add_argument('-M', '--max_length', metavar='max', type=int,
        help='Maximum length of generated words. (default: 7)', default=7)
    parser.add_argument('-i', '--ignore_case', action='store_true',
        help='Ignore letter case in data. (output will be all lower-case)')

    args = parser.parse_args()
    (hash, start) = lc(args.file, args.ignore_case)
    print ([new_word(hash, start, args.min_length, args.max_length) for x in range(args.number)])


# TODO: port these over as well
'''
#!/usr/local/bin/perl
#
# prop - turn output from "lc" into proper names;
# 	excess short or long words may be discarded.
# written by Christopher Pound (pound@rice.edu) Oct 1995.
#
# Run as "lc -[number of words] datafile | prop"
#
# prop puts together one short name and one long name.
# Define the number of vowels a short name has right HERE:

$vowel_cutoff=3;

#
#
srand(time);
while(<>){
  chop;
  ($c, $v)=0;
  @a=split('',$_);
  while(@a){
    $c=pop@a;
    if ($c=~/[aeiou]/) {$v++;}
  }
  if ($v < $vowel_cutoff) {push(@short,$_);}
  else {push(@long,$_);}
}
if ($#short > $#long) {$#short=$#long;}
else {$#long=$#short;}
while(@short){
  $a=pop(@short);
  $ai=substr($a,0,1);
  $ai=~tr/[a-z]/[A-Z]/;
  substr($a,0,1)=$ai;
  $b=pop(@long);
  $bi=substr($b,0,1);
  $bi=~tr/[a-z]/[A-Z]/;
  substr($b,0,1)=$bi;
  if (int(rand(2))) {print "$a $b\n";}
  else {print "$b $a\n";}
}
'''

'''
#!/usr/local/bin/perl
#
# fix - adds some prefixes and suffixes to lc's output to make it
#       look more like a real language.  The affixes are taken from
#       the lc output and then added to it, too.  The number of
#       affixes is equal to the number of words you feed fix, divided
#       by ten.  Some attempt is made to put the affix in the right
#       place & to ensure that it'll be pronounceable.
#
# Written by Christopher Pound (pound@rice.edu) November 1996.
#
srand(time);
$howlong=int(rand(3))+2;
@basic=<>;
@words=@basic;
$lim=int($#basic/10)+1;
while ($found < $lim) {
  $word=splice(@words, rand @words, 1);
  chop($word);
  $pre=0;
  if ((int(rand(3))+1) == 3) { $fix=substr($word,0,$howlong); $pre=1; }
  else { $fix=substr($word,length($word)-$howlong,$howlong); }
  next unless ($fix=~/[aeiouy]/);
  $found++;
  $fixes{$found}=$pre.'#'.$fix;
}
foreach $w (@basic) {
  chop($w);
  if (int(rand(2))) { print "$w\n"; next; }
  $fix=$fixes{int(rand($lim))+1};
  ($pre,$fix)=split('#',$fix,2);
  if ($fix=~/^[aeiouy]/) { $vp=1; }
  if ($fix=~/[aeiouy]$/) { $vs=1; }
  if ($pre) {
    if (($w=~/^[aeiouy]/)&&($vs)) { $w=substr($w,1,length($w)-1); }
    $w=~y/A-Z/a-z/;
    print "$fix$w\n";
  }
  else {
    if (($w=~/[aeiouy]$/)&&($vp)) { $w=substr($w,0,length($w)-1); }
    $fix=~y/A-Z/a-z/;
    print "$w$fix\n";
  }
}
'''
