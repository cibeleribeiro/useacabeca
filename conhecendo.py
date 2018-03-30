

movies=[
    "TheThe Holly Grail",1975, "Terry Jones e Terry Gilliam" ,91,
        ["Graham Chapman",
            ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]

names = ['Michael','Terry']
isinstance(names, list)
True
num_names = len(names)
isinstance(num_names, list)
False

for each_item in movies:
    if isinstance(each_item,list):
        for nested_item in each_item:
            if isinstance(nested_item,list):
                  for deeper_item in nested_item:
                        print(deeper_item)
            else:
                   print(nested_item)
    else:
            print(each_item)

movies=[
    "TheThe Holly Grail",1975, "Terry Jones e Terry Gilliam" ,91,
        ["Graham Chapman",
            ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]

names = ['Michael','Terry']
isinstance(names, list)
True
num_names = len(names)
isinstance(num_names, list)
False

for each_item in movies:
      if isinstance(each_item, list):
        for ne_item in each_item:
            if isinstance(ne_item, list):
                  for dee_item in ne_item:
                      if isinstance(dee_item, list):
                            for deepest_item in dee_item:
                                  print(deepest_item)
                      else:
                            print(dee_item)
            else:
                  print(ne_item)
      else:
        print(each_item)

def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)
