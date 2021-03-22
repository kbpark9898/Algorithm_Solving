k, problems=map(int, input().split())

pokemons_num_name={}
pokemons_name_num={}
count=1
for i in range(k):
    pokemon = input()
    pokemons_name_num[pokemon]=str(count)
    pokemons_num_name[str(count)]=pokemon
    count+=1


for i in range(problems):
    quiz = input()
    if quiz in pokemons_name_num:
        print(pokemons_name_num[quiz])
    else:
        print(pokemons_num_name[quiz])

