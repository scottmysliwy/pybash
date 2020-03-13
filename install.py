import platform

pform = platform.system()

if pform == 'Linux':
    pass
elif pform == 'Darwin':
    pass

def a(name):
    def wrap(name, val):
        return f'{name} {val}'
    return wrap


class Command(object):

    def __init__(self, name, options = None):
        self.name = name
        self.options = options
   

    def fullCommand(self):
        return f'{self.name} {self.options}'

    def __getitem__(self, Key):
        self.options = Key
        return self.fullCommand()

    def make_command(self, command):
        self.options = command
        return f'{self.name} {command}'
    
    def __str__(self):
        return self.fullCommand()
    
    def __add__(self, other):
            return f'{self.fullCommand()}\n{other.fullCommand()}'
    
    

class Updater(object):
    
    def __init__(self, **kwargs):
        t = lambda key,val: f'{key} {val}'
        {key: setattr(self, key, Command(key, ' '.join(value))) if isinstance(value, list) or isinstance(value, tuple)
                else setattr(self, key, Command(key, value)) for key, value in kwargs.items()}

class Commands(Updater):
    pass

# git = Command('git')
# print(git['this is a test'])
git = Commands(**{'git':['a','scott'],'ssh':'sok','wc': ''})
print(git.wc['thu'])
print(git.git + git.wc)
