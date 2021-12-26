sounds = {'clank':'a',
          'bong':'b',
          'click':'c',
          'tap':'d',
          'poing':'e',
          'clonk':'f',
          'clack':'g',
          'ping':'h',
          'tip':'i',
          'cloing':'j',
          'tic':'k',
          'cling':'l',
          'bing':'m',
          'pong':'n',
          'clang':'o',
          'pang':'p',
          'clong':'q',
          'tac':'r',
          'boing':'s',
          'boink':'t',
          'cloink':'u',
          'rattle':'v',
          'clock':'w',
          'toc':'x',
          'clink':'y',
          'tuc':'z',
          'whack':' '}

N = int(input())

string, CAPS, SHIFT = '', False, False
for i in range(N):
    key = input().strip()
    if key in sounds:
        string += sounds[key].upper() if CAPS and not SHIFT or not CAPS and SHIFT else sounds[key]
    elif key == 'bump':
        CAPS = not CAPS
    elif key == 'pop':
        string = string[:-1]
    elif key == 'dink':
        SHIFT = True
    elif key == 'thumb':
        SHIFT = False
print(string)
