import string, random

p = []
p.append(random.choice(string.punctuation))
p.append(random.choice(string.punctuation))
p.append(random.choice(string.digits))
p.append(random.choice(string.digits))
p.append(random.choice(string.ascii_uppercase))
p.append(random.choice(string.ascii_uppercase))
p.append(random.choice(string.ascii_lowercase))
p.append(random.choice(string.ascii_lowercase))
p.append(random.choice(string.ascii_lowercase))
p.append(random.choice(string.ascii_lowercase))
p.append(random.choice(string.ascii_lowercase))
p.append(random.choice(string.ascii_lowercase))
random.shuffle(p)
print ''.join(p)